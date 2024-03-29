<!-- title: Quelle distribution 'Gnome 2' choisir en 2012 ? -->
<!-- category: Humeur -->
<!-- tag: planet -->

Le titre est un peu provoc mais c'est une vraie question [que je me posais
déjà en Novembre
dernier](http://blogduyax.madyanne.fr/index.php?article60/gnome-3-pour-un-usage-
professionnel). Comment retrouver un niveau de productivité correct après
l'ouragan Gnome 3 / Unity dans le cadre professionnel<!-- more --> avec du matos récent (en
l'occurrence un core i7 avec de la RAM à gogo et une carte NVIDIA Optimus
achetés en décembre) ? J'ai posé deux contraintes : **une stabilité des
paquets sur 1 an** (hors mise à jour de Mozilla et patchs de sécurité bien
sûr) et **une distribution proche de Debian**. Pour ces raisons j'ai écarté
Archlinux, bien ce que soit mon coup de coeur depuis 2 ans.

 ![Gnome logo](/images/06x/gnome-logo.png#right") Mon grand
espoir était d'utiliser une [Debian](http://www.debian.org/) stable, ce qui
m'aurait laissé encore 1 an de tranquillité sous Gnome 2. Mais j'ai déchanté
! Après installation à partir des beaux DVD "Squeeze" récemment reçus j'ai
réalisé que la version stable embarque un kernel 2.6.32, trop ancien pour
gérer le chipset Wifi et que les versions de Mozilla sont vraiment anciennes.
Les [backports officiels](http://backports-master.debian.org/) n'ont pas aidé
à résoudre ces points. La perspective de *tweaker* manuellement la
distribution m'a effleuré. J'ai plutôt modifié les dépôts pour passer en
Testing. Ce que j'ai gagné c'est le passage à Gnome 3 et une gestion du Wifi
boiteuse. De plus Testing évolue continuellement. L'objectif initial n'étant
pas de passer à une pseudo-rolling release, j'ai quitté Debian avec quelques
regrets.

Sur le coup, mon raisonnement fut "tant qu'à faire une croix sur Gnome 2,
autant installer une distribution récente". Ce fut donc Ubuntu 11.10 avec Unity
ou Gnome 3. Bon Gnome 3 je connais, je l'ai utilisé presque 1 an à la maison.
C'est mignon, bien pensé mais pas adapté à mon usage où je papillonne toute
la journée parmi une vingtaine d'applications lancées. Du coup, j'ai donné sa
chance à Unity et j'ai tenu 2 semaines :-) Mais le bilan n'est pas si négatif.
J'ai beaucoup apprécié l'espace gagné sur l'écran grâce à la barre de menu
unique (comme dans le monde des pommes). Ce qui me déplait fortement c'est la
difficulté à trouver une application dans le panel. Quelle idée marketing
tordue de mixer les applications installées et celles disponibles dans l'Ubuntu
store!!! On peut contourner le problème en rajoutant le [Classic Menu
Indicator](http://www.webupd8.org/2011/06/use-classic-menu-in-unity-
classicmenu.html) mais le problème de basculement parmi une vingtaine
d'applications lancées reste entier.

Las j'ai transformé mon Ubuntu en Xubuntu. Ce que je peux dire sur XFCE a été
lu ou dit ailleurs : avec des efforts de personnalisation on arrive à recréer
un Gnome 2-like (en moins beau, moins bien intégré). On a une vraie barre des
tâches qui peut regrouper intelligemment les applications lancées et le menu
n'est pas une porte ouverte sur une boutique d'applications. Par contre le
gestionnaire de fichier Thunar est moins bien que Nautilus (notamment il manque
la gestion des onglets) et **on a le goût amer d'avoir quelque chose de presque
aussi bien qu'en... 2010** ;-) L'année 2010 c'est Ubuntu 10.04 juste avant que
Canonical n'entame le grand chantier Unity et que l'équipe Gnome ne démarre sa
révolution pour ouvrir Gnome aux tablettes et aux netbooks (en oubliant les
gens qui utilisent leur machine pour travailler). Bref 2010 c'est l'avant
dernière version "Gnome 2" sortie par Canonical dans [une version LTS maintenue
jusqu'en avril 2013](http://doc.ubuntu-fr.org/lucid). D'un coup il y a eu
déclic ! Serait-il possible que cette version avec un support étendu soit
capable de gérer mon matériel acheté en fin d'année 2011 ?

Et bien la réponse est positive, avec quelques ajustements mineurs :

*    l'activation des dépôts officiels "lucid-backports" et "lucid-proposed" pour
passer au plus récent kernel proposé en 2.6.x, à savoir le 2.6.38-13 (si
nécessaire on peut aller jusqu'au 3.0.0-15) et bénéficier de Firefox 9.
*    l'ajout du dépôt Ubuntuzilla pour bénéficier de Thunderbird 9 car la version
3.x fournie par défaut ne propose pas l'extension Lightning.
*    La désactivation du driver Nouveau (encore expérimental en 10.04) -
blacklisté dans /etc/modprobe.d/blacklist.conf - l'utilisation de la carte
Intel est bien suffisante pour mon usage.

Tous les outils que j'utilise quotidiennement pour le travail fonctionnent
parfaitement (Eclipse, JAVA, VMWare Player, Skype), l'environnement de bureau
est un bonheur retrouvé. Pour info, Ubuntu 10.04 démarre et s'arrête 2 fois
plus vite qu'une version 11.10. Que fait Canonical depuis 3 versions ? - ah oui
ils focalisent sur l'environnement de bureau :-( Après un mois d'errements,
j'ai enfin l'impression d'avoir la distribution qu'il me faut pour cette
machine. J'aurais pu intituler cet article "Retour vers le futur".
