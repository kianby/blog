<!-- title: Piwik, une alternative à Google Analytics -->
<!-- category: Hébergement -->

[Piwik](http://piwik.org) est une alternative crédible sous licence GPL à
Google Analytics. <!-- more -->Cerise sur le gateau, il requiert [LAMP](https://fr.wikipedia.org/wiki/LAMP) ce qui permet de l'héberger sans effort sur la même
machine que  WordPress et il s'inscrit parfaitement dans ma démarche de
contrôler l'accès à mes données. Le projet est  jeune et actif, une version
majeure 0.8 est sortie cette semaine et la version 1.0  est [planifiée en
détail](http://dev.piwik.org/trac/wiki/Piwik-Vision-Roadmap) pour le deuxième
semestre.

L'installation prend vraiment 5 minutes. On extrait l'archive à l'endroit
souhaité de son *public HTML* (/var/www pour Apache 2 sous Debian) et on se
connecte à son URL. Un installeur pas à pas va créer la base de donnée
nécessaire et recueillir en quelques écrans les informations nécessaires sur
le site à surveiller. En finalité on a quelques lignes de JSP à insérer dans
son site. Il faut un endroit stratégique ;-) partagé par toutes pages. Pour
WordPress ce sera dans le fichier footer.php sous wp-content (c'est très bien
décrit dans la documentation). Piwik est traduit en plusieurs langues dont le
français, ce qui a son importance.

A l'usage on retrouve un tableau de bord personnalisable avec des widgets pour
afficher les statistiques des visites (nombre, provenance géographique,
navigateur utilisé). Il y a tellement de possibilités que je n'ai pas encore
tout exploré. On peut créer des rapports de synthèse et depuis la version 0.8
exporter en PDF. De l'utilisation personnelle et simpliste que j'en ai, on peut
aller beaucoup plus loin dans le cadre d'une utilisation professionnelle où on
doit fournir du reporting multi-sites régulièrement.

![Piwik](/images/02x/piwik.jpg#center)
