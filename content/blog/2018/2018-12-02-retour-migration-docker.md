---
layout: post
title: Retour sur la migration vers Docker
categories: Containers Hébergement
tag: planet
---

Ce ne sera pas un scoop car j'ai distillé l'information à travers mes derniers articles : j'ai transformé mon serveur de virtualisation en serveur de containers Docker<!-- more --> depuis quelques mois. C'est l'occasion de faire un bilan en listant ce qui a bien fonctionné mais aussi ce qui a posé problème, et les avantages et inconvénients d'un serveur de containers. Au préalable, je n'utilise pas Docker dans un contexte professionnel mais pour héberger mes services personnels.

Docker n'est pas une lubie... je suis ses avancées depuis plus de trois ans. Il a eu sa période très instable où le choix de la distribution et surtout du kernel étaient primordiaux, puis celle où la sécurité était discutable. Mais aujourd'hui il est difficile de trouver des arguments pour ne pas au moins l'essayer. Docker est une vague de fond qui a déjà conquis les grandes entreprises et les développeurs. Ces derniers maintiennent de plus en plus souvent une version Docker de leurs logiciels en plus (mais jusqu'à quand ?) des paquets pour telle ou telle distribution. [J'ai déjà abordé le sujet](https://blogduyax.madyanne.fr/2018/quel-systeme-serveur/) : pour moi Docker, c'est la fin de la distribution serveur à court terme comme [flatpak et consorts](https://fr.wikipedia.org/wiki/Flatpak) annoncent la fin de la distribution bureau à moyen terme.

On entend souvent : 

    Docker n'a rien inventé, les containers existaient déjà !

Oui c'est vrai, on avait déjà chroot, LXC, OpenVz, les jails. D'ailleurs Docker s'est appuyé sur LXC dans ses premières versions. Mais ça, c'est la plomberie du sous-sol. C'est nécessaire et ça doit être performant mais ça ne résume pas Docker et ça n'explique pas son succès qui, pour moi, a 3 raisons principales : 

1. l'abstraction (partielle) au système d'exploitation, ce qui donne accès à Docker à un autre public que des ingénieurs système
2. un langage de description *Dockerfile* / *docker-compose.yml* facile d'apprentissage 
3. et, surtout, un écosystème communautaire : je parle bien sûr du marché au containers : [le Hub](https://hub.docker.com/)

Si je fais un parallèle rapide avec le langage Java, Maven a beaucoup concouru à son succès en donnant accès à toutes les librairies tierces Open Source. Et bien c'est exactement ce que fait Docker avec le hub : récupérer une image pour l'enrichir et fabriquer la sienne. 

On est en plein dans l'essence même de l'Open Source, le partage. Il faut toutefois prendre des précautions : 

- priviligier une image officielle d'un logiciel
- ne pas se dispenser de lire son Dockerfile pour voir comment elle est construite et sur quelles couches elle s'appuie

En fait, ce sont les mêmes réflexes qu'avec l'intégration d'une librairie inconnue à son programme. Cela explique aussi l'engouement des développeurs pour Docker et on peut faire plein de parallèles avec le développement. J'ai passé du temps à pratiquer et j'ai pris de la compétence progressivement. Je pense avoir atteint le 2ème dan, selon ma vision de la courbe d'apprentissage de Docker : 

- **1er dan** : docker file : écriture, réutilisation, exposition / attachement de ports, utilisation des volumes, publication dans une registry
- **2ème dan** : docker compose : composition de containers, communication intra-container, compréhension du cycle de vie des images et des containers
- **3ème dan** : orchestration, supervision, sécurité avancée : Kubernetes, Docker Swarm, audits de sécurité

Ma prochaine étape est d'effleurer le 3ème dan avec Swarm. Faute de ressources matérielles suffisantes, je ne me formerai probablement pas à Kubernetes dans la sphère personnelle.  

Pour progresser, j'ai déployé au plus vite pour me confronter en situation réelle. A l'époque, mon serveur fonctionnait avec des containers LXC dans Proxmox. Il a donc été aisé de migrer des bouts vers Docker sans faire la bascule d'un coup. De plus, j'avais le pare-feu de Proxmox et mes containers s'exécutaient dans une marchine virtuelle KVM ; cela m'a permis de me concentrer sur la création des images et des containers et retarder l'apprentissage de la sécurisation. 

Une bonne partie des containers font tourner des projets persos écrits en Python. j'ai donc naturellement créé une image commune pour les applications Python. Par paresse et comme je ne suis pas dans un contexte professionnel, j'ai réutilisé la même image pour plusieurs containers / applications en connectant un volume avec les sources Python dessus. Dans un contexte professionnel, j'aurais créé une image versionnée pour chaque application embarquant les sources. J'ai publié mes [quelques images sur le Hub](https://hub.docker.com/u/kianby/) et les sources sont [sur mon GitHub](https://github.com/kianby/docker) 

J'ai basé mon démarrage sur un simple fichier docker-compose qui décrit tous mes containers et une commande *docker-compose up* pour tout démarrer. Quand je me suis senti à l'aise et capable de sécuriser correctement Docker, [j'ai réinstallé le serveur de zéro avec une Debian et Docker](https://blogduyax.madyanne.fr/2018/installation-dun-serveur-de-containers/) pour en faire un serveur de containers bare metal. 

Pour la supervision, je suis resté simple en installant [Portainer](https://www.portainer.io/) pour redémarrer les containers, voir les logs... et [Glances](https://nicolargo.github.io/glances/) pour avoir une vision détaillés de l'usage des ressources. Les 2 outils sont s'exécutent eux-même dans des containers. 

Voilà j'en suis à 18 containers déployés avec 30% des 4 Go de RAM du serveur utilisé. Les performances sont très proches d'une installation monolithique. Docker demande un peu plus de RAM car même si les images sont légères on duplique des OS légers. En tout cas, on est très au dessus des performances de la virtualisation.

Le plus gros bénéfice de ma migration est un environnement de test identique, le truc que je n'ai jamais pu avoir auparavant. Pour cela, j'ai souscrit un nom de domaine .space à 0,99 centimes (merci les promos) et j'ai décliné la configuration de mon environnement sur ce domaine. Résultat, j'ai un environnement complet qui tourne sur mon PC de développement : très appréciable quand la moitié des containers exécutent du code écrit par soi-même et quand on veut tester des nouveaux containers avant de les mettre en production. Autre avantage, la sauvegarde en un tour de main : une arborescence de données, quelques volumes Docker.

Ce qui a moins bien marché, c'est le 1er démarrage de mes containers Python dépendants les uns des autres et habitués à avoir les services dépendants opérationnels. Dans Compose, on ne définit ~~pas~~ plus d'ordre de démarrage. le cycle de vie des containers est aussi plus volatile : une modification de *docker-compose* recrée juste les containers impactés. On a donc plus souvent des containers détruits / recréés. C'est donc une bonne approche d'avoir du code orienté micro-services, capable de : 

- gérer la non disponibilité d'un service en fournissant un service dégradé
- stocker localement les données reçues pour les traiter quand l'ensemble du système redevient opérationnel

J'ai donc revu le code de certains de mes projets pour leur ajouter une base de donnée locale SQLite et gérer le dynamisme de l'environnement. C'est positif et pas forcé par Docker ; son fonctionnement rend juste cette approche pertinente et on obtient du code plus résilient. Je suis très satisfait de cette migration et pas prêt de revenir en arrière. 

![Docker](/images/2018/docker.jpg)

**Est-ce que Docker est indétrônable ? Est-ce qu'il y aura une alternative libre ?**

Une partie de Docker est sous licence Open Source et on a des alternatives pour l'exécution de containers (comme rkt de CoreOS). L'arrivée un peu tardive de Swarm et les lacunes de ses premières versions ont permis à Kubernetes de remporter une grosse partie du marché de l'orchestration. Mais Docker a construit une communauté ces cinq dernières années et démocratisé la publication de containers au format Dockerfile, difficile d'imaginer qu'il puisse disparaitre comme ça. En  tout  cas, je pense que la mode de la containerisation a gagné le marché durablement.
