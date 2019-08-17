---
layout: post
title: Bilan hébergement 2018
category: Hébergement
tag: planet
---

Voici un rapide état de l'hébergement et des changements survenus l'année dernière. Mon serveur est toujours chez Online mais j'ai troqué ma Dédibox Start avec 1 téra de disque SATA contre le modèle avec 120 giga de SSD et je sens vraiment la différence sur la latence des services Web. Je ne m'étends pas sur la migration de OpenBSD vers Proxmox puis Docker en 14 mois, largement décrite [ici](https://blogduyax.madyanne.fr/2018/hebergement-containers/) et [là](https://blogduyax.madyanne.fr/2018/retour-sur-la-migration-vers-docker/). 

### Mes incontournables 

Mes services hébergés restent essentiellement les mêmes. 

J'use et abuse de l'excellent [Wallabag](https://wallabag.org/fr) pour lire en différé mes articles rencontrés au détour d'une recherche.

Je lis quotidiennent mes flux RSS. J'ai récemment viré Tiny Tiny RSS dont l'application mobile m'insupportait de plus en plus pour une découverte opportune (merci F-Droid): [Selfoss](https://www.selfoss.aditu.de/) qui prouve qu'on peut faire mieux avec moins (au revoir PostgreSQL et bonjour SQLite) et avoir une application mobile **ergonomique**. 

C'est d'ailleurs mon leitmotiv : privilégier le minimalisme s'il apporte le service rendu et l'isolation des services (Docker quoi) donc SQLite c'est parfait. 

Je suis toujours fan de [Shaarli](https://sebsauvage.net/wiki/doku.php?id=php:shaarli) qui stocke mes favoris depuis presque 5 ans. 

Le blog est toujours là, propulsé par [Hugo](https://gohugo.io/), mais j'ai viré tout analyseur de trafic.

### Les disparitions

Je n'héberge plus mon cloud. Ce n'est pas une décision technique (j'ai géré mon Nextcloud pas mal de temps), mais une volonté de déléguer à des tiers de confiance ce qui me prend du temps à administrer. J'ai commencé avec [la gestion des mots de passe](https://blogduyax.madyanne.fr/2018/les-mots-de-passe/) déléguée à BitWarden (ce qui fait grincer les dents  de quelques libristes). 

J'ai confié mes données à [Cozy Cloud](https://cozy.io) ; j'ai choisi l'offre d'hébergement 1 téra que je teste toujours gracieusement (merci les gars !). Cozy c'est plus que du stockage de fichier, c'est un concept qui n'a pas d'équivalent (du moins unifié dans le même outil) avec sa panoplie de connecteurs pour récupérer ses factures et ses remboursements de santé. Le partenariat avec Linxo est génial (et je ne dis pas ça parce que Linxo est réussite locale) car il apporte une analyse des données et effectue des rapprochements intelligents (un remboursement de sécu et le paiement du médecin généraliste par exemple). L'équipe de Cozy est sympa, accessible. Moi je suis une feignasse car j'ai commencé à développer un connecteur pour récupérer les factures des Eaux de Marseille mais c'est en chantier :-(    

J'ai délégué la gestion de mon agenda et de mes contacts à l'association *a mère Zaclys* qui propose (entre autre service) une instance Nextcloud. C'est de l'associatif et je n'ai pas souvenir d'une seule interruption de service sur l'année écoulée. Pour quelques euros à l'année, on ~~peut~~ doit les encourager à continuer :-)  

### Les nouveautés 2018

J'ai découvert [Jirafeau](https://gitlab.com/mojo42/Jirafeau) pour partager simplement des fichiers. Je ne l'utilise pas beaucoup mais j'ai aimé l'outil donc je l'ai ajouté à ma panoplie... en 30 minutes (je vous ai parlé de Docker ?).

J'ai eu besoin de garder trace des corrections et évolutions de mes projets persos et d'écrire un peu de documentation. Comme je ne voulais pas dépendre plus de GitHub, j'ai installé mon [service Redmine](https://www.redmine.org/) qui regroupe dans le même outil une gestion de tickets et un Wiki. Ca fait le job mais je trouve l'interface un peu molle et je suis pas convaincu par l'ergonomie générale. Si je trouve une meilleure alternative, je migrerai. 

J'ai commencé à utiliser [Qwant](https://www.qwant.com) à 100% en début 2018, en perso et en pro et je suis satisfait des résultats. Au début, il m'arrivait de vérifier pertinence d'un résultat de recherche (souvent anglophone) en faisant appel à Google. Ce n'est plus le cas, je suis convaincu de la qualité du résultat. On peut vraiment être fier de Qwant (Cocorico !). Je n'en dirai pas autant de Mozilla, je reste un grand supporter de Firefox mais la confiance a été écornée donc je leur confie ma navigation mais pas plus. 
