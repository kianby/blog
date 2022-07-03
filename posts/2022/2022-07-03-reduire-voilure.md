<!-- title: Réduire la voilure (bis)  -->
<!-- category: Hébergement -->

Ma précédente  tentative de [réduire mes services auto-hébergés](https://blogduyax.madyanne.fr/2019/reduire-la-voilure/) et d'utiliser des services clefs en main s'était soldée par un échec et un rapide retour en arrière. 

Néanmoins, j'ai une motivation différente pour retenter l'expérience. Il ne s'agit plus d'alléger l'administration du serveur qui est désormais assez réduite :
 
- réaliser les mises à jour du système hôte
- mettre à jour les images des containers après validation rapide sur mon environnement local (insérer lien article) 

J'ai souscrit au VPS le plus modeste de chez Contabo et il est adapté au besoin : 8 Go de mémoire, 200 Go de disque en SSD. Mes processus sont au point : je gère ma veille en combinant les flux RSS avec Selfoss et la lecture hors ligne avec Wallabag ; la publication sur le blog est aux petits oignons avec l'édition Markdown et la publication via un dépôt Git. Ça n'a jamais été si bien rodé même si je publie bien peu cette année. 

Tout fonctionne donc mais j'approche de la limite de l'espace disque à cause du stockage des photos et vidéos familiales. Ma solution actuelle basée sur Seafile et la galerie de photos Pigallery2 est adaptée à mon fonctionnement : l'appli mobile envoie les photos dans un répertoire temporaire et je trie à mon rythme. J'apprécie la souplesse de Seafile pour partionner les documents par librairie et partager une librairie entre utilisateurs. Mais le constat après deux années d'utilisation est que je suis le seul vrai utilisateur de l'application : le gardien des documents familiaux. Quand je dois partager un document j'envoie souvent un lien partagé à la personne ou le document lui-même. 

Pour avoir plus de disque, il faudrait changer de serveur. Mais l'espace disque sur les serveurs est coûteux si on le compare aux solutions de pur stockage. L'idée de confier tous mes fichiers à un drive de confiance s'est imposée. Et conserver un service de galerie photos sur mon serveur pour partager sur des durées limitées certains événements (quitte à dupliquer l'information). J'ai donc refait le tour de l'offre... 

Je refuse encore la facilité avec le stockage chez Google photos pour des raisons de préservation de la vie privée mais aussi pour l'approche consumériste et anti écologique. Stocker sur un service de ce type c'est suivre l'air du temps : agir et vite passer à autre chose : pas d' étape de tri des photos, de suppression des clichés ratés, de prendre le temps après une semaine de voyage ou un évènement de choisir, revoir, classer dans un album puis le partager. Google photos permet de réaliser toutes ces étapes bien sûr mais qui le fait vraiment ? On prend un cliché, on le partage dans l'instant, on envoie tout sur le cloud en vrac. Et l'intelligence artificielle nous enverra des mémos des meilleurs instants. C'est tentant et facile d'y céder,  le prix minimal du stockage et le couplage étroit avec l'appareil photo encourage ce mode de fonctionnement.

Pour l'instant je résiste... J'ai besoin de mes structures de dossiers par année, un dossier par album comme les albums d'antan. Trier, jeter la moitié des photos, conserver ce qui est représentatif. Peut être car je suis né à l'époque du chromatique et des ressources limitées ou peut être par fonctionnement interne. Ceci dit les ressources ont toujours été limitées, on a juste tenté de nous faire oublier que c'est le cas :-)

Après un rapide tour des offres j'ai jeté mon dévolu sur l'offre kDrive de Infomaniak qui propose 2 téraoctets pour 4,49 euros mensuels. Cet hébergeur suisse, n'est pas un inconnu pour moi, je lui ai déjà confié mes mails l'année dernière. Comme toujours, c'est la confiance qui l'emporte pour déléguer ses données. Leur service mail est de qualité, ils promeuvent une attitude écoresponsable et basent leur offre sur des logiciels open source. J'ai donc allégé mon serveur en basculant l'intégralité de mes documents sur le drive. Ils fournissent une application de synchronisation pour tous les systèmes, un application mobile qui *upload* les photos. Et pour partager plus simplement des photos, j'ai installé une application dédiée : [lychee](https://lychee.electerious.com). Avec une installation basique basée sur une base de données SQLite, on peut gérer en full-web l'envoi de photos, la création d'albums et leur partage. 

Pour l'instant ça me semble une très bonne solution à mes besoins.
