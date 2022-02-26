<!-- title: Sécurisation Docker : des pistes -->
<!-- category: Hébergement -->

Je réfléchis à renforcer la sécurité de mon serveur à base de docker compose. J'ai plutôt confiance dans mes containers mais c'est un sentiment subjectif et non justifiable. Certes j'utilise autant que possible des images officielles mais :
- je n'ai aucun outil pour tester les vulnérabilités 
- je ne suis pas à l'abri d'une compromission d'un container par l'exploitation d'une faille.

Je m'intéresse à deux aspects de la sécurisation :
1. le réseau : le contrôle des flux intra-containers et des containers vers l'hôte
2. les permissions : tous mes containers s'exécutent actuellement en tant que *root*

Le contrôle du réseau est limité par ce que propose Docker, et plus exactement *docker compose*. J'ai retenu la possibilité de segmenter en plusieurs réseaux et de définir dans quel réseau placer un container avec l'option *-networks*.   

Exemple avec le blog et deux réseaux "blog-backend" et "blog-frontend" :

```yaml
version: '3'

services:
  stacosys:
    container_name: stacosys
    image: kianby/stacosys
    volumes:
      - ${ROOT_INSTALL}/data/stacosys:/config
    networks:
      - blog-backend
    restart: unless-stopped
    expose:
      - 8100
  blog:
    container_name: blog
    image: kianby/blogduyax
    depends_on:
      - stacosys     
    networks: 
      - blog-backend
      - blog-frontend
    restart: unless-stopped
    expose:
      - 80
    labels:
      - traefik.enable=true
      - traefik.http.routers.blog.rule=Host(`${HOST_BLOG}.${DOMAIN}`)
      - traefik.http.routers.blog.entrypoints=https
      - traefik.http.routers.blog.tls=true
      - traefik.docker.network=blog-frontend
```      

Placer un container dans deux réseaux lui procure une adresse IP sur chacun et il a, de facto, accès à tous les containers sur ces deux réseaux. Cela permet de ne pas placer un container avec un rôle de *backend* (comme une base de donnée) sur un réseau *frontend* qui est exposé vers l'extérieur (via Traefik). Cela protège un peu plus d'une compromission d'un container mais ce n'est pas extraordinaire car chaque container peut accéder à la machine hôte et à tous les containers des réseaux auxquels il appartient et ceci sans restriction. 

Je réfléchis à des moyens d'aller plus loin dans la sécurisation avec des techniques officielles. J'ai lu un cas de mise en oeuvre où on désactive la gestion d'iptables par Docker et on crée ses propres règles pour contrôler tous les échanges. Effectivement c'est efficace mais on perd toute la gestion dynamique des containers et on se retrouve à administrer un pare-feu. Je ne souhaite pas aller dans cette voie. 

Pour l'aspect documentation, j'ai utilisé l'outil [Nwdiag](http://blockdiag.com/en/nwdiag/nwdiag-examples.html) pour représenter graphiquement les réseaux qui composent mon déploiement. Les sources sont sur le projet : https://github.com/kianby/selfhosting/



