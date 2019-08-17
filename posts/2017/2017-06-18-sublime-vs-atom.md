<!-- title: Sublime Text vs Atom -->
<!-- category: Développement -->
<!-- tag: planet -->

Je suis un utilisateur intermédiaire de VIM. Je connais les commandes de base
et certaines plus avancées, j'utilise quelques plug-ins<!-- more --> et je suis friand des
articles du style *"10 tips for VIM power users"*. J'installe Vim sur tous mes
systèmes et c'est mon éditeur favori en mode console, généralement pour des
connexions distantes SSH sur des serveurs. Pour progresser plus, et *level-up
comme disent les jeunes*, il faudrait pratiquer quotidiennement et l'utiliser
comme IDE, ce qu'il peut être pour les langages du Web et beaucoup d'autres.
Mais je ne suis pas aussi engagé et j'aime bien utiliser un éditeur de texte
avancé plus classique (comprenez avec pilotage à la souris, des onglets et une
barre de menu), en complément de Eclipse, mon IDE pour Java. Depuis quelques
années, cet éditeur c'est [Sublime Text](https://www.sublimetext.com) dans sa
version 3 et je n'ai rien à redire. Sublime est élégant, performant et il a
amené des fonctionnalités puissantes, qu'on peut retrouver dans VIM avec les
bons plugins, mais dans un éditeur graphique et convivial : l'extensibilité des
fonctions (plug-ins), des thèmes, la minimap sur la droite de l'éditeur, la
fonction *goto anything*. 

Ceci dit, je regarde ce qui sort regulièrement, et depuis 2 ans, je teste
régulièrement [Atom](https://atom.io), l'éditeur conçu par GitHub. Ce qui me
plait dans Atom, c'est que l'équipe GitHub a développé l'outil pour le
développement dont ils avaient besoin, en s'inspirant du meilleur de ce qui
existe (et beaucoup de Sublime) tout en essayant de faire mieux. Présenté comme
un *Hackable Editor* c'est sur ce terrain qu'il montre sa grande force, son
extensibilité. Mon test de la mouture du moment, montre des nets progrès de la
stabilité et des performances.

Caractéristques de **Sublime Text** :

- développé par Jon Skinner, licence propriétaire
- multiplateforme : Ms Win, Mac OS/X, Linux
- code natif C++ et Python
- extensions en Python, fédérées par Will Bond sur [Package Control](https://packagecontrol.io)
- +4000 paquets : la plupart sous licences open source
- versioning : création 2008, sublime 2 puis Sublime 3, officiellement en bêta *stable* depuis janvier 2013
- prix : autour de 70$

Caractéristiques d'**Atom** :

- développé par GitHub, licence MIT
- multiplateforme : Ms Win, Mac OS/X, Linux
- plateforme Web Electron (basée sur Chromium et NodeJS)
- codé en CoffeScript, un langage qui se transcompile en JavaScript
- étendu par des plug-ins en Node.js et ouverture JavaScript vers C++ pour s'interfacer avec des produits tiers
- +6000 paquets : la plupart sous licences open source
- versioning : création 2014, v 1.17.2

L'empreinte mémoire est à l'avantage de Sublime, moins de -100 Mo au démarrage.
Atom ne peut pas rivaliser sur ce plan avec son architecture Web basée sur
Electron. Si votre utilisation consiste à charger des fichiers de dizaines de
milliers de lignes (épluchage de logs par exemple), choisissez Sublime ou Vim
car Atom sera lent. Par contre, si vous cherchez un éditeur multi-langages pour
écrire du Python, du Ruby, du JavaScript, du CSS, de l'HTML, Atom est une
alternative sérieuse. Son éco-système grossit très vite : +6000 plug-ins. Basé
sur Electron, il est *Web* lui-même et on peut exécuter / déboguer du
JavaScript depuis l'éditeur.

En conclusion, Sublime est plus généraliste et plus performant pour gérer des
fichiers volumineux. Atom est plus versatile et la croissance du nombre de
plug-ins montre l'engouement des développeurs Web. J'ai une licence Sublime
mais j'ai fait la bascule sur Atom depuis quelques semaines pour tout ce qui
est développement (JAVA mis à part).

