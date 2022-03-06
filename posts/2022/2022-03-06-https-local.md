<!-- title: Tester en local avec HTTPS  -->
<!-- category: Hébergement Containers -->

Mes services sont hébergés sur un serveur de containers propulsé par docker compose. L'exposition des services HTTP et HTTPS est géré par le *reverse-proxy* [Traefik](https://traefik.io/traefik/) qui s'occupe aussi de renouveler les certificats SSL délivrés par Let's Encrypt ; pour cela il s'interface avec la plupart des *registrars* (les entités qui gère les noms de domaine). Cela permet de bénéficier de la méthode **dnsprovider** et de demander un certificat *wildcard*  (*.mondomaine.fr) plutôt que des certificats pour chaque hôte du domaine (soit chaque container exposé).

Un serveur à base de containers est facilement portable d'une machine à l'autre et on en vient vite à monter un environnement de test local sur sa machine pour tester / valider avant de déployer sur le serveur. Ce qui est plus *touchy* c'est de se placer dans des configurations similaires au serveur en production et notamment d'avoir du HTTPS.

Après avoir considéré la complication à gérer des certificats auto-signés, j'ai opté pour une solution basée sur la résolution de noms fournie par [Traefik.me](https://traefik.me/). Cette géniale idée permet de résoudre n'importe quel nom de machine du domaine **traefik.me** en **localhost**. Contrairement à ce que le nom du site laisse supposer, ce n'est pas une solution officielle fournie par Traefik mais je crois que [son auteur Pyrou](https://github.com/pyrou) est un utilisateur (et peut-être un fan) de Traefik. En tout cas on peut mettre en œuvre traefik.me avec n'importe quelle autre solution de *reverse-proxy*, les certificats PEM à jour sont fournis sur la page d'accueil du site.

Voici donc ma configuration locale pour résoudre les nom de mes containers en HTTPS sur le domaine traefik.me :


Fichier **docker-compose.traefik-local.yml** :

```yaml
services:
  traefik-local:
    container_name: traefik-local
    image: traefik:v2.5.3
    profiles: ["testing"]   
    ports:
      - 80:80
      - 443:443
      - 8080:8080
    expose:
      - 8080
    labels:
      - traefik.enable=true
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - traefik.yml:/etc/traefik/traefik.yml
      - tls.yml:/etc/traefik/tls.yml
      - certs:/etc/ssl/traefik

  traefik-reverse-proxy-https-helper:
    container_name: traefik-reverse-proxy-https-helper
    image: alpine
    profiles: ["testing"]   
    command: sh -c "cd /etc/ssl/traefik
      && wget traefik.me/cert.pem -O cert.pem
      && wget traefik.me/privkey.pem -O privkey.pem"
    volumes:
      - certs:/etc/ssl/traefik

volumes:
  certs:
```

Fichier **tls.yml**  :

```yaml
tls:
  stores:
    default:
      defaultCertificate:
        certFile: /etc/ssl/traefik/cert.pem
        keyFile: /etc/ssl/traefik/privkey.pem
  certificates:
    - certFile: /etc/ssl/traefik/cert.pem
      keyFile: /etc/ssl/traefik/privkey.pem
```

Fichier **traefik.yml** :

```yaml
logLevel: INFO

api:
  insecure: true
  dashboard: true

entryPoints:
  http:
    address: ":80"
  https:
    address: ":443"

providers:
  file:
    filename: /etc/traefik/tls.yml
  docker:
    endpoint: unix:///var/run/docker.sock
    watch: true
    exposedByDefault: false
    defaultRule: "HostRegexp(`{{ index .Labels \"com.docker.compose.service\"}}.traefik.me`,`{{ index .Labels \"com.docker.compose.service\"}}-{dashed-ip:.*}.traefik.me`)"

http:
  # global redirect to https
  routers:
    http-catchall:
      rule: "hostregexp(`{host:.+}`)"
      entrypoints:
        - http
      middlewares:
        - redirect-to-https

  # middleware redirect
  middlewares:
    redirect-to-https:
      redirectscheme:
        scheme: https
        permanent: true
```        

On notera le container compagnon "traefik-reverse-proxy-https-helper" qui s'occupe de rapatrier une version à jour des certificats et de les stocker sur le volume **certs** partagé avec le container "traefik-local".

La configuration de traefik pour le serveur est classique. Dans mon cas elle s'interface avec le registrar infomaniak qui me loue mon nom de domaine.

Fichier **docker-compose.traefik-infomaniak.yml** :

```yaml
services:
  traefik-infomaniak:
    container_name: traefik-infomaniak
    image: traefik:v2.5.3
    profiles: ["production"]
    command:
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false      
      - --api.dashboard=false
      - --entrypoints.http.address=:80      
      - --entrypoints.https.address=:443
      - --certificatesresolvers.letsencrypt.acme.email=${LETSENCRYPT_EMAIL}
      - --certificatesresolvers.letsencrypt.acme.storage=/acme.json
      - --certificatesResolvers.letsencrypt.acme.dnsChallenge=true
      - --certificatesresolvers.letsencrypt.acme.dnschallenge.provider=infomaniak
    environment:
      - INFOMANIAK_ACCESS_TOKEN=${LETSENCRYPT_DNSPROVIDER_TOKEN}
    labels:
      - traefik.enable=true
      - traefik.http.routers.api.entrypoints=http
      - traefik.http.routers.api.entrypoints=https
      - traefik.http.routers.api.service=api@internal
      # middleware auth
      - traefik.http.routers.api.middlewares=auth
      - traefik.http.middlewares.auth.basicauth.users=${BASIC_AUTH}          
      # request widlcard certificate
      - traefik.http.routers.api.tls.certresolver=letsencrypt
      - traefik.http.routers.api.tls.domains[0].main=${DOMAIN}
      - traefik.http.routers.api.tls.domains[0].sans=*.${DOMAIN}
      # global redirect to https
      - traefik.http.routers.http-catchall.rule=hostregexp(`{host:.+}`)
      - traefik.http.routers.http-catchall.entrypoints=http
      - traefik.http.routers.http-catchall.middlewares=redirect-to-https
      # middleware redirect
      - traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https
      - traefik.http.middlewares.redirect-to-https.redirectscheme.permanent=true     
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - acme.json:/acme.json
```

Le support des profils de docker-compose permet de choisir la bonne configuration au démarrage des containers.

En mode "production" sur le serveur :

    docker-compose --env-file .env --profile production up -d

En mode "test" sur la machine locale  :

    docker-compose --env-file .env --profile testing up    

Les configurations docker-compose de l'article sont un peu simplifiées pour faciliter la compréhension. Les sources complètes [sont sur GitHub](https://github.com/kianby/selfhosting).
