<!-- title: Proxmox, NAT et DHCP -->
<!-- category: Hébergement Containers -->

J'ai eu beaucoup de retours à [mon dernier article](/2018/hebergement-et-taille-de-containers/) qui ont  alimenté ma réflexion et m'ont permis de clarifier mon objectif avec mon serveur [Proxmox](https://fr.wikipedia.org/wiki/Proxmox_VE).<!-- more --> J'ai décidé de pousser plus loin avec les containers LXC, de ne pas utiliser Docker sur le serveur mais d'améliorer certains aspects de mon installation : containeriser ce que j'ai installé directement sur l'hyperviseur (que ce soit par flemme, pour aller vite ou par manque de connaissances) et automatiser le déploiement de certains containers pour faciliter une éventuelle  migration et me permettre d'installer un environnement de test local.

Voici un diagramme à gros grain de l'architecture actuelle :

![Architecture Proxmox](/images/2018/archi-proxmox.jpg)

Au niveau de l'hyperviseur, on a un pare-feu et une interface *Bridge* et j'ai installé un serveur NginX au niveau de l'hyperviseur qui joue le rôle de proxy Web vers les containers. Cela implique de modifier la configuration de NginX à chaque ajout d'un service Web et donc de se connecter en SSH à l'hyperviseur. C'est le premier point que je compte améliorer en migrant ce serveur Web vers un container. Or les containers sont configurés en IP fixe. Pour simplifier les configurations, je veux attribuer les adresses IP par DHCP et d'utiliser des noms DNS plutôt que des adresses.

Au préalable, approfondissons la configuration réseau de mon Proxmox déjà en place... rien de révolutionnaire car la plupart de ces choix ont été documentés par d'autres (et j'ai seulement assemblé pour arriver à mes fins) mais ça permettra de mieux comprendre la partie DHCP qui arrive ensuite. Mon serveur est [une Dedibox hébergée chez Online](https://www.scaleway.com/fr/dedibox/) et Proxmox est une distribution officiellement supportée, donc l'installation initiale est réalisée via l'interface Web d'administration du serveur. De base, une interface physique est configurée avec l'adresse IP fixe du serveur et l'adresse IP de la passerelle. Online attribue une adresse IP fixe à chaque dédibox et on peut acheter des adresses IP supplémentaires. C'est idéal pour associer une adresse IP à chaque container, mais on ne va pas faire ça du tout car :

1. c'est coûteux (2 euros HT par IP / mois) pour le l'auto-hébergement,
2. chaque container est directement exposé sur Internet donc il doit être capable d'assurer sa sécurité.

On va plutôt créer un réseau privée (non routable sur Internet), caché derrière l'IP publique du serveur. Les containers peuvent envoyer du trafic sortant sans restriction et le trafic entrant passe par le tamis du pare-feu avant d'être redirigé vers le bon container. C'est similaire à ce qu'on a tous à la maison avec un réseau en 192.168.x.x. derrière une box ADSL (ou fibre pour les chanceux). Pour cela on crée une interface *bridge* nommée vmbr0 qui sert de passerelle aux containers et on ajoute une règle de translation d'adresse (NAT) pour faire passer le trafic sortant de vmbr0 vers l'interface physique enp1s0.

Configuration dans */etc/network/interfaces* :

    auto lo
    iface lo inet loopback

    auto enp1s0
    iface enp1s0 inet static
            address  xx.xx.xx.xx
            netmask  255.255.255.0
            gateway  xx.xx.xx.1

    auto vmbr0
    iface vmbr0 inet static
            address  10.10.10.1
            netmask  255.255.255.0
            bridge_ports none
            bridge_stp off
            bridge_fd 0
            post-up echo 1 > /proc/sys/net/ipv4/ip_forward
            post-up iptables -t nat -A POSTROUTING -s '10.10.10.0/24' -o enp1s0 -j MASQUERADE
            post-down iptables -t nat -D POSTROUTING -s '10.10.10.0/24' -o enp1s0 -j MASQUERADE

Sans surprise, le pare-feu de Proxmox est basé sur [iptables](https://fr.wikipedia.org/wiki/Iptables) et l'interface Web facilite vraiment sa configuration en présentant trois niveaux de pare-feu : un niveau datacenter (qui peut contenir plusieurs Proxmox si on gère un cluster), un niveau noeud et un niveau container. On peut activer le pare-feu à chaque niveau. 

Ma configuration de base est la suivante :

- au niveau datacenter

    - input policy = DROP : tout le trafic entrant non autorisé explicitement est rejeté
    - output policy = ACCEPT : tout le trafic sortant est autorisé
    - autoriser le PING entrant des serveurs ONLINE (62.210.16.0/24) pour qu'ils puissent m'avertir si mon serveur n'est plus joignable

- au niveau noeud (mon proxmox principal)

    - autoriser TCP/8006 entrant : l'accès distant à l'interface Web de Proxmox
    - autoriser SSH
    - autoriser HTTP et HTTPS

Pour finaliser l'aspect sécurisé, on peut installer fail2ban pour scruter les logs des services critiques et bannir les fâcheux.

A ce niveau là, on a un Promox opérationnel : les containers en IP fixe dans le réseau 10.10.10.0/24 peuvent communiquer avec l'extérieur. On va modifier le système pour fournir du DHCP. La première action consiste à remplacer [le serveur DNS Bind](https://fr.wikipedia.org/wiki/BIND) fourni avec Proxmox par [Dnsmasq](https://fr.wikipedia.org/wiki/Dnsmasq) qui combine les fonctions DNS et DHCP.

    systemctl disable bind9
    apt-get install dnsmasq

Et on crée un fichier de configuration dans */etc/dnsmasq.d/containers* :

        domain-needed
        bogus-priv

        no-poll
        no-hosts

        no-dhcp-interface=enp1s0
        interface=vmbr0

        expand-hosts
        domain=madyanne.lan

        dhcp-authoritative
        dhcp-leasefile=/tmp/dhcp.leases

        dhcp-range=10.10.10.100,10.10.10.200,255.255.255.0,12h
        dhcp-option=3,10.10.10.1
        dhcp-option=19,1
        dhcp-option=6,10.10.10.1

        cache-size=256

        log-facility=/var/log/dnsmasq.log
        #log-queries

Quelques points clés de la configuration :

- une allocation DHCP entre 10.10.10.100 et 10.10.10.200
- on fixe la passerelle de sortie 10.10.10.1
- un domaine *interne* : madyanne.lan
- les baux DHCP sont stockés dans un fichier */tmp/dhcp.leases*

Pour tester, je configure un container en DHCP, démarre le container et... ça ne marche pas :-) Le container n'arrive pas à récupérer une adresse IP. En fait, le pare-feu bloque les requêtes DHCP. Je débloque la solution en autorisant les ports UDP/67 et UDP/68 en entrée de l'interface vmbr0.

La configuration du pare-feu au niveau Proxmox est la suivante :

![Configuration pare-feu](/images/2018/proxmox-firewall-rules.png)

Ainsi configuré, cela fonctionne ! Dnsmasq ajoute automatiquement les noms obtenus par DHCP à son service DNS. Ainsi depuis n'importe quel container je peux adresser un autre container par nom court :

    # ping dev
    PING dev (10.10.10.100) 56(84) bytes of data.
    64 bytes from dev.madyanne.lan (10.10.10.100): icmp_seq=1 ttl=64 time=0.137 ms
    64 bytes from dev.madyanne.lan (10.10.10.100): icmp_seq=2 ttl=64 time=0.076 ms

Il reste un problème en suspens : les containers de type Alpine ont le mauvais goût de ne pas propager leur nom au serveur DHCP ; c'est peut-être paramétrable dans leur [service Udhcpc](https://wiki.alpinelinux.org/wiki/Udhcpc), il faut que je regarde...

Ma prochaine évolution consiste à migrer le serveur NginX installé par mes soins au niveau de le Proxmox vers un container dédié avec la gestion des certificats SSL Let's Encrypt.