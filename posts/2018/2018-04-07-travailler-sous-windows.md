<!-- title: Travailler sous Windows -->
<!-- category: Humeur -->

Depuis presque une année, je suis revenu à un poste de travail professionnel
sur Ms Windows 7, pour me conformer à la politique de l'entreprise qui
m'emploie. La réadaptation a été un peu douloureuse (doux euphémisme...) après
6 années de bonheur<!-- more --> avec des distributions comme Fedora et Debian.

Le premier point qui m'a vraiment gêné c'est l'installation de logiciels :

- trop de sources pour installer un programme : le site officiel, des sites alternatifs, c'est une jungle dont les prédateurs sont le spyware et le malware.
- aucune gestion centrale des mises à jour : certains programmes installent une cochonnerie lancée au démarrage pour détecter la présence de mise à jour, d'autres le font à chaque lancement et quant à ceux qui restent, il faut deviner qu'ils ne sont pas dans leur dernière version

Dans Windows 10, une boutique d'applications a été rajoutée, néanmoins, je
doute qu'elle soit assez complète dans mon cadre d'utilisation et pour
l'instant je suis sous Windows 7. Sur les conseils éclairés de mon ami
moustachu, j'ai essayé et rapidement adopté
[Chocolatey](https://chocolatey.org), un gestionnaire de programmes très
complet, géré en ligne de commande. C'est ma source d'installation prioritaire
car je peux mettre à jour tous mes programmes en une commande. Si ce n'est pas
disponible dans Chocolatey, je me rabats sur les méthodes traditionnelles.

Le second point qui pique c'est l'absence d'un terminal digne de ce nom. La
taille des fenêtres CMD n'est toujours pas redimensionnable dynamiquement et il
n'y a pas d'onglets. Plusieurs alternatives existent, j'ai opté pour
Cmder (lien obsolète : http://cmder.net) basé sur [ConEmu](https://conemu.github.io), un peu
plus connu, qui comble ces lacunes. J'ai aussi besoin d'un shell Unix pour
certaines tâches et me connecter en SSH sur des serveurs. Après beaucoup de
recherches infructueuses, j'ai opté pour [MSYS2](https://www.msys2.org), un
terminal moderne (colorisé, gestion des onglets) qui sous le capot repose sur
[Cygwin](https://www.cygwin.com) auquel on a greffé le gestionnaire de paquets
en ligne de commande de ArchLinux, à savoir Pacman. Qui a eu l'occasion d'utiliser
l'installeur graphique de Cygwin pour ajouter ou mettre à jour des paquets
comprendra vite l'avantage d'avoir un Pacman en mode console... ce n'est pas du
tout une fantaisie de geek.

A ce stade, j'étais paré pour bosser sereinement.

J'ai installé [Clover](http://en.ejie.me) pour rajouter des onglets à
l'explorateur de fichier standard de Ms Windows, je ne voulais pas le remplacer
par une alternative mais juste ajouter ce qui lui manque. Très récemment 
j'ai installé [Keypirinha](http://keypirinha.com)
pour ~~ne plus avoir à fouiller le menu Démarrer~~ lancer les applications
rapidement. Pour le reste, mes outils n'ont pas vraiment changé : je navigue
sur la toile avec [Firefox](https://www.mozilla.org/fr/firefox), mon bloc-notes
déstructuré est [Zim](http://zim-wiki.org), je me connecte aux bases de données
avec [DBeaver](https://dbeaver.io/), je reste fidèle à
[Eclipse](https://eclipse.org) pour le développement Java et pour le reste
(JavaScript, HTML, CSS, Python, Markdown) j'ai goûté à [Visual Studio
Code](https://code.visualstudio.com), fortement inspiré du meilleur de Sublime
Text, avec une richesse et une qualité de plugins supérieure (un avis qui n'engage que
moi). Bravo à Microsoft pour cet outil, quand c'est réussi, il faut le dire.

Malgré ce changement de système de système d'exploitation, je continue à
privilégier les logiciels libres et Open Source, pas seulement par conviction
mais aussi parce que c'est du gagnant-gagnant. Et je rassure mon auditoire : je
n'ai pas sombré du côté obscur et privateur, mes serveurs restent sous Unix
ainsi que ma machine perso.