<!-- title: Installation de Jenkins CI -->
<!-- category: Développement -->
<!-- tag: planet -->

![Jenkins CI](/images/06x/jenkins-logo.png#left) L'intégration
continue s'inscrit dans [la méthodologie
Agile](http://fr.wikipedia.org/wiki/M%C3%A9thode_agile) ; Son objectif est de
garantir que le projet est stable tout au long du développement et qu'on peut
livrer le projet à tout moment. <!-- more --> Cela implique que les développeurs ne publient
que des fonctionnalités ou des micro-fonctionnalités complètes (dans le sens
entièrement implémentées et utilisables) dans le dépôt de sources et qu'on
peut à tout moment construire le projet dans son intégralité et le déployer,
généralement sur des environnements de tests pour que l'Assurance Qualité
puisse tester tout au long du cycle de développement, ou bien en tant que
version intermédiaire planifiée (milestone, alpha, beta).

Ici je vais décrire l'installation du logiciel d'intégration continue [Jenkins
CI](http://jenkins-ci.org/) dans le conteneur de Servlet
[Tomcat](http://tomcat.apache.org/) sous Ubuntu Server 10.4. D'abord on installe
Tomcat 6 avec le système de paquets :

```shell
sudo apt-get install tomcat6
```

Ensuite on installe manuellement le WAR de Jenkins CI :

```shell
# move to tomcat webapps dir
cd /var/lib/tomcat6/webapps
sudo wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war
```

Si Tomcat était lancé, Jenkins va être déployé et disponible en quelques
secondes. Sinon démarrez Tomcat :

```shell
sudo /etc/init.d/tomcat6 start
```

Jenkins est accessible ici : http://nom du serveur:8080/jenkins

Par défaut la sécurité n'est pas activée et tout le monde peut accéder et
administrer Jenkins. Nous allons remédier à cela en modifiant les paramètres
de sécurité dans la partie administration qu'on accède en cliquant sur le
lien *Administrer Jenkins* (http://localhost:8080/jenkins/manage) puis *Configurer le système* (http://localhost:8080/jenkins/configure).

![Sécurité](/images/06x/jenkins-security.png)

Après enregistrement, un bouton *S'identifier* fait son apparition dans la
bannière en haut à droite. Jenkins a délégué à Tomcat la gestion des
utilisateurs, il faut donc créer, au minimum, un administrateur Jenkins. Editez
le fichier /var/lib/tomcat6/conf/tomcat-users.xml avec votre éditeur favori et
ajoutez le rôle 'admin' et un administrateur, par exemple :

```
<role rolename="admin">
<user username="jenkins" password="jenkins" roles="admin">
```

Ensuite redémarrez Tomcat pour prendre en compte la création de l'utilisateur
et identifiez-vous à Jenkins en tant qu'administrateur. Attention,
l'utilisateur anonyme a encore accès à tout. Si votre intégration continue
tourne sur un serveur publique, vous voudrez probablement que l'utilisateur
anonyme n'ait aucune visibilité sur les projets. Modifions à nouveau la
sécurité ; on choisit la sécurité basée sur une matrice de droits, et on
rajoute l'utilisateur **jenkins** avec tous les droits cochés.

![Matrice de sécurité](/images/06x/jenkins-matrix.png)

Si vous avez joué de malchance et que vous n'avez pas affecté de droit à
l'administrateur avant de sauver, vous ne pouvez plus accéder à Jenkins :-)
Heureusement les développeurs ont prévu le coup et il faut réinitialiser la
sécurité en suivant [cette procédure du Wiki](https://wiki.jenkins-
ci.org/display/JENKINS/Disable+security).

A ce stade Jenkins est opérationnel avec une sécurité basique qui suffira
dans beaucoup de cas, prêt à gérer des projets, ce qui fera l'occasion d'un
prochain article.
