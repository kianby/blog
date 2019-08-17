<!-- title: Retour d'expérience Ubuntu Touch -->
<!-- category: Mobilité -->
<!-- tag: planet -->

L'article peut sembler opportuniste par rapport aux rumeurs d'abandon de
Firefox OS mais il n'en est rien<!-- more --> (je le jure votre honneur). C'est seulement
que j'ai eu la chance de toucher un Nexus 4 (merci Papa) et j'en ai profité
pour tester le système Ubuntu Touch pendant une semaine dans mon utilisation
quotidienne. En effet, ce téléphone est un des téléphones de référence pour la
société Canonical, toujours maintenu alors que leur OS, très discret, fêtera
bientôt sa 3ème bougie. Depuis le lancement de Ubuntu Touch, trois téléphones
ont été commercialisés : deux modèles du constructeur espagnol BQ qui semblent
très appréciés par la communauté Ubuntu et un modèle assez puissant, le MX4 du
constructeur chinois Meizu.

<img src="/images/2015/ubuntu-about.png" alt="A propos" style="margin: 0px 20px;
float:left;" />Ca commence donc par l'installation du système qui est assez
simple car d'une part le Nexus 4 a un booloader facile à déverrouiller et
Ubuntu Touch est basé sur un Android, on utilise donc des outils Android (adb,
fastreboot) pour flasher le système. Ensuite les outils Canonical
interviennent, la voie simple consiste donc à s'installer une version Desktop
de Ubuntu 14.04 ou supérieure sur un PC afin d'obtenir ces outils facilement.
Je me suis donc basé sur [la documentation officielle du Ubuntu
Developer](https://developer.ubuntu.com/en/start/ubuntu-for-devices/installing-ubuntu-for-devices)
et [sur cet
article](http://www.pcadvisor.co.uk/how-to/linux/how-install-ubuntu-touch-image-3531970)
qui apporte quelques précisions pour le Nexus 4. On a le choix entre deux
canaux de mise à jour système : stable ou développement.  Pour me faire une
idée la plus juste du système et ne pas la fausser avec des bugs d'une version
en cours de développement, j'ai choisi la version stable. Ce qui est
intéressant avec Ubuntu Touch, c'est que la version mobile fait partie
intégrante du développement de Ubuntu, il ne s'agit d'un développement à part,
déconnecté de la version *Desktop*. Après une installation fraîche, on a donc
un téléphone en version 15.04 et on reçoit des OTA (mise à jour) régulièrement.
On devrait d'ailleurs bientôt basculer en version 15.10. Canonical a une vision
précise de ce qu'il veulent obtenir avec leur système et cela s'appelle
Convergence. Un système mobile qui, une fois connecté à un clavier / souris en
bluetooth et à un moniteur se transforme en *Ubuntu Desktop* capable d'exécuter
les applications usuelles comme Libre Office ou Gimp.

Pour moi, Convergence est un rêve de Geek et on a du mal à imaginer le quidam
moyen utiliser son téléphone comme ordinateur. Et pourtant c'est un des
principaux avantages de Touch : on n'a pas un système Unix-like castré mais un
système GNU/linux complet. Je me suis plusieurs fois surpris à buter sur la
manière de faire certaines choses parce que l'interface graphique n'est pas
encore complète sur certains point et qu'il faut raisonner ligne de commande
avec les outils usuels : du shell script (SH ou BASH) et des tâches CRON. Mais
je m'emballe, faisons d'abord un petit tour en images du système.

**L'écran de déverrouillage et ses statistiques amusantes :**

<img src="/images/2015/ubuntu-unlock1.png" alt="ubuntu unlock"/>

<img src="/images/2015/ubuntu-unlock2.png" alt="ubuntu unlock"/>

**L'écran principal avec ses applications en rang d'oignons:**

<img src="/images/2015/ubuntu-appli1.png" alt="ubuntu application"/>

<img src="/images/2015/ubuntu-appli2.png" alt="ubuntu application"/>

**Les applications favorites sur la gauche en faisant glisser le bord gauche de l'écran**

**et les applications lancées en faisant glisser le bord droit de l'écran :**

<img src="/images/2015/ubuntu-unity.png" alt="ubuntu unity"/>

<img src="/images/2015/ubuntu-tasks.png" alt="ubuntu tasks"/>

**Les paramètres système et un aperçu du magasin d'applications :**


<img src="/images/2015/ubuntu-settings.png" alt="ubuntu settings"/>

<img src="/images/2015/ubuntu-store.png" alt="ubuntu store"/>

A part la particularité du tirage des bords d'écran pour faire apparaître la
barre latérale ou passer d'une application à l'autre mais on pige vite le coup,
on est dans une interface classique, on n'est pas perdu. Les paramètres sont
similaires à ce qu'on peut trouver sur d'autres systèmes, le magasin Ubuntu
Store est plus conséquent que ce à quoi je m'attendais. De ce que j'ai lu sur
les forums de discussion Ubuntu, l'équipe Canonical a mis le focus sur le
système dans un 1er temps, les applications viendront ensuite. Voici une liste
de ce qui marche et de ce qui dysfonctionne sur le Nexus 4 en 15.04 OTA 8:

- la téléphonie fonctionne (oui c'est bien de l'écrire pour rassurer tout le
  monde)
- l'envoi de SMS et de MMS fonctionne mais j'ai un doute sur la réception MMS
  (je crois en avoir raté un)
- le bluetooth est présent mais je n'ai pas réussi à le faire fonctionner avec
  mon main-libre Jabra malgré un appairage réussi.
- le GPS est capricieux
- le tethering USB fonctionne. la fonction Hotspot Wi-Fi est censée être
  présente mais je ne l'ai pas vu dans mes paramètres.
- l'application e-mail officielle *Dekko* est fonctionnelle depuis peu. Elle est
  agréable à utiliser.
- les applications *contact* et *calendrier* sont présentes et bien faîtes.
- les performances du systèmes sont acceptables mais perfectibles (on a une
  patience d'1 à 2 secondes à chaque lancement d'application)

Deux sujets ont exigé de mettre le nez dans la ligne de commande car ils ne
sont pas (encore) configurables par l'interface graphique : les sonneries
personnalisées et la synchronisation des contacts et du calendrier.

D'abord il nous faut un accès SSH sur la bête. On active le mode *développeur*
depuis les paramètres du téléphone et on se connecte avec *adb shell* pour
activer le service SSH  Ensuite on copie la clef publique de notre PC sous
GNU/Linux dans le téléphone. Ca donne en gros les étape suivantes lues sur
[AskUbuntu](http://askubuntu.com/questions/348714/how-can-i-access-my-ubuntu-phone-over-ssh)

    adb shell android-gadget-service enable ssh
    adb shell mkdir /home/phablet/.ssh
    adb push ~/.ssh/id_rsa.pub /home/phablet/.ssh/authorized_keys
    adb shell chown -R phablet.phablet /home/phablet/.ssh
    adb shell chmod 700 /home/phablet/.ssh
    adb shell chmod 600 /home/phablet/.ssh/authorized_keys

Partant de là, on peut se passer de *adb* et se connecter directement en SSH sur
le téléphone avec l'utilisateur phablet. Comme par défaut sur Ubuntu, le compte
root est désactivé et l'utilisateur phablet doit utiliser *sudo* pour obtenir
les super-pouvoirs. Ces pouvoirs ne permettent pas de modifier un fichier du
système qui est en dehors du répertoire */home/phablet* car par sécurité les
partitions sont montées en lecture seule. Donc on sera souvent amené à remonter
la partition en lecture-écriture avec la commande suivante :

    sudo mount /dev/loop0 / -o remount,rw

On va configurer la synchronisation de nos contacts et du calendrier vers
Owncloud par les protocoles de sychronisation **cardav** et **caldav** en
s'inspirant de [cette
discussion](http://askubuntu.com/questions/360466/ubuntu-touch-officially-launched-version-how-to-sync-contacts)
sur AskUbuntu. D'abord on configure syncevolution :

``` shell
# les valeurs username, password et syncurl doivent être adaptées
syncevolution --keyring=no --configure --template webdav username=yax password=??? syncurl="mycloud.madyanne.fr" target-config@owncloud
syncevolution --configure --template SyncEvolution_Client sync=none syncURL=local://@owncloud username= password= peerIsClient=1 owncloud

# on configure la synchro des contacts
syncevolution --configure database=https://mycloud.madyanne.fr/remote.php/carddav/addressbooks/yax/contacts backend=carddav target-config@owncloud contacts
syncevolution --configure sync=two-way backend=contacts database="Personnel" owncloud contacts

# on configure la synchro du calendrier
syncevolution --configure database=https://mycloud.madyanne.fr/remote.php/caldav/calendars/yax/personnel backend=caldav target-config@owncloud calendar
syncevolution --configure sync=two-way backend=events database="Personnel" owncloud calendar

# on lance une 1ère synchro qui donne priorité au serveur Owncloud
syncevolution --sync slow owncloud contacts
syncevolution --sync slow owncloud calendar
```

Ce qui manque juste, c'est une
synchronisation périodique avec Owncloud par exemple une fois par heure.
D'abord j'ai naïvement ajouté deux lignes dans la CRONTAB :

    syncevolution owncloud contacts
    syncevolution owncloud calendar

Et bien ça ne marche pas car syncevolution utilise DBUS et qu'en lançant hors
shell utilisateur, les variables d'environnement *DISPLAY* et
*DBUS_SESSION_BUS_ADDRESS* ne sont pas initialisées. Il faut donc récupérer ces
valeurs dans le shell script qu'on va lancer en CRON, merci
[Alexandre](http://askubuntu.com/questions/611761/syncevolution-in-cronjob-to-sync-the-ubuntu-phone-via-caldav-arddav).
Donc finalement c'est ce script qu'on va mettre sous CRON :

``` shell
export DISPLAY=:0.0
export DBUS_SESSION_BUS_ADDRESS=$(ps -u phablet e | grep -Eo 'dbus-daemon.*address=unix:abstract=/tmp/dbus-[A-Za-z0-9]{10}' | tail -c35)
syncevolution owncloud contacts
syncevolution owncloud calendar
```

Amusant non ? J'ai joué pas mal avec la synchronisation des calendriers et des
contacts et je peux dire que *syncevolution* tient bien la route. Le dernier
détail indispensable pour moi, c'était de récupérer ma sonnerie habituelle ; il
n'y a pas encore la possibilité de télécharger une sonnerie personnalisée.
Après le chantier de la synchronisation, c'est un jeu d'enfant : il suffit de
la convertir au format OGG et de la placer dans le répertoire
*/usr/share/sounds/ubuntu/ringtones/*.

Après une semaine d'utilisation quotidienne, j'ai trouvé le système crédible et
agréable à utiliser. Qu'ils rajoutent un clavier physique et ce sera le
meilleur du monde (troll inside !). Ubuntu Touch s'améliore régulièrement. Les
développeurs se sont imposés un rythme de 6 semaines pour livrer une OTA.
L'inconnue pour moi c'est comment Canonical espère monétiser son système et
combien de temps ils réussiront à le pousser sans que ce soit rentable. En tout
cas techniquement, c'est un petit bijou qui fait du pied aux Unixiens, un bol
d'air frais quand les systèmes alternatifs au couple Android / IOS jettent
l'éponge ou déposent le bilan l'un après l'autre.
