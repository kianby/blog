<!-- title: Github, CI et jolis badges -->
<!-- category: Développement -->

Dans le prolongement du dernier article sur [Github Actions](https://blogduyax.madyanne.fr/2021/github-et-docker/), j'ai enrichi l'intégration continue du projet [Stacosys](https://github.com/kianby/stacosys) avec un workflow classique : l'exécution des tests unitaires et le calcul de la couverture de code testée. 

Fichier *.github/workflows/pytest.yaml* :

```yaml
name: pytest
on: push

jobs:
  ci:
    strategy:
      fail-fast: false
      matrix:
        python-version: [3.9, 3.9.6]
        poetry-version: [1.1.7]
        os: [ubuntu-18.04, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Run image
        uses: abatilo/actions-poetry@v2.0.0
        with:
          poetry-version: ${{ matrix.poetry-version }}
      - name: Install dependencies
        run: poetry install
      - name: Pytest and Coverage
        run: |
          poetry run coverage run -m --source=stacosys pytest tests
          poetry run coverage report        
      - name: Send report to Coveralls
        run: poetry run coveralls
        env:
          COVERALLS_REPO_TOKEN: ${{ secrets.COVERALLS_REPO_TOKEN }}
```

Le workflow est exécuté à chaque push sur n'importe quelle branche. On définit une matrice des variations qu'on veut tester : 

- les version de Python : je retiens la première 3.9 (GA) et la dernière mineure de la 3.9
- les versions de Poetry, le système de build : la dernière stable me suffit, ce n'est pas Poetry que je teste.
- les systèmes d'exploitation : le tryptique classique Linux / MacOS / Ms Win 

A partir de cette matrice, le workflow va calculer le produit cartésien de tous les environnements de tests et dérouler les actions sur chacun. On s'appuie sur l'action poetry du [marketplace Github](https://github.com/marketplace?type=actions) pour avoir un workflow plus concis et plus lisible :

- exécution des tests avec pytest
- génération du rapport de couverture de code 
- publication du rapport sur la solution Saas [Coveralls](https://coveralls.io/)

Au préalable, on aura activé son compte sur Coveralls en le connectant avec son compte Github et récupéré la valeur du token du repository pour le rajouter aux secret Github sous le nom COVERALLS_REPO_TOKEN. 

A cette étape, on pousse du code pour vérifier que le workflow est exécuté. 

![workflow-pytest](/images/2021/action-pytest.png)

Le rapport de couverture est publié sur Coderwall [ici](https://coveralls.io/github/kianby/stacosys?branch=master). Il permet d'identifier facilement pourquoi on n'a que 65% de couverture de code sur le projet :-) 

![coverage](/images/2021/coverall.png)

La CI est en place, les informations sont présentes mais il faut aller les chercher : l'historique des workflows dans l'onglet Action de Github, la couverture de code sur le site de Coderwall. On va regrouper tout ça dans le fichier README.md qui fait office de page d'accueil du projet en se servant des badges parce que c'est beau et et amusant à réaliser. 

Github produit directement un badge pour la dernière exécution d'un workflow.

```md
[![Build Status - pytest](https://github.com/kianby/stacosys/workflows/pytest/badge.svg)](https://github.com/kianby/stacosys)
```

Et Coderwall fournit le code markdown pour le badge de pourcentage de la couverture de code.

```md
[![Coverage Status](https://coveralls.io/repos/github/kianby/stacosys/badge.svg?branch=master)](https://coveralls.io/github/kianby/stacosys?branch=master)
```

Après j'ai pris goût et je me suis amusé en décrivant visuellement les dépendances principales du projet :

```md
[![Python version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)

[![Flask version](https://img.shields.io/badge/Flask-2.0.1-green.svg)](https://flask.palletsprojects.com)
```

Et j'ai même trouvé un générateur de badge pour la licence du projet :-)

```md
[![GitLicense](https://gitlicense.com/badge/kianby/stacosys)](https://gitlicense.com/license/kianby/stacosys)
```

Le résultat est plutôt sympathique. 

![badges](/images/2021/stacosys-badges.png)