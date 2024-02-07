<!-- title: Deux installations de OpenBSD -->
<!-- category: Hébergement BSD -->

Déjà un peu évoqué sur Diaspora, j'ai migré mon serveur vers OpenBSD depuis
deux mois<!-- more --> à une période où les planètes étaient alignées : j'avais du temps et
l'envie, et aussi une revanche à prendre suite à une installation ratée l'année
dernière sur mon portable. Les BSD m'intriguaient depuis longtemps, plus
spécialement OpenBSD et j'avais commencé à regarder et apprécier la qualité de
la documentation et j'avais l'image d'une petite communauté qui prend le temps
de réfléchir, de bien faire les choses sans céder aux sirènes de la mode, en
maintenant un cap : la sécurité avant tout et le KISS. Ce qui me retenait
hormis la difficulté apparente, c'était mon goût pour la GPL. Les mois ont
passé, la tournure qu'a pris Linux a commencé à me déplaire. Puis Thuban a
publié la première version de son livre sur l'auto-hébergement avec OpenBSD et
il a montré que non seulement ce n'etait pas si compliqué mais qu'on pouvait
faire tourner tous les services de l'auto hébergement. C'est un point très
important car venant d'une distribution Linux comme Debian avec ses milliers de
programmes, on peut craindre qu'OpenBSD soit pauvre et qu'il faille tout se
compiler à la mimine. En fait, la vérité est ailleurs, pardon à mi chemin :
pour une utilisation serveur, on trouve tout ce qu'il faut pour de
l'hébergement de services et plus en standard (*out of the box*) que certaines
distributions Linux pour l'administration système.

Ça a ravivé la flamme et migrer mon serveur vers OpenBSD c'etait concret en
terme d'objectif. J'héberge un certain nombre de services : lecteur de flux RSS
(Tiny Tiny RSS), gestionnaire de favoris (Shaarli), partage de fichier,
synchronisation d'agenda et de carnet d'adresse (NextCloud), lecture hors ligne
(Wallabag) et ce blog (Pelican / Stacosys). Des services classiques mais sur un
nouveau système avec des programmes différents et une administration
différente. Ma cible c'est donc [ma Dedibox chez
Online](https://www.online.net/fr/serveur-dedie/dedibox-sc) pour laquelle
OpenBSD n'est pas encore officiellement supporté mais FreeBSD est proposé, ce
qui augure du bon concernant le support du matériel. En cherchant un peu sur la
toile, quelques courageux aguerris avaient déjà expérimenté et [partagé une
méthode d'installation
manuelle](https://devnullblg.wordpress.com/2014/04/18/openbsd-installation-on-a-dedibox-sc-gen2).
Je me suis donc lancé, muni :

- des [pages man](http://man.openbsd.org/cgi-bin/man.cgi) : sur OpenBSD c'est
  beaucoup plus que de simples pages man ; très détaillées, agrémentées
  d'exemples, c'est l'essentiel de la documentation officielle.  
- du livre [Héberger son serveur avec OpenBSD](https://www.atramenta.net/books/heberger-son-serveur-avec-openbsd/562)
- de quelques retours d'expérience sur le Net.
- [du Wiki OBSD4](https://obsd4a.net/wiki)

J'ai pris mon temps pour me familiariser avec les programmes développés par
OpenBSD. C'était le principal intérêt : ne pas juste réinstaller un serveur Web
et PHP mais apprendre le système et ses programmes particuliers : le pare-feu
(pf), le serveur HTTP (httpd), le load-balancer applicatif (relayd). Sur
quelques jours, j'ai remonté un serveur avec tous mes services, sécurisé et
simpliste d'administration. Ça tourne depuis 2 mois et à part un oeil au
rapport de sécurité quotidien envoyé par le serveur dans ma boite e-mail et aux
bulletins de sécurité publiés par l'équipe OpenBSD, je n'ai plus rien fait.

C'est le week-end dernier que j'ai réalisé que les connaissances acquises
risquaient de se perdre par manque de pratique. Et puis je suis loin de tout
maîtriser, j'etais reste au chapitre de la théorie sur les mises à jour de
sécurité par exemple. Or j'ai maintenant un serveur OpenBSD en production...
Ma solution : pratiquer plus régulièrement donc installer OpenBSD sur mon
vénérable  Toshiba portege (année 2009, core 2 duo, 4go de ram, ssd de 64 Go,
écran 13''3) et conserver mon vieux portable Ldlc (année 2011, i7, 8go ram, 750
Go hdd, écran 15''6) sous Linux. Et c'est ainsi que j'ai retenté l'installation
sur le fameux Toshiba. Le plus gros écueil avec BSD c'est le support du
matériel, moins vaste que sur Linux.

Le toshi est un bon candidat avec ses composants tout Intel (carte graphique,
chipset Wi-Fi). Et pourtant les problèmes ont commencé dès l'installation avec
un gel du boot depuis la clef USB à cause de l'acpi, un standard pas toujours
correctement implémenté par les constructeurs et où la rigueur d'OpenBSD a été
bloquante. Après desactivation temporaire de l'acpi depuis le UKC (User Kernel
Configuration) j'ai pu mener l'installation jusqu'au bout.

Le démarrage se passe bien, le système est fonctionnel mais je n'ai pas de
réseau. Un message au boot suggère que le firmware du chipset n'est pas
disponible. En effet, aucun code propriétaire n'est embarqué dans OpenBSD.
Depuis un autre PC, j'ai téléchargé [le firmware
nécessaire](http://firmware.openbsd.org/firmware/6.1) et je l'ai installé avec
fw_update (lien obsolète : http://man.openbsd.org/fw_update.1). J'ai du wifi après c'est de la
configuration : l'installation de xfce (il paraît que mate est pour bientôt),
mes outils habituels (Vim, Tmux, Firefox, Thunderbird).

Dernier écueil, j'ai planté pendant l'installation de XFCE avec *pkg_add* car
le PC chauffe pas mal, à cause de son âge. Sur Linux, j'utilise des outils
comme *cpufreq* pour limiter la fréquence du processeur. J'ai cherché un
équivalent un petit moment avant de m'apercevoir que c'est en standard dans
OpenBSD et qu'il suffit de configurer le Kernel avec des directives comme
[hw.setperf par sysctl](http://man.openbsd.org/sysctl.8). Le planté en pleine
installation de paquets a corrompu la référence de pkg. Je ne pouvais plus
terminer l'installation, le système voyait des incohérences entre ce qui était
déjà installé et sa base de référence. J'ai regénéré sa référence en combinant
les outils **pkg_check** et **pkg_delete**. Ca m'a mis en confiance sur la
robustesse du système de gestion de paquets. A cette étape, j'ai un laptop sous
OpenBSD avec XFCE.

J'ai enchaîné sur les patchs de mise à jour de sécurité du kernel avec
**syspatch**, un outil récent qui permet d'appliquer des patchs binaires et de
regénérer un nouveau kernel. Je me suis rassuré en appliquant les patchs
publiés depuis la sortie de OpenBSD 6.1 sur le portable pour valider la
manipulation puis j'ai fait de même sur le serveur.

J'utilise indifféremment mes deux portables selon les jours donc je devrais
alterner régulièrement entre Linux et OpenBSD et suivre l'évolution de ces deux
mondes parallèles, à la fois très proches et très différents.
