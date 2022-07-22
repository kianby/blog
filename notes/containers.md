<!-- title: Les containers -->

# Docker

## docker-compose.yml

Concaténation de //docker-compose.yml// :

    # composition de docker-compose
    # si ficher d'environnement ajouter --env-file submodule/A_SUB_PROJECT/.env 
    docker-compose -f submodules/A_SUB_PROJECT/docker-compose.yml config > _tmp_.A.yml
    docker-compose -f submodules/B_SUB_PROJECT/docker-compose.yml config > _tmp_.B.yml
    docker-compose \
    -f _tmp_.A.yml \
    -f _tmp_.B.yml \
    config > docker-compose.yml
    rm _tmp_.*.yml

Gérer les //docker-compose.yml// des sous-répertoires comme un seul avec une fonction bash

    docker-compose ()
    {
        /usr/local/bin/docker-compose $(find -name 'docker-compose*.yml' -type f -printf '%p\t%d\n'  2>/dev/null | sort -n -k2 | cut -f 1 | awk '{print "-f "$0}') $@
    }

## Manipuler les images

construire depuis le répertoire du Dockerfile

    docker build -t srmail .

lister les images :

    docker images

supprimer une image :

    docker rmi <image id>

Lister les containers actifs:

    docker ps

Lister tous les containers :

    docker ps -a

Supprimer un container

    docker rm <container id>

Construire et démarrer un container en interactif

    docker run --name srmail_trunk -ti srmail /bin/bash

Démarrer et stopper un container

    docker start <container id or name>
    docker stop <container id or name>

Démarrer et attacher une console

    docker start srmail_trunk
    docker attach --sig-proxy=false srmail_trunk
    # sortir avec CTRL p + CTRL q

Exécuter une commande dans un container

    docker exec srmail_trunk ps -ef
    docker exec -i -t 665b4a1e17b6 /bin/bash

Inspecter le file system d’une image

    docker run --rm -it 044e1532c690 sh 

## Publier ses images 

Après la construction de l'image on peut la publier :

    docker build -t tcpping .
    
Se connecter à la registry Docker (hub.docker.com)

    docker login --username=kianby

Retrouver l’id de l’image

    docker images

Tagguer l’image et pousser vers Docker Hub

    docker tag f5a6531f8874 kianby/tcpping
    docker push kianby/tcpping

Variation avec une version autre que latest

    docker tag 87615e686d1f kianby/hugo:0.31.1

# Buildah

Construire une image depuis une URL 

    buildah build -t www-madyanne:latest github.com/kianby/docker-image-www-madyanne

Lister les images 

    buildah images

Stockage local dans //~/.local/share/containers//
