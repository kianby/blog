---
layout: post
title: Les mots de passe
category: Sécurité
tag: planet
---

J'ai été sensible assez tôt à l'importance de la sécurité des mots de passe. Aujourd'hui, plus qu'hier, on ouvre quantité de comptes sur des sites de commerce, de banque ou d'assurance, de santé.<!-- more --> J'avais choisi le logiciel [KeePassX](https://www.keepassx.org), un coffre fort numérique protégé par un mot de passe unique, et suivi les bonnes pratiques : associer un mot de passe costaud et différent pour chaque site. Tout avait bien démarré avec de la bonne volonté, mais l'informatique des nuages et la mobilité ont progressivement compliqué les choses.

Au début, c'était simple car on avait une machine familiale dans la maison. Puis au fil des ans, j'ai acquis un portable, puis une tablette et un smartphone, et le casse-tête de la synchronisation entre les périphériques s'est posé. J'ai commencé simple (la machine familiale est la machine maître pour le fichier et des copies sont installées sur les autres périphériques) puis ça a fini par une synchronisation de la base KeePassX à travers Nextcloud, ce qui permet à n'importe quel périphérique de rajouter un mot de passe si besoin.

Enfin il s'est rajouté le problème de l'accès à ses mots de passe depuis des machines tierces (en milieu professionnel notamment). On peut ouvrir les mots de passe sur le téléphone et recopier le mot de passe dans le navigateur de la machine mais c'est pénible. Quand on est développeur, on a forcément une identité numérique (un compte GitHub, un compte StackOverflow, etc...) et on n'est pas ~~forcément~~ schizophrène donc on ne va pas en ouvrir un différent à chaque changement de poste. Du coup, j'ai ajouté la synchronisation de Mozilla Firefox dans la boucle, protégé par un *master password* pour partager certains identifiants liés à mon activité professionnelle en me rassurant que la référence c'est ma base KeePassX.

Le bilan, au bout de 12 ans, c'est que c'est un sacré bazar :

- j'utilise une version antédiluvienne de KeePassX pour être compatible avec celle supportée par mon téléphone : la sécurité globale est nivelée par celle du maillon le plus faible
- j'ai des mots de passe dans KeePassX, des doublons dans Firefox et probablement des mots de passe oubliés uniquement mémorisés dans Firefox.
- la sécurité du stockage des mots de passe dans Firefox [n'est pas terrible](https://www.bleepingcomputer.com/news/security/firefox-master-password-system-has-been-poorly-secured-for-the-past-9-years) mais c'est tellement commode le remplissage automatique des formulaires quand on est sur un site.
- la base KeePassX est physiquement sur mon téléphone : même si c'est chiffré sérieusement, combien de temps faudrait-il à quelqu'un de motivé et équipé pour la craquer en cas de vol ?

Cela fait beaucoup de points négatifs, il était temps de repenser tout cela et de se mettre au goût du jour. J'ai regardé un peu ce qui se fait avec quelques idées en tête :

- copier-coller des mots de passe entre une application et un site Web c'est dépassé (et compliqué sur un appareil mobile),
- stocker une base de mots de passe sur un périphérique mobile c'est risqué,
- le risque de piratage des sites Web est plus grand qu'auparavant, la solution doit être simple pour créer un mot de passe différent par site.

J'ai finalement choisi [BitWarden](https://bitwarden.com) qui remplit mes critères. Le coffre-fort est hébergé sur leurs serveurs, dans le cloud Azure Microsoft pour être exact. On peut décider de l'héberger soi-même mais je doute faire mieux que des professionnels pour en sécuriser l'accès. On déverrouille l'accès au coffre-fort avec un mot de passe maître, le seul à retenir finalement ; idéalement c'est une phrase plutôt qu'un simple mot de passe car toute la sécurité repose sur lui. Et si on l'oublie, ce n'est pas la peine de le demander aux administrateurs de BitWarden car ils ne l'ont pas, il n'est pas stocké chez eux. L'avantage de BitWarden par rapport à d'autres solutions du même genre c'est aussi qu'il propose des applications pour toutes les plateformes : des extensions de navigateurs, des applications bureau et mobiles. Autre bon point, ils ont des fonctions d'import pour la plupart des solutions concurrentes.

Alors comment décider de faire confiance à BitWarden ? Ce qui compte pour moi c'est :

- la publication en Open Source du cryptage pour être audité en toute transparence,
- la possibilité de sortir ses données avec un export en CSV,
- le sérieux de l'hébergement de la solution.

La confiance, c'est compliqué. Quelles que soient les garanties, il y a un moment où, en son âme et conscience, il faut se  lancer ou rebrousser chemin. J'ai franchi le pas et décidé de leur confier mes mots de passe.

Premier écueil pour sortir les mots de passe de Firefox : l'extension [Password Exporter](https://addons.mozilla.org/en-US/firefox/addon/password-exporter) ne supporte pas Firefox 57, j'installe la version Firefox 52 ESR. D'ailleurs on annonce la version Firefox 62 ESR pour le mois d'août, ça me conforte dans l'idée que c'est le moment de s'en occuper. L'extension exporte les mots de passe dans un fichier CSV et BitWarden permet de les importer. Pour KeePass, on a un import mais comme j'ai une version KeePassx 0.4 j'ai du passer par la migration vers une version récente de KeePass avant de pouvoir importer ma base de mots de passe dans BitWarden. A ce stade, j'ai un coffre-fort avec plein de doublons entre les données de FireFox et KeePass ; bien fait pour moi, le gros ménage commence.

Je désactive la mémorisation des identifiants de Firefox et je vide les identifiants enregistrés puis j'installe l'extension BitWarden pour Firefox. On ouvre le coffre-fort en entrant son méga mot de passe.

![Ouverture coffre-fort](/images/2018/bitwarden-ouverture.png)

On peut paramétrer la fermeture du coffre-fort. A la maison, on laissera le coffre-fort ouvert jusqu'à la fermeture du navigateur ; au travail on optera pour une fermeture automatique sur inactivité, au bout de 15 minutes. Le principal intérêt d'avoir un gestionnaire de mots de passe couplé au navigateur c'est le remplissage des formulaires pour ne plus faire de copier-coller de mots de passe. L'icône de BitWarden change quand un mot de passe est disponible pour un site et il suffit de le sélectionner pour remplir le formulaire.

![Remplissage de formulaire](/images/2018/bitwarden-remplissage.png)

J'ai terminé ma bascule vers BitWarden depuis une semaine ; je me sers de l'extension Firefox et de [l'accès Web](https://vault.bitwarden.com), je n'ai installé aucune application native sur mes périphériques. Par sécurité, j'ai prévu une sauvegarde régulière et manuelle vers un support physique, c'est à dire un export des mots de passe vers une clef USB qui reste dans un coffre (non numérique celui-ci)... au cas où BitWarden disparaitrait ou bien si je deviens amnésique ;-)