<!-- title: Fuse avec Docker -->
<!-- category: Hébergement -->

La plus grosse partie du stockage de mon serveur est utilisée pour la photothèque familiale. J'en suis à 80 Go (pour 20 ans), ce qui n'est rien comparé aux usages d'aujourd'hui. Un utilisateur mobile lambda avec une présence sur les réseaux sociaux en balance probablement autant mensuellement sur les serveurs de Google ou Apple. Je reste dans un usage "album de famille" avec des photos pour les évènements de la vie.

Néanmoins stocker tout cela en ligne en gardant la maîtrise technique, sans céder aux sirènes des offres gratuites (du moins monétairement parlant), demande de l'effort :

- D'abord trouver un serveur avec suffisamment de disque à un tarif raisonnable : je suis aujourd'hui sur l'offre VPS S de [Contabo](https://contabo.com/en/vps/) avec 200 Go de SSD.
- Ensuite choisir ses logiciels. Mon stockage de documents et photos est géré par Seafile depuis [mon départ de NextCloud](https://blogduyax.madyanne.fr/2020/dispersion-du-gros-nuage/). Et pour la galerie photo, je viens de quitter l'excellent [pigallery2](https://bpatrik.github.io/pigallery2/) pour [photoview](https://photoview.github.io/).

Seafile a son propre système de stockage. On ne peut pas simplement partager un dossier avec la galerie photo. C'est un problème qui vient de trouver une bonne solution mais avant cela je suis passé par deux étapes intermédiaires :  

1. Je duplique mes photos sur le serveur en utilisant le client de synchronisation *seaf-cli* : je synchronise la bibliothèque des photos dans un répertoire, je monte le répertoire dans le container de pigallery2. J'avais un peu de moins de photos : 75 Go x 2 => il me restait 50 Go d'espace sur le VPS (enfin 25 vu que je duplique tout). C'était pas génial, sûrement pas Green IT mais j'ai fonctionné ainsi une année.
2. je m'assois, je réfléchis et je prends le temps de lire  la documentation de Seafile et je découvre qu'[ils fournissent un daemon fuse](https://manual.seafile.com/extension/fuse/) pour exposer une bibliothèque Seafile en filesystem sur un point de montage. Du coup, j'essaie de gérer FUSE depuis Docker et je me casse les dents. C'était une période où je manquais de temps (et de ténacité) donc je réinstalle Seafile et Pigallery2 en versions natives (sans Docker).

J'avais au moins récupéré la moitié de mon espace disque mais avoir à nouveau une installation hybride (mi-docker, mi-services sur la machine hôte), devoir réinstaller un NginX en reverse proxy après mes efforts pour maîtriser [Traefik](https://traefik.io/) et avoir une installation full-container, ce n'était vraiment pas satisfaisante. Néanmoins je suis resté dans cette situation quelques mois. 

J'ai enfin trouvé le temps (et l'envie) de me pencher sur le sujet et expérimenter le support de FUSE entre deux containers. FUSE demande des capacité de la machine hôte, le point de montage sera forcément sur l'hôte (attention à la sécurité) et partagé entre les deux containers (Seafile et la galerie photo dans mon cas).

Le bout de docker-compose de Seafile :

```yaml
volumes:
  - type: bind
    source: ${ROOT_INSTALL}/data/seafile-fuse
    target: /seafile-fuse
    bind:
      propagation: rshared
privileged: true
cap_add:
  - SYS_ADMIN  
```

Et celui de Photoview :

```yaml
volumes:
  - type: bind
    source: ${ROOT_INSTALL}/data/seafile-fuse
    target: /photos        
    bind:
      propagation: rslave
privileged: true
cap_add:
  - SYS_ADMIN
```

Je suis revenu à un serveur entièrement conteneurisé. Les sources complets sont sur mon [GitHub](https://github.com/kianby/selfhosting).
