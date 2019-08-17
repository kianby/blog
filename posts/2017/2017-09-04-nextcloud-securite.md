<!-- title: Sécurité des données, focus sur Nextcloud -->
<!-- categories: Hébergement BSD -->
<!-- tag: planet -->

En 2007, j'ai ouvert un compte Dropbox avec l'offre gratuite de 2 Go. J'avais
parrainé des collègues et des amis pour gagner de l'espace de stockage. Oui je
le reconnais, j'avais vendu des amis au
[GAFAM](https://fr.wikipedia.org/wiki/GAFAM) contre quelques octets<!-- more --> : mes
~~parrainages~~ compromissions m'avaient permis d'atteindre 6 Go de stockage...
Vertigineux ;-) A cette époque, ma fibre libriste était encore latente, j'étais
fier d'avoir autant d'espace et je m'en servais pour partager des photos avec la
famille. Je ne me suis jamais senti assez en confiance pour partager des
documents importants.

En 2010, j'ai commencé à héberger mes services et en 2014 je démarrais avec
[Owncloud](https://owncloud.org) principalement pour  la synchronisation des
contacts et du calendrier. Puis j'ai commencé à partager quelques fichiers, mais
rien d'important. En 2015, j'ai remplacé Owncloud par [Cozy](https://cozy.io),
de la fameuse  startup française qui oeuvre pour que l'utilisateur reprenne le
contrôle de sa vie numérique et ne la brade plus aux GAFAM. Cozy va plus loin
que le partage de fichiers et c'est vraiment un projet à suivre de près. C'est
avec eux que j'ai commencé à prendre confiance et partager des documents
importants. Et en 2016, je suis revenu vers Owncloud ou plus exactement vers son
fork né des guéguerres internes : [Nextcloud](https://nextcloud.com).

Bref mon compte Dropbox ne me servait plus depuis un bail mais j'avais du mal à
décider sa fermeture... mince c'était quand même gratuit ;-) Aujourd'hui il est
officiellement clôturé.

Donc j'ai quelques Giga octets de données sur Nextcloud, notamment des documents
administratifs, et je suis responsable de la sécurité de mes données. Alors la
sécurité c'est un vaste sujet. Cela commence par une protection physique des
données. Si mon serveur était à la maison, j'aurais probablement chiffré le
disque dur en cas de vol. Là il est chez un fournisseur de confiance, dans un
datacenter sécurisé donc l'accès direct à mon disque dur est le moins probable.

![Mr Robot dans le data center](/images/2017/mrrobothack.jpg)

La pierre angulaire de la sécurité c'est le système d'exploitation et ses
capacités intrinsèques à résister aux attaques. Ensuite c'est de la
configuration : le parefeu, le routage réseau, la virtualisation, des outils de
détection d'attaques qui vont permettre d'améliorer la sécurité du système. Mais
si le système d'exploitation est gâté à la base, tout ce qui suit est un
emplâtre sur une jambe de bois ! Enfin on se comprend :-)

![Tux et BSD grillent XP](/images/2017/tux-bsd-windows.jpg)

Depuis quelques mois, mon serveur est propulsé par OpenBSD (et je ne suis pas
prêt de revenir en arrière). Avec de la lecture et des conseils, je l'ai
sécurisé du mieux que j'ai pu. Je n'entrerai pas dans les détails, je ne suis
pas assez qualifié pour donner des cours sur le sujet mais le résultat n'est pas
mal du tout.

Pour la sécurité de mes données, ce qui m'inquiète le plus ce sont les failles
potentielles des applications hébergées qui pourraient servir de porte d'entrée
royale pour accéder aux données. La parano venant, j'ai décidé d'attaquer le
sujet par étapes et aujourd'hui j'ai focalisé sur mon instance **Nextcloud**.
C'est une application Web avec son propre sous-domaine qui donne directement sur
ce bel écran de connexion :  

![Nextcloud login](/images/2017/nextcloud-login.png)

J'accède à mes données en mobilité donc il n'est pas possible de restreindre
l'accès par adresse IP. Donc je suis dépendant du système d'authentification de
Nextcloud. Première étape, je dois savoir ce qui se passe. Nextcloud fournit un
rapport d'audit et on peut configurer les actions qui doivent y figurer.

![Nextcloud audit](/images/2017/nextcloud-audit.png)

C'est une fonction nécessaire mais pas suffisante. Le rapport est envoyé chaque
heure si des données ont changé, un peu tard si on s'est fait ~~ni~~ha-cker.

Exemple de rapport :

    Bonjour,

    Vous recevez cet email car l'activité suivante a eu lieu sur https://nextcloud.mondomaine.fr/

    * Vous avez partagé Partage/Blog/documents avec un lien public - Aujourd’hui 16:54:04
    * Partage/Blog/documents/moderncv.zip téléchargé par lien public - Aujourd’hui 16:54:48
    * Vous avez créé Notes/todo.txt - Aujourd’hui 17:04:49

Ce que j'aimerais aussi avoir, c'est un moyen de bloquer les gars qui font du
[brute-force](https://fr.wikipedia.org/wiki/Attaque_par_force_brute) sur l'écran
de connexion pour trouver mon mot de passe. C'est faisable si l'application a la
bonne idée de noter dans un log quand une tentative de connexion échoue :

- Sous Linux, l'excellent outil fail2ban (ben oui c'est du Python) permet d'analyser un
log à la recherche de messages spécifiques, d'extraire l'adresse IP concernée et
de créer une règle de blocage dans le parefeu (iptables) pour une durée
déterminée.
- Sous OpenBSD, Thuban s'est inspiré de fail2ban pour créer [Vilain](https://yeuxdelibad.net/Blog/?d=2017/02/05/09/53/19-vilain-setoffe) qui
fonctionne de concert avec l'incroyable parefeu [pf](https://man.openbsd.org/pf.conf).  

Ce qui suit est donc réalisé avec Vilain sous OpenBSD mais c'est facilement transposable sous Linux.

Je bloque les fâcheux pendant une heure avec cette règle pour Vilain qui
fonctionne aussi bien pour l'écran de connexion à l'interface Web que pour
l'accès aux fichiers avec WebDAV.

    [nextcloud]
    logfile = /var/www/htdocs/datacloud/nextcloud.log
    regex = .*Bruteforce attempt from \\"(.*)\\" detected

Quid des partages par lien public ? En effet, Nextcloud permet aussi de partager
un fichier ou un dossier à quelqu'un qui n'a pas de compte avec un lien public.
La création d'un partage est aussi simple que ceci :

![Nextcloud partage](/images/2017/nextcloud-partage.png)

La sécurité repose essentiellement sur l'URL générée *au hasard* donc le partage
d'un document important sans spécifier de mot de passe est à proscrire.
D'ailleurs l'interface d'administration de Nextcloud permet d'interdire la
création de tels liens par les utilisateurs. J'utilise assez souvent ces liens
publics et je ne m'étais jamais posé la question de leur sécurité. Alors
mauvaise nouvelle, si on crée un lien avec mot de passe et que l'URL tombe dans
les mains d'un malfaisant (ou réussit à être devinée), il peut tranquillement
faire du brute-force sur le lien car Nextcloud n'écrit aucune info dans ses logs
sur ces erreurs d'authentification. Pas cool ça hein <i class="fa fa-ambulance" aria-hidden="true"></i>


La solution va venir du logs d'accès du serveur HTTP qui trace toutes les
requêtes HTTP et leur code retour. Pour un accès avec le bon mot de passe,
on aura un log comme celui-ci :

    80.214.223.96 - - [02/Sep/2017:12:36:58 +0200] "POST /s/wKDvKK8vt6ZSU5E/authenticate HTTP/1.1" 303 5 "-" "Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2163 Mobile Safari/537.35+"

Alors que pour un accès refusé car le mot de passe est incorrect on aura ceci :

    80.214.223.96 - - [02/Sep/2017:12:36:27 +0200] "POST /s/wKDvKK8vt6ZSU5E/authenticate HTTP/1.1" 200 16186 "-" "Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2163 Mobile Safari/537.35+"

Alors au premier abord, ça semble bizarre car l'erreur de mot de passe renvoie
un code HTTP 200 qui correspond à OK. C'est parce qu'en cas d'erreur, on reste
sur la page qui redemande le mot de passe, alors qu'en cas de succès le code de
retour est une redirection HTTP 303 vers la page qui affiche les documents du
partage. Le formatage de mes logs d'accès dépend de la configuration de mon
serveur HTTP (en l'occurence NginX) donc l'expression régulière qui permet
d'identifier les erreurs de mot de passe doit en tenir compte. Sur cette base je
peux rajouter la règle suivante à Vilain :

    [nextcloud-share]
    logfile = /var/www/logs/access-nextcloud.log
    regex = (\d+\.\d+\.\d+\.\d+) \-.*POST /s/\w+/authenticate HTTP/1.1\" 200

Voilà, nous avons deux règles efficaces qui vont bloquer les attaquants à chaque
double échec d'authentification. C'est cool mais je voudrais aussi connaître le
nombre de mes ennemis, car si je suis soumis à des centaines d'attaques par jour
je réviserai peut-être ma façon de me protéger. Je vais donc m'envoyer un rapport
journalier de l'activité de Vilain :  

- je modifie la configuration de Vilain pour qu'il écrive dans un log dédié et non plus dans */var/log/daemon*
- je configure un recyclage journalier pour ce log à minuit
- j'ajoute une tâche CRON à minuit moins 2 brouettes pour m'envoyer par e-mail le log de la journée

Quelque chose comme ça :

    # /etc/newsyslog.conf
    /var/log/vilain                         640  5     *    $D0   Z "rcctl restart vilain"

    # crontab
    55       23     *       *       *       cat /var/log/vilain | mail -s "Vilain Rapport" yax

Oui je l'ai appelé le **Vilain Rapport**, au niveau de l'humour on ne se refait pas :-)
