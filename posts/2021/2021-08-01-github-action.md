<!-- title: Github action et Docker -->
<!-- category: Développement -->

J'ai utilisé les workflows de Github, appelés *"Github Actions"* pour constuire et publier mes images Docker sur le Docker Hub. Jusqu'à aujourd'hui, c'était un process géré *à la papa* ; j'avais un projet commun avec tous mes docker files, la plupart n'était plus utilisés depuis un bail et je lançais les quelques commandes docker build / tag / push à la demande. 

Et puis la finalisation de la version 2.0 de Stacosys qui est une version orientée qualité (suppression de demi-fonctionalités jamais mises en oeuvre, ajout de tests unitaires, simplification de la base de code existante), m'a ramené sur le sujet de la CI/CD complètement laissé de côté dans mes projets perso.

J'ai donc fait la liste des images réellement utilisées dans mon docker-compose : 
- les dockerfiles qui correspondent à un projet de dev ont été rapatriés dans le projet Github correspondant,
- les images pur docker, personnalisations basées sur d'autres images ont donné lieu à la création d'un projet dédié sur Github.

Il ne restait plus qu'à configurer la chaîne CI/CD de Github. 

D'abord on crée un token d'accès pour Github depuis son compte Docker Hub et on le note soigneusement. Puis pour chaque projet Github, on crée les trois secrets suivants dans le paramétrage du projet : 

- DOCKER_HUB_USERNAME : le nom d'utilisateur Docker Hub
- DOCKER_HUB_REPOSITORY : le nom du projet cible dans Docker Hub
- DOCKER_HUB_TOKEN : le token d'accès

Puis dans l'onglet Actions du projet on crée un nouveau workflow manuel avec le code suivant : 

```yaml
name: Docker Image CI
on:
  push:
    branches: [ master ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Build the Docker image
      run: |
        echo "${{ secrets.DOCKER_HUB_TOKEN }}" | docker login -u "${{ secrets.DOCKER_HUB_USERNAME }}" --password-stdin docker.io
        docker build . --file Dockerfile --tag docker.io/${{ secrets.DOCKER_HUB_USERNAME }}/${{ secrets.DOCKER_HUB_REPOSITORY }}:latest
        docker push docker.io/${{ secrets.DOCKER_HUB_USERNAME }}/${{ secrets.DOCKER_HUB_REPOSITORY }}:latest
```

On *commite* le fichier et on peut le retrouver dans les sources du projet dans **.github/workflows**.

Pour mes cas d'usage, je n'ai que des projets mono-branche et je déploie l'image de la branche **master** de Git dans une version **latest**. Dans le cadre d'un projet conséquent géré en gitflow on aurait un versioning des branches releases et un versioning spécial pour la branche de développement principale.






