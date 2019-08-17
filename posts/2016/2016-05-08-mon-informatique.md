<!-- title: Mon informatique personnelle -->
<!-- category: Hébergement -->
<!-- tag: planet -->

C'est une période de réflexion et de mise en ordre de mon informatique
personnelle.<!-- more --> Après un hiver rigolo à changer de distribution toutes les deux
semaines sur mon fidèle portable, l'occasion de découvrir quelques distributions
peu connues et sympathiques comme la [NuTyX](http://nutyx.org), de faire mon
test annuel de BSD et en conclure que ce n'est pas (encore) pour moi ou que je
n'aime toujours pas KDE, avant de revenir à ma distribution de départ : une
Debian Jessie avec Mate Desktop, l'environnement de bureau qui progressivement
uniformise l'ensemble de mes machines. J'ai longtemps utilisé XFCE, que
j'apprécie toujours, mais je trouve un charme *old school* inimitable à Mate
Desktop qui me rappelle ma jeunesse ;-) Fini donc le yoyo des distributions pour
quelques temps, il est temps de se servir de sa bécane au lieu de la
réinstaller.

Le sujet de réflexion du moment, c'est **la sécurité des données**. C'est loin
d'être une obsession pour moi  mais il y a un minimum à faire pour ne pas se
trouver démuni quand le pépin arrivera (et il arrivera forcément). J'ai donc
recensé mes données sensibles et importantes. Je me rends compte que je
trimballe pas mal de données sensibles sur mon portable, notamment ma base de
données [KeepassX](https://www.keepassx.org) qui conserve mes identifiants de la
quantité de sites Web que je fréquente. Mon portable fait des sauvegardes vers
la seule machine fixe de la maison, un iMac de 2007 (pas de troll merci) et je
fais régulièrement un clone de cette machine sur un disque dur externe. L'iMac
conserve aussi les photos familiales, on arrive à 60 Go de photos. Ce sont les
données importantes à ne surtout pas perdre. J'ai donc une sauvegarde de tout ça
en local mais pas de sauvegarde sur un autre site. En cas de gros pépin
(cambriolage, incendie), j'ai tout faux :-(

Pour protéger mes données sensibles en déplacement, j'ai opté pour le
chiffrement du disque dur à la réinstallation de ma Debian et j'ai mis en place
des certificats Let's Encrypt pour mon installation d'Owncloud et mon WebMail
Roundcube.

Pour sauvegarder mes données à l'extérieur, j'ai d'abord envisagé un serveur
plus gros que celui qui héberge mon blog et mon cloud actuellement et une
solution simple basée sur Rsync. Le prix de l'espace disque m'a un peu refroidi
et je me suis intéressé aux solutions de stockage pur pour retenir Hubic qui,
sur le papier, a beaucoup d'atouts (oui ça va se gâter si vous êtes des fans OVH
qui ne supportent pas la critique de leurs idôles, sautez les paragraphes qui
suivent) :

* la réputation de l'hébergeur OVH
* un stockage sur des serveurs localisés en France    
* un stockage triplé sur trois serveurs différents
* un coût qui écrase toute concurrence : 1 euros les 100 Go par mois

J'avais testé Hubic lors de sa sortie avec l'offre de 25 Go offerts, c'était en
bêta test, il y avait beaucoup de soucis et tout a été refait techniquement
depuis, je me suis dit banco et j'ai souscrit pour une année. Dommage !     

