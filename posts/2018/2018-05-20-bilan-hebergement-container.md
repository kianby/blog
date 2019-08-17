<!-- title: Hébergement et taille de containers -->
<!-- categories: Hébergement Containers -->
<!-- tag: planet -->

Dans le prolongement de mon article ["Choix du système pour s'auto-héberger"](https://blogduyax.madyanne.fr/2018/quel-systeme-serveur), je peux faire un bilan des 6 mois écoulés avec mon hébergement à base de containers LXC avec la distribution [Proxmox](https://fr.wikipedia.org/wiki/Proxmox_VE).<!-- more -->

# Commençons par les avantages

Le passage d'une installation monolithique à une installation containerisée avec des services répartis dans une dizaine de containers donne la flexibilité de choisir le meilleur outil pour chaque tâche :

- les micro-services Python se contentent de containers Alpine ultra-légers (64 Mo de RAM).
- le service Nextcloud a migré d'un container Alpine à un container ArchLinux. Je n'aurais jamais pensé utiliser Arch sur un serveur mais c'est une bonne solution pour garantir une version stable et toujours à jours en terme de sécurité de Nextcloud.
- [le middleware RabbitMQ](https://blogduyax.madyanne.fr/2018/mes-notes-sur-rabbitmq) est installé sur sa distribution de prédilection **CentOS** dans un container dédié.

La modularité facilite l'administration du serveur : on a besoin d'un nouveau service, on rajoute un container et on limite les risques de *casser quelque chose* sur l'installation existante.

L'interface Web d'administration de Proxmox est de qualité. Au delà de la gestion des machines virtuelles KVM et des containers LXC, elle donne une vision des ressources CPU /Mémoire consommées par container et au niveau physique.

![Tableau de bord Proxmox](/images/2018/proxmox-dashboard.png)

# Ce qui n'est pas parfait

J'ai un service Nextloud, aisé à gérer dans un seul container avec l'application, les données et la base de donnée. Pour sauvegarder, c'est moins drôle, cela revient à sauvegarder le container de bientôt 100 Go avec Proxmox et la balancer sur l'espace FTP de 100 Go offert par Online. Autre option, sauvegarder les données du calendrier et les contacts [avec des scripts *maison*](https://blogduyax.madyanne.fr/2015/deploiement-et-sauvegarde/) et mettre en place une sauvegarde classique vers un disque externe des fichiers synchronisés sur mon ordinateur portable. C'est vers cette solution que je m'oriente.

La nuée de services développés par bibi autour du blog (SRMail, Stacosys) serait parfaite pour Docker. Aujourd'hui c'est installé dans des containers LXC, avec des partages de répertoires entre le hôte et les containers pour externaliser la configuration et les données. Docker permettrait de standardiser cet assemblage et d'en profiter à la maison pour facilement remonter un environnement de test.

C'est vraiment le point négatif : j'ai des relations troubles entre la machine hôte et les containers. J'ai installé un serveur NginX sur Proxmox qui fait du proxy vers les NginX des différents containers en fonction du service demandé. J'ai partagé des répertoires entre le hôte et les containers pour externaliser les parties sensibles (la configuration et les données) et faciliter leur sauvegarde puis la machine hôte. Je gère les certificats Let's Encrypt au niveau du hôte aussi. Bref j'ai une installation *custom* de Proxmox avec des containers mais aussi plein de trucs installés au niveau de l'hyperviseur. 

# Conclusion

Ca fonctionne bien mais si j'ai un souci (mise à jour de Proxmox qui casse quelque chose, panne du serveur), je risque de passer des jours à tout remettre en service car j'ai tout installé à la mano. L'idée de tout reprendre à zéro en passant plus de temps pour tout containeriser refait surface. L'idéal pour moi serait de tout exécuter dans des containers et d'avoir une seule arborescence de fichiers à sauvegarder. J'avais tâté un peu Docker et je sais que ça prend pas mal de temps de repenser en containers, de choisir les bonnes images de base... Autre bémol, miser sur une seule entreprise ne m'emballe pas, malgré les efforts de l'[Open Container Initiative](https://blog.docker.com/2017/07/demystifying-open-container-initiative-oci-specifications) pour standardiser partiellement la technologie. 

Donc j'étudie les options :

- un provisioning avec Ansible d'un container LXC générique
- l'ajout de Docker à Proxmox pour rajouter Docker au panel KVM / LXC: dockeriser c'est long, donc garder Proxmox permettrait de répondre rapidement à un besoin avec un container LXC, quitte à dockeriser ensuite le service dans un 2ème temps...

Si vous avez des suggestions je suis carrément preneur :-)