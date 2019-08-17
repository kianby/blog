---
layout: post
title: Histoire d'hébergement
category: Hébergement
tag: planet
---

Dans la continuité de [mon article
précédent](http://blogduyax.madyanne.fr/mon-informatique-personnelle.html) je
continue à mettre de l'ordre dans mon informatique.<!-- more --> Après le renoncement de
confier à Hubic mes 70 Go de photos familiales j'ai recherché une solution
classique : un hébergement de serveur avec suffisamment d'espace disque qui
puisse à la fois accueillir mes photos (synchronisées en *rsync*) et mes
services (blog, cloud) pour ne pas exploser ma facture d'hébergement.

L'hébergement c'est une belle jungle avec :

* des poids lourds : quelques gros hébergeurs qui possèdent leur infrastructure
  système et réseau (OVH et Online par exemple).
* des grossistes : des hébergeurs qui louent en volume chez les gros hébergeurs
  et qui façonnent des offres commerciales un peu différentes, un peu
  l'équivalent des MVNO dans le domaine de la téléphonie
* des petits hébergeurs qui possèdent leur propre infra et essaient de tirer
  leur épingle du jeu avec des offres différentes (techniquement ou commercialement)    

Tout d'abord il n'y a pas d'hébergeur miracle qui possède la meilleure offre du
marché. En fonction  du type d'hébergement (serveur physique ou virtuel) et de
la gamme, on va trouver des offres plus intéressantes  chez l'un ou chez
l'autre.

Moi je cherchais un serveur virtuel VPS (pour sa flexibilité et son faible taux
de pannel) avec une  assurance de sauvegarde des données (snapshot ou espace
FTP) pour rapidement tout restaurer en cas de panne. J'ai écarté les
grossistes, ça ne m'intéresse pas d'avoir un hébergeur qui dépend d'un autre
pour résoudre les incidents techniques. J'ai d'abord exploré  le monde des
petits hébergeurs où on trouve quelques perles (des hébergeurs à fond sur le
Green IT) et des gens qui ne tiennent pas la route malgré un site Web
alléchant.

Après deux expériences foireuses chez des petits hébergeurs, j'ai failli opter
pour une Dedibox de Online : du serveur physique à un prix plancher ; le pendant
chez OVH est la gamme Kimsufi. Du serveur physique, pas très cher donc, mais
avec souvent un service minimum (pas de RAID, pas de sauvegarde). Dedibox
propose 100 Go de FTP et ça me semblait pas mal, sans surprise. je connais
l'offre à titre professionnel : le taux de dispo est impressionnant et la bande
passante très bonne. Seul hic, c'est un peu en dessus de mon buget de 9 euros HT
par rapport aux 8 euros TTC d'aujourd'hui chez FirstHeberg. Par contre, avec une
Dedibox j'avais un gros disque de 1 To.    

J'allais me lancer quand j'ai aperçu les offres Scaleway sur le site Online.
C'est quoi [Scaleway](https://www.scaleway.com) ? C'est une filiale de Online
avec un positionnement **Cloud**. Le problème du terme Cloud, c'est qu'on l'a
tellement usé et absusé (hein les marketeux) qu'on ne sait plus de quoi on parle
là. Scaleway se positionne sur le créneau de Amazon AWS et de Google App Engine
avec une offre tarifée à l'heure qui permet de faire du pilotage / de
l'orchestration pour par exemple automatiser des déploiements de nouveaux
serveurs dans le cadre d'une intégration continue d'un logiciel en cours de
développement, ou démarrer une grappe de serveurs supplémentaire pour absorber
une charge Web dans le cas d'un architecture balancée. Pour cela, ils proposent
des API et un matériel original puisqu'il s'agit d'un serveur physique peu
performant basé sur une architecture ARM. Je parle ici du serveur C1, leur
premier modèle. L'offre est originale car ce genre d'orchestration se fait
généralement sur du virtuel pour sa souplesse  à stopper, démarrer, reconfigurer
des VMs et eux proposent un micro serveur qui ne consomme pas grand chose avec
l'argument que sur du physique il n'y a pas d'inconnu sur la performance comparé
au virtuel où votre voisin (que vous ne connaissez pas) a mangé la CPU de
l'hyperviseur. C'est donc un peu comme si on avait un Raspberry chez un
hébergeur avec une grosse bande passante. Ils arrivent à mettre plus de 900
serveurs dans un rack 1U. Le côté *green IT* m'a séduit.

Et l'espace disque ? C'est l'autre grosse particularité de l'offre. L'espace
disque est attribué par tranche de 50 Go (1 euros la tranche) et géré
dynamiquement puisque la vocation du Scaleway est d'offir la même souplesse que
les VPS : stopper, déplacer, redéployer... Donc en fait, les données sont
centralisées (dans un gros NAS). Et au démarrage d'un serveur,
elles sont rapatriées pour être attachées au boot. Quand le serveur est stoppé,
elles sont réécrites dans le central. Pour quelques centimes, on peut conserver
un snapshot de notre disque.   

Ce qui m'a plus dans cette offre ce sont les points suivants :

* un hébergement physique
* la flexibilité de rajouter ou d'enlever des volumes disques
* une architecture ARM : performances modestes faible consommation électrique

Est-ce que c'est une offre adaptée à un hébergement classique ? Clairement, ce
n'est pas la cible et le Scaleway n'a pas été conçu pour héberger un blog et
quelques services Cloud mais il peut le faire avec un bémol sur l'arrêt /
relance du serveur : le temps de rapatriement des données vers l'espace central
est très long. Surtout qu'aux 50 Go de base, j'ai souscrit un volume
supplémentaire de 100 Go pour stocker mes fameuses photos. J'ai tout stoppé pour
réaliser un snapshot du disque système (pas de snapshot à chaud) mais on ne
stoppe pas un serveur régulièrement donc c'est gérable. Autre point à prendre en
considération : l'architecture ARM est supportée par peu de distributions. Sans
surprise, j'ai choisi Debian. Tout ajout de logiciel qui ne ferait pas partie du
système de paquets nécessite une compilation pour la plateforme ARM.

J'ai achevé ma migration vers Scaleway depuis un mois et jusqu'ici tout va bien :-)
