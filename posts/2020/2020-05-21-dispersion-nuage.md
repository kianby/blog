<!-- title: Dispersion du gros nuage -->

<!-- category: Hébergement -->

J'ai viré [Nextcloud](https://nextcloud.com), après lui avoir confié plusieurs années mes fichiers, mes contacts, mon calendrier et même mes notes. Rien de personnel comme on dit dans le milieu, il faisait correctement son job<!-- more --> : les clients PC et Android fonctionnent correctement, tout au plus je peux lui reprocher sa lenteur à chaque migration d'un serveur à l'autre quand je dois balancer mes 75 Go de données (mais ça n'arrive pas tous les jours) et sa mauvaise manie de désactiver les applications contact et calendrier à chaque mise à jour. Mais Nextcloud est fiable et le nombre d'applications valables qu'on peut lui adjoindre ne fait que croître. 

Malheureusement je n'ai jamais réussi à avoir des performances acceptables avec mes galeries de photos. J'ai essayé plusieurs choses : les réglages avancés de cache, l'application de génération des vignettes... Rien n'a réussi, c'est mou du genou et pire depuis un mobile ; impossible d'avoir des galeries fluides. Le partage d'albums étant devenu plus essentiel ces derniers temps à cause du confinement j'ai décidé de chercher une alternative. 

J'ai d'abord envisagé d'utiliser une autre application que je brancherai sur les fichiers hébergés par Nextcloud puis de fil en aiguille, le mantra UNIX **"une tâche, un outil"** s'est imposé à moi et j'ai décidé de disperser le gros nuage en plus petits en choisissant le meilleur outil, selon mes besoins et mes goûts, pour chaque tâche. 

Je me retrouve donc avec : 

- [Seafile](https://www.seafile.com) pour la gestion des fichiers dans les nuages. Le concept des librairie est déroutant au début mais très adapté au partage en multi-utilisateurs.  Les performances sont excellentes : 1h30 pour le chargement initial des 75 Go de données contre 20h pour Nextcloud à serveur et ligne Internet équivalents. L'application Android est complète, l'envoi automatique des photos du téléphone fonctionne parfaitement (n'est-ce pas ??? OK pas de troll)

- [Radicale](https://radicale.org) pour gérer le calendrier et les contacts. C'est minimaliste, en Python donc forcément bon ;-) et ça fonctionne tout seul. Tellement minimaliste qu'il n'y a pas de client Web intégré pour visualiser / éditer ses contacts ou ses tâches comme sur Nextcloud. C'est juste un serveur CalDAV / CardDAV et c'est parfait, cette gestion est réalisée depuis mon téléphone avec l'application DAVx5 et depuis mon PC avec Thunderbird.

- [Pigallery2](https://github.com/bpatrik/PiGallery2) pour visualiser et partager les photos stockées avec soin par Seafile. J'ai essayé une légion de galeries photos, la plupart incapables de gérer 70 Go de données, utilisé un temps Piwigo qui fait beaucoup trop de choses à mon goût avec des extensions non unifiées visuellement et le projet Pigallery2 en Node.JS m'a surpris par sa vélocité. Pas de pré-traitement pour créer toutes les miniatures, il s'appuie sur les fichiers originaux en lecture et gère ses données à côté, le traitement périodique de synchronisation des galeries par rapport au répertoires sur disque est automatique. Il s'appuie sur une base de donnée interne et ça tourne dans un seul container Docker.    

- [PicoCMS](http://picocms.org) et le plugin [PicoAuth](https://picoauth.github.io) pour gérer mes notes privées. J'ai beaucoup hésité entre gestionnaire de notes et Wiki. Le markdown était un pré-requis et finalement le combo PicoCMS / Seafile est parfait pour mon usage.

C'est en place depuis un bon mois à l'exception de la galerie photo découverte toute récemment, ça tourne comme une horloge. 

![SUI accueil](/images/2020/sui-homepage.png)
*ma page d'accueil avec [Sui](https://github.com/jeroenpardon/sui)*

