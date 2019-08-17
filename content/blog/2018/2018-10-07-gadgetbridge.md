---
layout: post
title: Gadget Bridge et autres connectés
category: Matériel
tag: planet
---

Je porte un bracelet Xiaomi Mi-Band connecté depuis Noël dernier. Ce n'est pas un cadeau tentateur pour libriste en perdition mais un achat assumé.<!-- more --> L'angoisse de l'approche de la cinquantaine probablement, je voulais moi aussi mesurer la qualité de mon sommeil et mon manque d'activité physique, bref vérifier [si moi aussi je ne serais pas l'homme du 21ème siècle.](https://www.youtube.com/watch?v=AEv9VLQegvY&list=PLTwkIOfLU8_reQI_2mapPF4zv2Co6lSTg&index=8) Je pensais que ça m'amuserait quelques semaines mais c'est devenu une habitude et ça a aidé à une reprise d'activité sportive plus régulière. 

Le bracelet est autonome ; il a des capteurs, il enregistre et à l'occasion on synchronise les données vers une application mobile. Dans ce mode, il a une autonomie de 4 à 6 semaines, c'est impressionnant. On peut aussi l'utiliser en mode connecté au téléphone pour envoyer des notifications en temps réel : appels, messages. Ce mode est beaucoup plus consommateur en batterie (du bracelet et du téléphone). 

J'ai utilisé l'objet en mode autonome pendant plusieurs mois. Le premier jour, j'ai installé l'application officielle Xiaomi qui s'occupe aussi des mises à jour du firmware. Il faut créer un compte chez Xiaomi (sic!) 
et le lendemain matin on apprend qu'on a mieux dormi que 43% des autres ~~membres du troupeau~~ utilisateurs. Et oui, le ticket d'entrée du 21ème siècle coûte le leg de ses données personnelles... que deviennent les données ensuite ? combien d'années avant qu'elles soient revendues à mon groupement mutualiste qui me fera un tarif santé fonction de mon rythme de vie ? Bref, on sait où ça mène ! 

Donc déconnexion de l'appli officielle et recherche d'une meilleure solution ; je n'ai pas cherché longtemps, je traîne suffisamment sur [la boutique F-Droid](https://f-droid.org) pour avoir remarqué l'application [Gadgetbridge](https://github.com/Freeyourgadget/Gadgetbridge) qui :

- gère la plupart des bracelets / montres Xiaomi et les Pebble,
- conserve les données sur l'appareil et propose même un import / export de la base de données
- propose des fonctionnalités communes à tous les équipements supportés : activité (compteur de pas),  qualification du sommeil, réveil, 
- des fonctionnalités spécifiques en fonction du type de bracelet ou de montre joliment détaillées [dans cette matrice](https://github.com/Freeyourgadget/Gadgetbridge/blob/master/FEATURES.md)   

Je n'ai pas parlé de la fonction réveil. Ca peut sembler anecdotique mais quand on est traumatisé par les sonneries à l'aube, on échange volontiers contre la douce vibration du bracelet. 

![gadget bridge](/images/2018/gadgetbridge.png)

Récemment je suis passé dans le mode d'utilisation connecté au téléphone alors que je refusais, au début, ce fil à la patte. Mais avec ces téléphones Android un peu récents, tous identiques, rectangulaires, sans saveur où les constructeur ont le droit de choisir la taille et la qualité de l'appareil photo mais surtout aucune  personnalisation matérielle non validée par le dieu Google, on n'a même plus la LED de notification qu'on trouvait sur les premiers modèles et on se retrouve finalement à les allumer régulièrement juste pour vérifier si on n'a pas raté un appel ou un SMS important. J'ai donc commencé à utiliser le mode notification du bracelet en environnement professionnel. 

La notification sur le bracelet Mi Band 2 est minimale : on sait que le téléphone (en vibreur dans un coin) sonne ou qu'on a reçu un message. C'est déjà pas mal et ça m'a donné envie de passer au niveau supérieur avec la montre Xiaomi Amazfit Bip qui reçoit les messages SMS, affiche le nom des correspondants des appels et peut même afficher les prévisions météorologiques. Pour le reste on retrouve les fonctionnalités du bracelet Mi Band (someil, activité) et la même technologie d'écran qui fournit une autonomie de plusieurs semaines. C'est ce qui a entériné mon choix d'ailleurs, je fuis les montres qu'il faut recharger chaque soir.

C'est donc mon cadeau d'anniversaire (merci M. de mon coeur), étrenné depuis 2 semaines, toujours de concert avec Gadgetbridge qui est la meilleure solution pour ce matériel car il sait résoudre le problème des accents. En effet, la montre propos un firmware chinois et un firmware anglais pour l'international. Soit on teste des firmware non officiels pour le français, soit on reste en international ce qui est mon choix. Et dans ce cas-ci, les SMS sont épurés de leurs caractères accentués ce qui complique un peu la lecture. Gadgetbridge fournit un paramètre *transcription* qui remplace les accents par leur équivalent ASCII : "é" devient "e", ce qui est bien mieux qu'un abscons symbole ¤ 

La fonction météo semblait mal engagée mais on trouve l'application *Weather Notification* sur F-DROID qui fournit les prévisions de OpenWeather Map à GadgetBridge et cela fonctionne très bien. 

Enfin que serait une montre connectée sans la possibilité de changer de cadran au gré de ses humeurs. Le site [Amazfitwatchfaces](https://amazfitwatchfaces.com/bip/) recense les contributions des graphistes et permet de télécharger des nouveaux cadrans. On peut créer un compte et voter pour les meilleurs artistes pour les encourager, c'est  bon enfant. 

![watch face](/images/2018/amazfitwatchfaces.png)

Bon voilà je suis revenu sur Android et je suis connecté. A ce propose je remercie le talentueux [Bunnyy](https://forum.xda-developers.com/member.php?u=8946392) pour le portage de [la ROM Resurection Remix](https://forum.xda-developers.com/samsung-a-series/development/rom-resurrection-remix-rr-v6-unofficial-t3765542) sur Samsung A5 2016 : je compte sur toi pour faire fonctionner les appels Bluetooth sous peu. 

Est-ce que je suis entré dans le 21ème siècle ? un peu mais tout est loin de me plaire et j'essaie de ne choisir que les meilleurs côtés :-) 