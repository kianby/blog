<!-- title: Python et dépendances  -->

<!-- category: Développement -->

J'ai développé,  de longue date, l'habitude d'isoler mes projets Python et leurs dépendances dans des environnements virtuels avec les outils classiques [virtualenv](https://virtualenv.pypa.io) et [pip](https://pip.pypa.io/) et de simplement mettre la liste des dépendances sous gestion de sources après extraction par la commande *pip* suivante : 

    pip freeze >requirements.txt

C'est basique mais cela suffisait à mes besoins car je ne publie pas de paquet sur [Pypi](https://pypi.org/) et hormis le passage de Python 2 à Python 3, je n'avais pas eu besoin de tester le bon fonctionnement d'un projet avec une version spécifique de Python. Mais j'ai récemment été confronté à des problèmes de compatibilité entre le Python 3.7 cible de mon serveur et le 3.9 de mon environnement de développement et j'ai senti la nécessité de maîtriser la version d'exécution donc ne ne pas reposer bêtement sur l'interpréteur installé par la distribution. 

C'est exactement le but de l'outil [pythonz](https://github.com/saghul/pythonz) : installer localement (dans le répertoire *home* de l'utilisateur) des interpréteurs Python compilés à partir des sources.  La page du projet GitHub tient lieu de documentation tant c'est simple à utiliser : 

```bash
$ pythonz install 3.8.7
Extracting Python-3.8.7.tgz
Installed CPython-3.8.7 successfully.
$ pythonz locate 3.8.7
~/.pythonz/pythons/CPython-3.8.7/bin/python3
```

Quant à la gestion des dépendances avec le combo *virtualenv / pip* (ou [pew](https://pypi.org/project/pew/) pour ne manipuler qu'un seul outil), elle souffre d'une grosse limitation : l'impossibilité de distinguer les niveaux de dépendances et d'analyser vraiment ce qui est nécessaire au projet à la lecture du fichier *requirements.txt* car la liste est en rang d'oignons.  Cela complique aussi la montée de version individuelle de chaque paquet.

Fichier *requirements* d'un projet qui nécessite Flask, Peewee, Clize : 

```
attrs==17.3.0
click==6.7
clize==4.0.2
docutils==0.14
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.10
jsonschema==2.6.0
MarkupSafe==1.0
od==1.0
peewee==2.10.2
pika==0.11.2
sigtools==2.0.1
six==1.11.0
Werkzeug==0.12.2
```

J'ai donc décidé de m'investir dans [Poetry](https://python-poetry.org/) l'outil de gestion de projets Python qui a l'ambition de remplacer tous les outils existants pour gérer les dépendances, empaqueter et publier. 

Poetry peut *bootstrap-er* un nouveau projet en créant une arborescence complète pour les sources et les tests unitaires  ou initialiser un projet existant avec la commande *poetry init*. La configuration du projet est conservée dans un fichier *pyproject.toml* qu'on mettra sous gestion de sources. 

En ajoutant mon Python 3.8.7 installé avec *pythonz* dans le PATH, je peux définir l'interpréteur a utiliser avec la commande **env use**. Cela va créer un environnement virtuel pour le projet basé sur cet interpréteur (les commandes s'exécutent toujours à la racine du projet qui contient le fichier de configuration de poetry)  :

```
$ poetry env use 3.8
$ poetry env info

Virtualenv
Python:         3.8.7
Implementation: CPython
Path:           ~/.cache/pypoetry/virtualenvs/blogduyax-1cef7RDQ-py3.8
Valid:          True

System
Platform: linux
OS:       posix
Python:   ~/.pythonz/pythons/CPython-3.8.7
```

On peut ajouter les dépendances nécessaires à l'exécution de notre projet avec la commande **add** et la commande **show --tree** affiche clairement le niveau de dépendance de chaque module :

```
$ poetry add requests
$ poetry add pygments
$ poetry show --tree
pygments 2.7.3 Pygments is a syntax highlighting package written in Python.
requests 2.25.1 Python HTTP for Humans.
├── certifi >=2017.4.17
├── chardet >=3.0.2,<5
├── idna >=2.5,<3
└── urllib3 >=1.21.1,<1.27
```

Poetry gère automatiquement un fichier *poetry.lock* qui fige les dépendances et leurs versions. Il est recommandé de le mettre sous gestion de sources aussi.

On peut exécuter une commande directement dans l'environnement virtuel associé avec la commande **run** ou carrément ouvrir un shell avec **shell**. 

Sous le capot, on sent une réelle complexité (pour la gestion des versions par exemple) mais Poetry gomme cette complexité à l'utilisateur avec un binaire unique, des commandes compréhensibles et une bonne documentation. J'ai seulement effleuré une partie des fonctionnalités ; je n'ai pas abordé l'empaquetage, la publication ou la mise à jour des paquets mais Poetry semble avoir les moyens de ses ambitions d'unifier tous les aspects techniques de gestion d'un projet Python.      
    


