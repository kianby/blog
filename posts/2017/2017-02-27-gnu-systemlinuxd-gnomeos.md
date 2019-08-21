<!-- title: De GNU/Linux à gnuSystemlinuxdGnomeOs -->
<!-- category: GNU/Linux BSD Humeur -->

Cet article n'est pas un réquisitoire contre **systemd** mais l'argumentaire de
mon positionnement<!-- more --> qui me situe quelque part entre les deux positions
régulièrement entendues :

- systemd c'est tout pourri, la preuve regardez ce bug
- systemd c'est le progrès inévitable et en plus ça ne change rien pour l'utilisateur final

J'ai vécu en première ligne l'arrivée de systemd dans nos distributions et,
professionnellement, l'impact a été la nouvelle manière de décrire des
services. C'est simple et standard entre les distributions qui ont basculé sur
systemd soit presque l'intégralité des distributions *mainstream* en 5 ans :
Redhat / Centos / Fedora bien sûr puisque le projet est dirigé par Lennart
Poettering, un employé de Redhat, Ubuntu et... Debian qui a dérogé à sa ligne
de conduite d'intégrer des outils mâtures et stables et a misé sur systemd,
probablement trop tôt, et s'est mis en conflit avec une partie de ses
contributeurs qui ont pris la porte et démarré le projet
[Devuan](https://devuan.org/fr/). Je ne vais pas m'étendre car c'est polémique
mais il y a une pression de l'équipe systemd, depuis sa création, pour forcer
son adoption rapide par les distributions ce qui a fortement contribué à son
image de [boatware](https://fr.wikipedia.org/wiki/Bloatware) truffé de bugs.

Bon ok, mais c'est quoi le but de systemd ? Au début, je pensais que ça se
cantonnait à un nouveau système d'init plus rapide et standardisé. Après des
discussions avec mon double Linuxien à moustache et diverses lectures il
ressort que plus rapide (car systemd est parallèlisé) est un argument léger :
sur un serveur on s'en cogne, et les 1% d'utilisateurs de Linux Desktop ne
verront aucune différence avec un SSD à 30 balles. Par contre, ce parallélisme
cause un manque de prédictabilité de l'ordre de démarrage et pose des problèmes
aux gens qui font de l'embarqué avec Linux (et là on ne parle pas de 1%
d'utilisateurs mais du gigantesque marché de l'IoT et du M2M).

Bon, mais alors c'est quoi le but de systemd ? Il semble que ce soit la
fourniture d'API pour faire papa / maman afin que l'environnement de bureau
Gnome sur lequel à misé Redhat puisse devenir plus qu'un simple environnement
de bureau mais une expérience utilisateur disruptive par une intégration
poussée avec son système d'exploitation (pensez à un pingouin qui court sur une
banquise en train de se réchauffer). Bref, Gnome veut devenir le nouveau
MacOS/X pour atteindre... 2% du marché des PC de bureau... à une époque où le
PC ne se vend plus. Bon j'ironise mais je comprends l'objectif de l'équipe
Gnome qui a envie de passer à la vitesse supérieure et qui est le seul DE en
position de le faire aujourd'hui. Donc cette élaboration d'une API standard
entre les distributions serait la justification aux modules engrangés par
systemd: gérer les points de montage, remplacer CRON, résoudre le DNS [avec
brio](https://www.blog-libre.org/2017/04/20/essuyer-les-platres-dns-sur-ubuntu).

En tirant une ligne vers l'horizon et en fermant un oeil, on voit la finalité :
Linux, Systemd, Wayland, Gnome => un Linux Desktop OS avec un niveau de
finition et une accessibilité au même niveau qu'un Mac OS/X, un Windows 10 ou
un Android.  Avec le soutien de Redhat, je ne doute pas qu'ils vont réussir :
systemd va se stabiliser et se fiabiliser. Pour quel marché, c'est moins
clair...

Ce qui me gêne, moi, c'est la mise en terre de la philosophie UNIX. Ca ne
semble pas parler beaucoup aux utilisateurs enthousiastes (ou résignés) de
systemd. C'est peut-être une différence de culture ou de génération. La planète
linuxienne est enthousiaste sur son système, beaucoup sont même concernés par
la liberté à travers les licenses. Moi j'ai connu UNIX avant de connaître
Linux. J'ai adoré les cours de mon vieux professeur en salopette qui les mains
dans les poches nous faisait revivre la naissance d'Internet à travers les
différents protocoles basés sur TCP/IP et le fonctionnement interne d'un
système UNIX.  J'ai connu les UNIX propriétaires (Solaris, HP/UX, AIX) et j'ai
adoré sa philosophie :

- KISS : Keep It Simple Stupid
- un outil => une tâche
- des mécanismes éprouvés pour faire travailler ces outils ensembles (comme les |)
- le format texte privilégié en toute circonstance sur le binaire

Quand Linux est arrivé, j'ai bien sûr apprécié de pouvoir installer un UNIX sur
un PC personnel mais c'est aussi le GNU et la GPL qui m'ont séduit, la notion
de partage et de retour des contributions à la communauté. J'admire le noyau
Linux pour ce qu'il est devenu en l'espace de 20 ans, en terme de performance,
de fiabilité et de support du matériel. Mais c'est juste un kernel ; ce qui
compte aussi énormément c'est la GPL et la philosophie UNIX du système complet.

Systemd est une anti-thèse à la philosophie UNIX : un init binaire, des logs
binaires, une construction théoriquement modulaire mais avec tellement de
dépendances qu'il s'impose comme indispensable, une réinvention de la roue en
permanence. Il est plausible que systemd s'invite dans le kernel Linux dans
quelque temps. Et le résultat sera sûrement appétissant à l'oeil pour le Linux
de bureau et il simplifiera la vie de certains administrateurs systèmes. Ceux qui
envient leurs collègues certifiés Microsoft apprécieront même.

Mais Linux ne sera plus un système UNIX... Et si je veux utiliser un UNIX-Like
j'ai Android, et bientôt Windows 10 vu la vitesse du rapprochement de Microsoft
avec Canonical.

Donc si je veux utiliser un système UNIX, il me reste :

- les BSD qui, paradoxalement, alors qu'ils sont issus des UNIX propriétaires, apparaîssent aujourd'hui comme les dépositaires de la foi (euh philosophie)
- quelques rares distributions GNU/Linux qui aiment UNIX (comme Gentoo ou Slackware par exemple). Non ce n'est pas de la vaine résistance. Linux ce n'est pas juste un kernel et des programmes GNU. Il y a autre chose à préserver.

J'ai donc décidé de n'utiliser plus que des systèmes qui respectent ces
critères. Ca n'empêchera pas la terre de tourner et *gnuSystemlinuxdGnomeOs* de
voir le jour et occuper sa place mais, comme pour le 7 mai prochain, c'est à
chacun de se positionner en son âme et conscience.

Moi j'ai choisi UNIX.
