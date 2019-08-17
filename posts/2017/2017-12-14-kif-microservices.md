<!-- title: Mon kif pour les microservices -->
<!-- category: Développement -->
<!-- tag: planet -->

Je m'intéresse aux microservices depuis un bout de temps. Comme pour beaucoup
de sujets de fond, je suis à maturation lente : j'engrange les concepts, je
lis les retours d'expérience, je pèse les avantages et les inconvénients.<!-- more -->
Quand on a commencé à parler d'architecture microservices, l'engouement était
tel qu'on confrontait souvent l'architecture orientés services (SOA) et on
présentait les microservices comme la réponse adéquate pour tout type
d'application. Aujourd'hui, les esprits sont plus calmes, l'opinion commune
décrit  l'architecture à base de microservices comme une version plus
granulaire que le SOA, qui suit les mêmes principes (séparation des
responsabilités, interface de communication formalisée entre les composants)
afin d'atteindre les mêmes objectifs : maintenabilite du code, indépendance
entre le code et le déploiement (localisation, redondance).

J'espère ne pas m'attirer des foudres avec les deux paragraphes suivants.

La SOA est surtout mise en oeuvre dans le SI (système d'information) de
l'entreprise, avec des services s'exécutant sur des serveur d'applications
(bienvenue dans le monde de la JVM). La terminologie est précise (service
métier, service d'intégration, annuaire de services), des protocoles sont
préconisés et la mise en oeuvre est balisée (urbanisme, lotissement). La SOA
est mature et normalisée, elle a été pensée par des architectes logiciels
comme un ensemble de bonnes pratiques pour concevoir des applications non
monolithiques et évolutives.

A l'opposé, les microservices sont nés sur [le front
nuageux](https://fr.wikipedia.org/wiki/Cloud_computing), dans un environnement
plus dynamique (ajout à chaud d'instances de services pour supporter la
charge), très hétérogène (mix de plusieurs langages de programmation) avec des
contraintes fortes sur les temps de réponse (cas des sites de réservation ou
d'achat, réseau social). Nés un peu à l'arrache, c'est en grandissant qu'on
conceptualise progressivement leurs modèles de conception :
[http://microservices.io](http://microservices.io). Les microservices
remettent en question les façons de tester, déboguer, déployer, surveiller car
une application est constituée de très nombreux microservices, certains étant
prévus pour être répliqués afin d'absorber des pics de charges ; il ne
partagent souvent aucun socle commun (pas de serveur d'application) et ils
sont distribués sur des serveurs, des machines virtuelles ou des containers
Docker...

*"Marrant ton truc, ça rappelle un peu [la cathédrale et le bazar](https://fr.wikipedia.org/wiki/La_Cath%C3%A9drale_et_le_Bazar) non ?"*

- C'est pas faux ! D'ailleurs j'ai toujours eu un goût prononcé pour le bazar, à ne pas confondre avec le chaos. Et ce bazar fonctionne ; des grosses sociétés ont misé dessus : Facebook, Amazon, Netflix, Twitter...

Pour un développeur / architecte... Java EE (au hasard), s'intéresser aux
microservices c'est un peu comme être exfiltré du rayon condiments de
Carrefour et parachuté dans le marché aux épices d'Istanbul : un étiquetage
moins formel, pas de conditionnement normalisé mais beaucoup de couleurs et de
senteurs.

![Marché aux épices](/images/2017/epices.jpg)

Il n'est pas évident de s'y retrouver, aisé de faire des choix inappropriés
mais c'est plutôt excitant. Concrètement, on va utiliser le langage de
programmation le plus approprié pour chaque tâche (du Node.js, du Python, du
Golang ou autre), communiquer avec un modèle adapté au besoin (du RPC, de la
communication par message), choisir des protocoles adaptés à la taille des
informations échangés et aux contraintes (LAN, WAN, réseaux mobiles), fournir
une persistence locale à chaque microservice (quitte à redonder de
l'information) et surtout gérer finement le mode déconnecté (pas d'accès
réseau, inaccessibilité d'un service distant), autant que possible rendre un
service dégradé en cas de perturbation (faire mieux qu'une erreur *404 Not
Found*).

Ce projet GitHub recense les briques existantes pour construire des
microservices : [https://github.com/mfornos/awesome-
microservices](https://github.com/mfornos/awesome-microservices). Mon goût
prononcé pour Python m'a amené à jouer avec
[Nameko](https://nameko.readthedocs.io), puis à développer [un mini-
framework](https://github.com/kianby/microsvax) qui permet de communiquer par
message et RPC à travers une base mémoire [Redis](https://redis.io). Ca n'ira
jamais en production mais c'était amusant à faire. Je me suis intéressé au bus
de message ultra-rapide [NSQ](https://github.com/nsqio/nsq) écrit en Golang,
et dernièrement, je revois mon projet de service d'e-mail
[SRMail](https://github.com/kianby/srmail) dans une optique microservices.

Bref c'est un terrain de jeu illimité en connexion avec les révolutions
amenées par le développement dans les nuages, les objets connectés et le
DevOps : des domaines encore jeunes mais prometteurs qui réveillent les
~~papilles~~ neurones :-)
