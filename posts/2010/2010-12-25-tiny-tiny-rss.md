<!-- title: Tiny Tiny RSS -->
<!-- category: Android GNU/Linux Hébergement -->

J'ai découvert récemment une alternative à Google Reader : [Tiny Tiny
RSS](https://tt-rss.org/). <!-- more -->L'avantage par rapport à un simple client de flux
c'est d'avoir un serveur qui actualise les flux périodiquement et qui offre une
interface Web pour la consultation. J'ai pu installer facilement Tiny Tiny RSS
sur mon hébergement [O2Switch](http://www.o2switch.fr/). Basé sur PHP et MySQL
l'installation chez un hébergeur ne pose pas de souci. Le point délicat est la
synchronisation des flux. Le Wiki de Tiny Tiny propose trois solutions. Dans le
cas d'un hébergement, on ne peut généralement pas installer le daemon mais on
peut lancer le rapatriement des flux par une commande sous Cron.

Mon utilisation au quotidien alterne l'utilisation Desktop et Mobile ; par
chance un projet cousin [ttrss-reader-fork](http://code.google.com/p/ttrss-
reader-fork/) propose une application cliente pour Android qui se connecte à un
serveur Tiny Tiny RSS. C'est une application de qualité sous licence GPL dont
le développeur Nils Braden est très actif. J'ai posé un bug jeudi dernier, il
était corrigé moins de 2 jours après :-)

![Image TT-RSS](/images/04x/CAP201012251832.jpg)
