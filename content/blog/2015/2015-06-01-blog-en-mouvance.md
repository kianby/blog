---
layout: post
title: Hébergement en mouvance
category: Hébergement
tag: planet
---

Très satisfait de mon hébergeur actuel, je reste à l'écoute du marché. Ah
pardon on ne parle pas recrutement<!-- more --> j'ai confondu ;-) Je reprends : bien que
très satisfait de mon hébergement je me suis laissé tenter par
[FirstHeberg](https://www.firstheberg.com) qui propose une large gamme de VPS
répartie en trois familles :

- des containers légers OpenVz
- des machines virtuelles Qemu
- des machines virtuelles Qemu avec option de sauvegarde

Chaque famille se décline bien sûr en plusieurs puissances, plusieurs capacités
RAM et disque. Ce qui m'a intéressé c'est la possibilité de louer une machine
virtuelle pour le même prix que mon conteneur OpenVz actuel. J'ai donc souscrit
à l'offre GP1 cette semaine en choisissant un système Debian 8 (Jessie). La
livraison est classique avec l'envoi des informations de connexion adresse IP,
DNS en fhnet.fr et mot de passe du compte root. Le service SSH est activé en
standard. Je n'ai pas encore beaucoup joué avec les outils mais une interface
d'administration sobre fournit l'essentiel : un redémarrage forcé de la VM, la
possibilité de réinstaller avec l'OS de son choix et des graphes d'activité du
VPS pour la dernière heure : utilisation CPU, consommation mémoire, trafic
réseau et activité disque.

Mon objectif c'est de migrer progressivement les services d'un serveur à
l'autre. Alors plutôt que de réinstaller manuellement j'ai saisi l'opportunité
de me former à [Ansible](http://docs.ansible.com), un outil de déploiement et
des gestion des configurations. L'utilisation usuelle consiste à définir des
recettes d'installation (*playbook* dans la terminologie Ansible) et de
vérifier la conformité des cibles de déploiement avec ces recettes. C'est un
outil utilisé pour superviser des parcs de serveurs mais il a aussi de
l'intérêt dans mon cas d'utilisation : j'ai créé une machine virtuelle sous
Virtual Box avec les caractéristiques du serveur FirstHeberg et je mets au
point mes playbooks. L'idée c'est de valider systématiquement sur la machine
virtuelle locale avant de mettre en production et de formaliser le déploiement
du serveur à la sauce Ansible qui emploie un format textuel et compréhensible
afin de *versionner* les changements sous GIT et faciliter le changement
d'hébergement dans l'avenir, bref d'avoir une démarche un peu plus
professionnelle quant à la gestion des configurations du serveur.

Pour l'anecdote, Ansible est un outil Python (hé oui encore un) comme
[Fabric](http://www.fabfile.org) (que je connais et utilise déjà) et il ne
demande qu'un accès SSH pour interagir avec les serveurs. De bons articles ont
déjà été publiés sur le [Planet](http://www.planet-libre.org), je peux rajouter
l'excellent [tuto de leucos](https://github.com/leucos/ansible-tuto)  qui
complète la documentation officielle déjà très complète par des exemples.
