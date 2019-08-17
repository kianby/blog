<!-- title: Installation d'un serveur de containers -->
<!-- categories: Hébergement Containers -->
<!-- tag: planet -->

Plus des notes techniques pour ma mémoire défaillante qu'un véritable article, je vais compiler les étapes d'installation d'un serveur de containers.<!-- more --> Quel système d'exploitation ? j'ai envie de dire on s'en cogne mais il est préférable de choisir une distribution poussée par Docker pour se simplifier la vie ; ce sera donc Debian 9 *Stretch* supportée sur Dedibox. 

J'installe donc via l'interface d'administration Online. Je choisis le mot de passe *root*, le compte utilisateur et son mot de passe. Online me communique ma configuration réseau :

- Adresse IP : xxx.yyy.zzz.xxx
- Masque réseau : 255.255.255.0
- Passerelle : xxx.yyy.zzz.1
- DNS primaire : 62.210.16.6
- DNS secondaires : 62.210.16.7

# SSH

Je vérifie qu'on peut se connecter au serveur : 

    ssh yax@xxx.yyy.zzz.xxx

Je me déconnecte et génère une clef avec **ssh-keygen**, en choisissant une clef RSA. On peut fournir une *passphrase* si on pense qu'elle peut tomber entre de mauvaises mains. Je nomme ma clef *fr_mondomaine* ; cela génère une clef publique *fr_mondomaine_rsa.pub* et une clef privée *fr_mondomaine_rsa*. 

Je copie la clef publique sur le serveur : 

    ssh-copy-id -i fr_mondomaine_rsa.pub yax@xxx.yyy.zzz.xxx

On peut simplifier la connexion au serveur en modifiant la configuration du client SSH *~/.ssh/config* de sa machine pour que l'utilisateur et la clef soient choisis sans le spécifier sur la ligne de commande : 

    Host fr.mondomaine
        User yax
        Hostname xxx.yyy.zzz.xxx
        IdentityFile ~/.ssh/fr_mondomaine_rsa

Je vérifie qu'on se connecte sans saisir de mot de passe :

    ssh fr.mondomaine

J'interdis complètement la connexion SSH au compte *root*. Pour cela, je me connecte au serveur, je passe en *root* avec **su** et j'édite le fichier de configuration du service SSH */etc/ssh/sshd_config* pour fixer les paramètres suivants :

    PermitRootLogin no
    PasswordAuthentication no

Je redémarre le service SSH : 

    systemctl restart sshd

Et si on s'est raté ou si on perd la clef RSA sur notre PC à la maison ? Et bien on est bon pour redémarrer le serveur en mode secours avec la console Dedibox, monter les partitions et se *chrooter* pour arranger la configuration de SSH. C'est encore faisable facilement car systemd n'a pas encore binarisé tout le système (*troll inside*).

Je ne configure pas **sudo**, je veux pouvoir tout faire avec un utilisateur standard, les connexions à root par **su** doivent rares, principalement pour effectuer les mises à jours du système Debian.

# Docker

Installation de Docker CE sur Debian Stretch avec la procédure officielle qui ajoute des dépôts APT Docker pour récupérer une version de Docker plus récente que celle fournie avec Debian Stretch : https://docs.docker.com/engine/installation/linux/docker-ce/debian/

Installation d'une version récente de **Docker Compose** en suivant aussi la procédure officielle : https://docs.docker.com/compose/install/

Ajout de l'utilisateur yax dans le groupe docker 

    usermod -aG docker yax

Démarrage automatique de Docker:

    systemctl enable docker

# Pare-feu 

J'installe **shorewall** pour IPv4, un pare-feu puissant qui ne rajoute pas de service supplémentaire au système puisqu'il traduit ses règles assez complexes en règles *iptables*.

    apt-get install shorewall

Par sécurité, le temps de mettre au point les règles, je désactive le démarrage automatique :

    systemctl disable shorewall

Si ça foire, je pourrai toujours forcer un redémarrage électrique du serveur :-) 

