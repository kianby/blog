<!-- title: Nouvelle année, nouvelle distrib -->
<!-- category: Archlinux -->

Comme j'ai toujours beaucoup de temps libre, je l'ai passé sur la planète
Linux ces dernières semaines<!-- more -->  : quelques révisions de base, des lectures de
blogs (issus de Planet Libre (lien obsolète : http://www.planet-libre.org/) en autre).

La lecture de l'excellent blog de [Frédéric
Bezier](http://frederic.bezies.free.fr/blog) et de certains articles tendance
comme " [Ubuntu which directions are you
heading?](http://www.dedoimedo.com/computers/ubuntu-direction.html) " m'ont
donné envie de m'orienter vers une "rolling release" distrib pour :

*    rajouter du fun : Ubuntu marche trop bien "out of the box"
*    mettre les mains dans le cambouis
*    vérifier sur la durée si le concept est valide : on reste à jour et on ne
réinstalle pas tous les 6 mois. Pour ce dernier point il est un peu tôt pour
répondre :-)

Ma machine est un portable Toshiba Portégé M800, core 2 Duo, chipset vidéo et
Wifi signés Intel, disque de 250 Go en dual boot avec Windows 7.

![Gentoo](https://assets.gentoo.org/tyrian/site-logo.svg)

J'ai commencé une install de Gentoo sous VirtuaBox sous
Ubuntu pendant 1/2 journée pour appréhender les concepts puis je me suis
lancé : suppression des partitions et installation grandeur nature. En 2
grosses journées j'avais un environnement Gnome fonctionnel et une grande
fierté (c'est moi qui l'ai compilé).

Ce que j'ai apprécié :

*    ça fait cliché forcément mais... c'est la force de la Gentoo : les options de
compilations fines pour mon processeur, la richesse des fameuses options USE
pour désactiver certaines fonctionalités / dépendances des paquets.
*    me traîner dans le cambouis : ça m'a permis de me remettre à jour sur la
config d'un serveur X post-an 2000 (ben oui j'avais pas fait ça depuis des
années), d'un serveur Pulse Audio, de recompiler 10 fois mon kernel pour
affiner / rajouter des options.

Ce que je n'ai pas trouvé génial :

*    là aussi c'est cliché : les temps de compilation (attends tu vas voir,
j'installes... attends reviens ça compile).
*    la fraîcheur relative des paquets : bien sûr il y a les overlays, ces extra-
repository mais ça mène souvent à des conflits.

 Je pense que la gentoo est géniale pour faire vivre une install stable
(serveur ou desktop) mais pas adaptée à un forcené comme moi qui installe un
truc nouveau tous les jours et le vire 3 jours après.

![Arch](http://www.archlinux.fr/commun/images/titlelogo.png)

J'ai donc basculé après quelques jours de Gentoo sur
Archlinux : toujours le concept de la "rolling release" qu'on n'installe qu'une
fois mais avec paquets binaires. De plus la communauté anglophone et française
semble très active.

Ce que j'ai apprécié :

*    la facilité d'installation : 1 petite journée pour installer, rapatrier mes
données, et configurer le système au poil. Tout fonctionne : virtual box,
bluetooth, dropbox...
*    la grande cohérence de l'environnement Gnome installé (j'avais eu des soucis
de polkit avec la Gentoo)
*    les gestionnaires de paquets ont des noms rigolos (pacman et yaourt) mais g
èrent-ils vraiment bien les dépendances et la cohérence du système. Et bien
pour l'instant la réponse est OUI.
*    la gestion très fine des dépendances : c'est la 1ère distrib ou j'installe
tout gnome et je peux ensuite désinstaller epiphany / evolution sans tout
casser.
*    la vitesse de démarrage : très similaire à Ubuntu.

Ce que je n'ai pas trouvé génial :

*    pour le moment je suis sous le charme :-)
