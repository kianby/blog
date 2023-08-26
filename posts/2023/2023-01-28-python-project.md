<!-- title: Configurer un projet Python -->
<!-- category: Développement -->


En relisant mes articles sur [la configuration de Sublime Text pour développer en Python](https://blogduyax.madyanne.fr/2022/sublime-ide-pour-python/) et [l'utilisation de Poetry](https://blogduyax.madyanne.fr/2020/python-et-dependances/) ils m'apparaissent un peu incomplets et pas assez didactique sur la mise en place initiale pour démarrer un projet. Voici donc un complément à jour des informations distillées par les articles précédents.

D'abord je gère tous mes projets avec [Poetry](https://python-poetry.org/) qui apporte la gestion des dépendances, de l'environnement d'exécution mais aussi de l'empaquetage. je vous recommande la lecture de la documentation de très bonne qualité pour le détail de chaque fonctionnalité. 

La création du projet peut-être réalisée par Poetry par la commande : 

    poetry new nom-du-projet

Cette commande génère le fichier de configuration *pyproject.toml* et un squelette de sources. Partant de là, on peut ajouter des dépendances d'exécution ou de compilation avec des commandes *poetry add* et la résolution des dépendances exerce sa magie. Au préalable, il est judicieux d'avoir une configuration spécifique de Poetry, portée par le projet, pour certains paramètres avancés. 

Ainsi je préfère installer l'environnement d'exécution dans le répertoire du projet plutôt que dans la configuration utilisateur (**~.cache/pypoetry/virtualenvs**), cela simplifie la vie des IDE et ça a plus de sens pour un environnement spécifique à un projet. Pour cela, on exécute la commande suivante :

    poetry config virtualenvs.in-project true --local

Cela a pour conséquence de créer un fichier de configuration *poetry.toml* à la racine du projet ayant précédence sur les autres fichiers de configuration (celui de l'utilisateur et le global du système). 

Pour ne pas être limité aux versions de Python fournies avec votre distribution GNU/Linux, j'utilise un gestionnaire d'interpréteurs Python qui permet d'installer n'importe quelle version. Plusieurs outils de ce type existent, **pyenv** a l'avantage d'être [recommandé par Poetry](https://python-poetry.org/docs/managing-environments#managing-environments) et simple à utiliser : 

```bash
# lister les versions installées
pyenv version 
# installer une nouvelle version Python
pyenv install 3.11.0
# utiliser une version dans le shell courant
pyenv local 3.11.0
```

L'installation des dépendances après activation du bon interpréteur sous réserve qu'il soit compatible avec la version de Python spécifiée dans la configuration du projet *pyproject.toml* devrait initialiser l'environnement virtuel du projet dans le répertoire .venv du projet. Il est de bon ton d'aider Poetry à sélectionner la bonne version en activant le paramètre :   

    poetry config virtualenvs.prefer-active-python true --local

Au final, le ficher de surcharge de la configuration Poetry *poetry.toml* pour le projet est tel que : 

```toml
[virtualenvs]
in-project = true
prefer-active-python = true
```

Et l'activation de l'environnement du projet avec *poetry shell* ou *poetry run* devrait sélectionner le bon interpréteur sans forcer sa version avec *pyenv local* et bien sûr l'environnement virtuel du projet.
