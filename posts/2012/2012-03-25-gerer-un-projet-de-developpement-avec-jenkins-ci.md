<!-- title: Gérer un projet de développement avec Jenkins CI -->
<!-- category: Développement -->
<!-- tag: planet -->

![Jenkins Logo](/images/06x/jenkins-logo.png#left) Faisant suite à
[l'article décrivant l'installation de Jenkins
CI](http://blogduyax.madyanne.fr/index.php?article63/installation-de-jenkins-
ci), nous allons voir comment gérer un projet en reprenant la configuration
déployée sous Tomcat <!-- more -->avec Ubuntu 10.04 serveur. Pour rappel, [Jenkins
CI](http://fr.wikipedia.org/wiki/Jenkins_%28informatique%29) permet de mettre en
place une intégration continue afin de traquer d'éventuelles régressions d'un
projet logiciel pendant le cycle de développement. En pratique, il sait
accéder à la plupart des gestionnaires de sources et s'interface avec la
plupart des système de build. Son rôle principal consiste à recompiler le
projet périodiquement, dérouler les tests unitaires et produire des
notifications si quelque chose va de travers.

Mon projet d'exemple est représentatif de mes activités de ces derniers mois :
le développement d'un logiciel écrit en Java qui utilise le système de build
[Apache Maven](http://fr.wikipedia.org/wiki/Apache_Maven) pour construire le
projet. D'abord il faut installer Maven

```shell
$ apt-get install maven2
```

Maven est géré nativement par Jenkins (sans l'ajout de plugin). On accède à
la configuration de l'outil Maven depuis la page d'administration globale :

![Configure Maven tool](/images/06x/configure-maven-tool.png)

A l'exécution, Jenkins cherche les données relatives à Maven dans
/usr/share/tomcat6 car il s'exécute dans le conteneur de servlet Tomcat en tant
qu'application Web. Si le projet nécessite un fichier de configuration Maven
particulier, il faut le copier dans **/usr/share/tomcat6/.m2/settings.xml** et
il faut s'assurer que l'utilisateur tomcat6 possède tous les droits sur le
répertoire.m2.

Maintenant, nous sommes prêts à créer un nouveau Projet. Les projets de type
Maven ont leur propre type de projet :

![New Project](/images/06x/new-project.png)

Peu d'informations sont nécessaires pour définir un projet de type Maven :
*    l'interaction avec le gestionnaire de sources,
*    le chemin du fichier POM.XML qui contient la description du build Maven,
*    les "goals" de compilation du projet.

Dans mon exemple, le gestionnaire de source est Subversion (SVN pour les
proches) et il est supporté en standard, de même que CVS. La liste est
restreinte mais ne paniquez pas, une quantité de plugins permettent de
supporter à peu près tout ce qui existe (Bazaar, GIT, ClearCase,
Mercurial,...). Cerise sur le gâteau la gestion des plugins n'est pas
bidouillesque. Les plugins sont supportés officiellement, listés et
installables depuis l'interface d'administration de Jenkins.

Configurer SVN pour le projet se borne à définir l'URL du projet et configurer
l'authentification.

![Configure SVN](/images/06x/configure-repository.png)

Une section Maven définit les "goals" à exécuter et le chemin du fichier de
build POM.XML. Les "goals" 'clean' 'install' sont les cibles classiques pour
nettoyer puis reconstruire tout le projet.

![Maven Goals](/images/06x/maven-goals.png)

Le build peut être déclenché de plusieurs manières: manuellement ou
automatiquement. Dans ce dernier cas, ce peut être sur changement des sources
dans le gestionnaire de sources, indirectement dans le cas de multi-projets
ayant des dépendances (où l'on recompile le projet B chaque fois que le projet
A est construit). Il y a d'autres cas plus spécifiques, voire très
particuliers :-) gérés par des plugins.

Dans notre exemple je reste simple et je définis un déclenchement de build du
projet sur modification du gestionnaire de source. De manière similaire à
l'outil CRON, on peut définir le mot-clef '@hourly' qui signifie qu'une fois
par heure Jenkins regarde si quelque chose à changé sur SVN (c'est à dire si
un développeur a publié du nouveau code).

![Trigger Build](/images/06x/trigger-build.png)

Dans le cas de mon projet dont la compilation prend une vingtaine de minutes
c'est une valeur sensée. Quand l'intégration continue est présentée aux
développeurs, il prennent rapidement leur marque par rapport au fait que le
projet est vérifié chaque début d'heure et ils évitent quelques pièges :

*    morceler des 'commits' qui ne compilent pas (ce qui est une mauvaise pratique en
soi) et pire, publier un peu avant l'heure entière ce qui augmente le risque de
casser le build de l'intégration continue pendant la prochaine heure,
*    publier en fin d'heure, ce qui limite les chances de rattraper le coup en cas de
problème inattendu.

Le dernier point restant à voir pour boucler l'exemple, c'est la notification
des développeurs quand l'intégration continue échoue. Là aussi on peut
élaborer un système complexe, toute une catégorie de plugins existe pour
s'interfacer avec des systèmes existants (SCM, Messengers) ou rester basique et
envoyer une notification par email.

![Notification](/images/06x/notify-build-errors.png)

Jenkins CI conserve un certain nombre de builds et il affiche une météo du
build en fonction de la stabilité des derniers résultats. En cas d'erreur, il
envoie les parties pertinentes. Si cela ne suffit pas à identifier la cause de
l'erreur, toutes les traces de console sont conservées et attachées à chaques
build.

Jenkins CI peut être mis en œuvre en moins d'une journée sur un projet simple
et ainsi apporter les bénéfices d'une intégration continue à une équipe de
développeurs et de testeurs. Mais l'outil est d'une telle richesse qu'il peut
apporter beaucoup plus :

*    support de projets complexes par une architecture maître/esclave pour
déléguer la construction de sous-parties du projet,
*    support de langages / systèmes de builds / gestionnaires de sources très
étendu,
*    déclenchement de tâches post-build pour générer des rapports (analyse de la
qualité du code, couverture du code par des tests), déployer les versions
produites automatiquement.

Né du fork de Hudson l'année dernière (suite à un différent avec Oracle),
Jenkins CI est un projet open source (sous licence MIT) en plein essor, ce que
confirme le rythme régulier des sorties et l'activité de son forum.