J'ai d'abord sorti mes photos du *silo* iPhoto de MacOS pour les stocker de
manière standard : un répertoire par année, puis un répertoire combinant la date
et le nom de l'évènement. Pour cela, je remercie [Brian et sa moulinette
magique](https://github.com/BMorearty/exportiphoto). J'ai posé les photos dans
mon répertoire synchronisé avec Hubic et j'ai regardé tourner la machine une
semaine. Ca n'est pas choquant, j'ai une ligne ADSL avec un upload moyen et j'ai
limité Hubic pour ne pas utiliser toute la bande passante. En parallèle je me
suis intéressé à sortir de iPhoto en installant la gallerie Web Piwigo sur ma
vieille version de MacOs (Snow Leopard). Je passerais rapidement sur mes galères
avec le monde de la pomme : installer MacPorts pour pouvoir juste installer Git,
installer HomeBrew et virer MacPort pour éviter les conflits, trouver une
version de Xcode d'époque et finalement installer une stack MNMP (MacOS / NginX,
MySQL, PHP) opérationnelle, puis finalement Piwigo.

Ah Piwigo c'est pas mal ! De belles galeries en mode Web, une gestion des droits
utilisateurs,  une gestion de l'unicode parfaite (???) Enfin parfaite... sans
bug en tout cas, car inexistante ce qui gomme tout problème d'intéropérabilité,
les accents ne sont pas supportés dans les noms de fichiers, ni les espaces
juste le classique *A-Za-z0-9_-*. C'est probablement un choix rationnel pour une
galerie destinée à héberger des photos  sur le Web mais sur le coup ça ne m'a
pas arrangé. J'ai regardé mes photos juste synchronisées sur Hubic et j'ai
commencé une moulinette  pour détecter les caractères interdits. Rien de trop
méchant au final, 98% des fichiers sont déjà corrects,  par contre 95% des
répertoires ont des accents ou des espaces. Dans la lancée j'ai fait une
moulinette *crade* pour renommer mes répertoires. C'est là que j'ai vu la 1ère
faille d'Hubic qui a commencer à supprimer les fichiers pour repousser les mêmes
fichiers dans un répertoire avec un nom différent. En gros, chez Hubic, il n'y a
pas de somme de contrôle pour détecter qu'un fichier a juste changé de nom ou
que le répertoire a changé de nom. Pire que cela, la suppression est
désespérement longue : c'est le désavantage de la fameuse triple redondance, on
attend la confirmation de suppression des données sur les trois data centers. A
ce stade, j'ai trouvé malin de stopper le client de synchronisation, de virer
mes photos localement et de passer par l'interface Web Hubic pour supprimer les
données, pensant que ça serait plus rapide. Erreur, cela a pris environ 8
heures.

Ne me laissant pas décourager, j'ai regénéré un répertoire propre avec mes
photos bien formatées [en forkant la moulinette de
Brian](https://github.com/kianby/exportiphoto) pour rajouter une option et je
suis reparti pour une petite semaine de synchronisation avec Hubic. Ca s'est
bien passé, j'ai un serveur Piwigo local accessible par Wifi dans la maison.
Mais deux choses m'ont gratté :

* parfois le client Hubic télécharge à nouveau des photos (alors qu'il possède
  la version de référence des données)
* la taille occupée par mes données sur l'interface d'administration Hubic ne
  correspond pas à ce que je compte sur mon disque.

Du coup, je me suis mis à douter de l'intégrité de mes données. J'ai souscrit un
mois d'hébergement pour un serveur avec 100 Go de disque et j'ai installé une
Debian et le client Hubic pour Linux. J'ai commencé à rapatrier mes données sur
ce serveur. A mon grand étonnement, le téléchargement n'est guère plus plus
rapide que l'envoi, des débits entre 50 et 250 Ko/s. Le rapatriement des données
a pris 4 jours. En grand parano, j'ai fait un checksum MD5 de l'ensemble des
fichiers et j'ai comparé avec ma référence sur l'iMac. Et bien ça correspond,
Hubic fonctionne (les fans OVH, vous pouvez revenir).

Au final, je vais changer de solution de sauvegarde à cause du manque de
confiance  que j'ai acquis en deux semaines de test et des faibles performance
en téléchargement. Je m'oriente donc vers une solution classique avec un serveur
hébergé et du probablement du rsync et je cherche la perle rare dans les tarifs
que je m'impose, mais c'est une autre histoire.