Docker a la particularité de gérer ses propres règles *iptables* pour l'accès aux containers ce qui rend sa cohabitation délicate avec tout pare-feu basé sur *iptables* Depuis quelques versions, Shorewall supporte Docker, ce qui revient à dire qu'il le laisse faire sa sauce et gère les règles *iptables* qui lui sont propres.

Donc j'édite */etc/shorewall/shorewall.conf* et déclare que je vais utiliser Docker : 

    STARTUP_ENABLED=Yes
    DOCKER=Yes

Puis j'édite */etc/shorewall/zones* pour définir mes zones :

    #ZONE         TYPE        OPTIONS
    fw            firewall
    net           ipv4
    dock          ipv4        # 'dock' is just an example

Et les règles de passage d'une zone à l'autre en éditant */etc/shorewall/policy* :

    #SOURCE        DEST        POLICY         LEVEL
    $FW            net         ACCEPT
    net            all         DROP           info 
    dock           $FW         REJECT
    dock           all         ACCEPT
    # last rule
    all            all         REJECT         info

Enfin, j'associe les zones aux interfaces physiques (attention *enp1s0* est le nom de l'interface Ethernet de mon serveur), en éditant */etc/shorewall/interfaces* : 

    ?FORMAT 2
    #ZONE          INTERFACE        OPTIONS
    net            enp1s0           dhcp,tcpflags,logmartians,nosmurfs,sourceroute=0
    dock           docker0          bridge,routeback=0   #Disallow ICC

Là on a un pare-feu opérationnel qui refuse toute connexion entrante ; on ajoute quelques règles pour autoriser le PING ICMP et les connexions SSH avec une limite de 3 connexions par minute (pour calmer les facheux). 

Ca se passe dans le fichier */etc/shorewall/rules* : 

    #ACTION		SOURCE		DEST		PROTO	DEST	SOURCE		ORIGINAL	RATE		USER/	MARK	CONNLIMIT	TIME		HEADERS		SWITCH		HELPER
    #							PORT	PORT(S)		DEST		LIMIT		GROUP
    ?SECTION ALL
    ?SECTION ESTABLISHED
    ?SECTION RELATED
    ?SECTION INVALID
    ?SECTION UNTRACKED
    ?SECTION NEW

    # Drop packets in the INVALID state

    Invalid(DROP)  net    	        $FW		tcp

    # Drop Ping from the "bad" net zone.. and prevent your log from being flooded..

    Ping(ACCEPT)	net		$FW

    # Permit all ICMP traffic FROM the firewall TO the net zone
    ACCEPT	    	$FW		net		icmp

    SSH(ACCEPT) 	net             all        	-        -            -         -                s:1/min:3


# Tester la sécurité

Là ça devient plus amusant ! Je reboote et je démarre manuellement shorewall puis je jette un oeil à la bonne cohabitation des règles **iptables** entre Shorewall et Docker :

    iptables -L -n -v

D'abord je teste les accès distants :

- on peut scanner les ports avec NMAP depuis sa machine : on voit le port 22 ouvert 
- on vérifie facilement que SSH est limité à 3 connexions par minute

Enfin je teste la sécurité intra-docker en déployant 3 containers Docker avec [l'image tcpping](https://hub.docker.com/r/kianby/tcpping/) :

    version: "3"
    services:
      web1:
        image: tcpping
        expose:
          - 80
        networks:
          - frontend
      web2:
        image: tcpping
        networks:
          - frontend
          - backend
      web3:
        image: tcpping
        ports:
          - 8000:80
        networks:
          - backend
    networks:
      frontend:
      backend:

Les containers web1 et web2 sont sur le réseau *frontend*
Les containers web2 et web3 sont sur le réseau *backend*

Je vérifie les points suivants : 

- chaque container peut accèder à Internet
- aucun container ne peut accéder au serveur : ni ping, ni SSH
- web1 et web2 se voient en ICMP et en TCP 80
- web2 et web3 se voient en ICMP et en TCP 80 

Je refais un scan de port plus poussé avec NMAP et je vois que le port 22 et 8000 (celui de web3) sont accessibles depuis Internet. 

Si je liste les règles *iptables*, je remarque que l'isolation des réseaux entre les containers donne lieu à des règles *iptables* supplémentaires.