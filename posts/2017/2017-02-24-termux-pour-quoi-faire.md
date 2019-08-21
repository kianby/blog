<!-- title: Termux pour quoi faire ? -->
<!-- category: GNU/Linux Mobilité -->
<!-- tag: planet -->

Cascador m'a communiqué son engouement pour [Termux](https://termux.com) à
travers sa série d'articles [Termux sur
Android](https://www.blog-libre.org/serie/termux-sur-android).<!-- more --> En quelques
mots, Termux est un terminal pour Android qui émule un environnement Debian et
permet d'installer certains programmes à travers le gestionnaire de paquets
**apt**. Point intéressant, cela fonctionne sans avoir *rooté* son appareil
Android et le projet est plutôt actif avec des mises à jour de paquets
régulières. La série de Cascador décrit différents scénarios d'utilisation :
installer un serveur SSH, utiliser des outils console, accéder à des API
Android. 

<img src="/images/2017/termux-esynic.jpg" alt="termux" style="margin: 0px 20px;
float:left;" />J'ai bien mordu, jusqu'à me faire offrir un super clavier
bluetooth pour Noël (merci frérot).

Le risque était que le coup de coeur retombe ; qu'après avoir
bien rigolé à installer **vim** et consorts, on s'essoufle à cause des
limitations techniques (on n'a pas un vrai Linux, le matériel a des
performances limitées) ou du manque d'utilité. Et bien, après 3 mois
d'utilisation, je peux témoigner que ce n'est pas mon cas. J'ai deux cas
d'usages récurrents (en plus de faire le malin) sur ma tablette. 

Premier usage : j'ai un Linux dans la poche (enfin dans le sac à dos) qui me
permet d'accéder à mes serveurs hébergés. Termux va plus loin qu'un simple
client SSH car je peux rapatrier et transférer des fichiers, j'ai des outils de
base de Linux (curl, wget). La tablette est Wifi et je peux monter un Hotspot
Wifi avec mon téléphone donc je peux faire le pompier de n'importe où.

Seconde utilisation : j'ai installé tout ce qu'il faut pour écrire mes articles
de blog. C'était un peu prédestiné à vrai dire : ayant un blog statique dans
lequel j'écris mes articles en
[Markdown](https://daringfireball.net/projects/markdown), j'ai besoin d'outils
*console* uniquement : **vim** pour écrire et **python** pour générer le blog
en HTML. Du coup en local je peux écrire et vérifier ma production. Et avec une
connexion Internet, je publie l'article grâce à **git**.

Termux est une application publiée sur le Play Store et sur F-Droid, sous
licence GPL, qui vaut le coup d'être testée. Et en fonction de vos besoin, vous
pourriez bien y trouver un intérêt sur le long terme. 



