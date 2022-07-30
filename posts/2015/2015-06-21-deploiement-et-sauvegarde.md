<!-- title: Déploiement et sauvegarde -->
<!-- category: Hébergement -->
<!-- tag: planet -->

J'ai terminé la migration de mon serveur.<!-- more --> [Comme
annoncé](http://blogduyax.madyanne.fr/hebergement-en-mouvance.html) j'ai
utilisé l'outil de déploiement
[Ansible](https://fr.wikipedia.org/wiki/Ansible_%28logiciel%29) pour :

- conserver l'historique d'installation du serveur,
- valider au préalable sur une machine virtuelle locale l'installation de
  nouveaux services,
- être capable de rapidement redéployer un nouveau serveur.

J'ai d'abord écrit un playbook de base qui configure à mon goût une Debian
fraîchement installée : paquets supplémentaires, création des utilisateurs,
préférences de Bash, Tmux et Vim. Les préférences sont récupérées depuis [mon
projet dotfiles sur GitHub](https://github.com/kianby/dotfiles) et Ansible
s'occupe de leur installation. Si demain je modifie mon prompt Bash ou si
rajoute un plug-in à ma configuration Vim, je peux facilement synchroniser les
changements avec un *git pull*. Ce playbook m'a déjà resservi sur le plan
professionnel, c'est un investissement de temps déjà rentabilisé. Je l'ai
publié dans [un projet provisioning sur
GitHub](https://github.com/kianby/provisioning).

Le second playbook est beaucoup plus personnel puisqu'il déploie ce blog. En
cas de pépin il me permettra de me remettre en ligne rapidement. C'est un
playbook qui peut servir de tutorial, il n'est pas complexe mais mixe
différents types de tâches : installation de fichiers, manipulation de GIT,
enregistrement de tâches dans Cron.

Ceci dit, à contrario de mon idée initiale, je n'ai pas écrit de playbooks pour
l'intégralité des services à déployer car c'est très consommateur en temps (or
je suis fainéant : souvenez vous je suis développeur) et c'est peu intéressant
pour des services faciles à installer et périssables. Je prends pour exemple
[Piwik, l'outil de statistiques de site Web](https://piwik.org/) ; c'est une
application LAMP (Linux, Apache, MySQL, PHP) classique qui par la suite est
capable de se mettre à jour elle-même. Je n'ai pas vu d'intérêt à créer un
playbook pour installer une version de Piwik qui sera obsolète dans 2 mois et
de passer du temps à maintenir un playbook au lieu de maintenir mon serveur.
Mes autres services, soit moins critiques, soit mis à jour automatiquement ont
donc été installés manuellement : Piwik, Tiny Tiny RSS, Owncloud, Shaarli et
Roundcube.

L'installation est donc achevée, je suis à priori capable de remonter le blog
en moins de deux heures sur un nouveau serveur (ce qui prendra plus de temps
c'est de faire pointer les DNS vers la nouvelle adresse du site). Il me reste
à détailler le sujet des sauvegardes.

Mon besoin est modeste mais précis :

- les articles du blog sont déjà sauvegardés dans
  [GitHub](https://github.com/kianby/blog) (merci les blogs statiques) mais je
  dois sauvegarder les commentaires,
- sauvegarder la base de donnée MySQL de Tiny Tiny RSS n'a aucun intérêt mais
  sauvegarder le fichier OPML qui contient mes abonnement RSS est important,
- sauvegarder mes favoris conservés par Shaarli est essentiel,
- peu m'importe mes fichiers synchronisés avec Owncloud puisque j'ai une copie
  locale par contre il m'importe de sauvegarder mon calendrier.
- sauvegarder les configuration du serveur HTTP (NginX dans mon cas)

Ma solution est atypique et peut-être un mauvais exemple mais elle répond à mon
besoin et je n'avais aucune envie de sortir la grosse artillerie, de dumper
toutes mes bases et tout mon répertoire /var/www avec des centaines de fichiers
pour créer des grosses archives sauvegardées incrémentalement vers ... un FTP
distant ou autre. Je suis parti du principe qu'en cas de crash, je serais
capable de remonter le blog rapidement et que je prendrais plus de temps pour
remonter mes services donc je focalise sur les données de ces services.  Ce qui
est important par contre, c'est d'avoir une sauvegarde avec rotation qui
conserve les 2 derniers jours, 2 dernières semaines et 2 derniers mois  pour
avoir un historique et revenir en arrière en cas de problème. J'ai donc
personnalisé [un modeste shell
script](https://nicaw.wordpress.com/2013/04/18/bash-backup-rotation-script) qui
a le bon goût de gérer la rotation des sauvegardes, pour :

- d'abord récupérer toutes mes données à sauvegarder à droite à gauche par
  différents moyens : copie, extraction avec les API proposées par les
  applications,
- et ensuite envoyer la sauvegarde quelque part.

Sachant que je n'ai pas d'autre serveur ou d'espace FTP je me suis demandé où
serait ce *quelque part*. J'ai regardé un peu [la solution
Hubic](https://hubic.com/fr/) mais la complexité pour en détourner l'usage de
base qui est la synchronisation de fichiers et monter l'espace Hubic comme
stockage distant m'a peu motivé. Une sauvegarde c'est bien quand ça fait son
boulôt et qu'on l'oublie. J'ai moins de 2 Mo à sauvegarder par jour j'ai donc
eu une idée, tordue au premier abord et peut-être bien aussi au second (d'un
autre côté je suis le gars qui s'acharne à greffer des systèmes de commentaires
à des blogs statiques donc ça n'étonnera peut-être pas grand monde) : balancer
mes sauvegardes dans Owncloud ainsi elles seront synchronisées sur mes machines
locales et j'aurais une notification journalière que la sauvegarde s'est bien
déroulée.

Voici donc les grandes lignes de la partie **récupération des données** :

```shell
# Les fichiers de configuration de NginX
cp -r /etc/nginx/* $TARGET_DIR/nginx/.

# Les favoris de Shaarli stockées dans des fichiers PHP
cp /var/www/shaarli/data/* $TARGET_DIR/shaarli/.

# Le fichier OPML de Tiny Tiny RSS par son URL publique
wget "http://ttreader.madyanne.fr/opml.php?op=publish&key=XYXYXYXYXYXYXYXYXYX" \
        -O $TARGET_DIR/reader/reader.opml

# Le fichier ICS du calendrier Owncloud
OC_USER=owncloud_user
OC_PWD=owcloud_password
wget --no-check-certificate --auth-no-challenge --no-clobber \
        --http-user=$OC_USER --http-password=$OC_PWD \
        -O $TARGET_DIR/owncloud/cal.ics \
        "https://owncloud.madyanne.fr/index.php/apps/calendar/export.php?calid=1"
```

Suite à cela, le script crée une belle archive et la copie dans un répertoire
*backup* de mes fichiers Owncloud. Ce n'est pas suffisant pour qu'elle soit
synchronisée par Owncloud car on l'a copié en douce. Il faut forcer Owncloud à
rescanner son répertoire avec la commande suivante exécutée en tant
qu'utilisateur *www-data*:

```shell
su -c "/usr/bin/php /var/www/owncloud/console.php files:scan all" \
-s /bin/sh www-data
```

Il reste encore un peu de peaufinage mais ça semble faire le boulôt et je vois la
fin du tunnel de cette migration de serveur.

![Rabbit](/images/2015/rabbit_hole.jpg)
