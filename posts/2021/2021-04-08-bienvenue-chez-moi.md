<!-- title: Bienvenue chez moi -->
<!-- category: GNU/Linux -->

Je partage de la configuration entre mes installations GNU/Linux, les fameux **dotfiles** pour retrouver ses réglages sur ses différents environnements :  bashrc, vimrc, les multiples fichiers de configuration du répertoire utilisateur. En 2013 j'avais simplement créé un dépôt GitHub pour stocker les fichiers et j'installe les fichiers sur chaque système avec des liens symboliques vers le dépôt Git local. Cela fonctionne mais il est impossible d'avoir une vue d'ensemble des configurations installées et les risques d'erreur sont elevés (j'ai déjà perdu une modification effectuée sur un fichier qui n'était pas *symlinké*). Cela tient à l'organisation même des fichiers dissiminés dans différents répertoire du HOME. A part mettre tout le HOME sous Git... et bien c'est une des solutions proposées par le [Wiki d'ArchLinux DotFiles](https://wiki.archlinux.org/index.php/Dotfiles). Saugrenue de prime abord, ça peut fonctionner en gérant bien la liste des fichiers ignorés mais ça me semble très risqué. 

Par contre, cette même page m'a interessé pour sa liste d'outils de gestion de dotfiles moins archaïques que ma gestion manuelle. J'ai écarté les outils écrits en Python car je jongle entre plusieurs interpréteurs et cela complique l'installation d'un outil qui doit être accessible dans n'importe quelle condition. Et j'ai privilégié les outils proposant une fonctionalité de *template* pour un double avantage : 

- pouvoir stocker sur un dépôt public des configuration contenant des infos sensibles en utilisant des variables dont les valeurs sont conservées sur chaque machine,
- fournir des fichiers avec des parties optionnelles en fonction de la machine cible toujours en jouant avec des variables. Cela permet, par exemple, de produire un bashrc compatible entre ArchLinux et WSL en désactivant certaines parties en fonction de la cible.

Après avoir regardé quelques outils Rust bien documentés mais qui me semblaient très complexes, mon choix s'est finalement porté sur [ChezMoi](https://www.chezmoi.io/) écrit en Golang qui propose toutes les fonctions nécessaires à travers un binaire unique et qui est correctement documenté. ChezMoi propose plusieurs types de fonctionnement sans en imposer aucun et j'ai apprécié cette approche. Puis j'ai puisé les fonctions qui me conviennent :

- stockage des fichiers nativement dans un dépôt Git sous *$HOME/.local/share/chezmoi* qu'on peut pousser manuellement vers un dépôt central (mais il peut aussi gérer le *push* automatiquement).
- gestion des fichiers par copie (mais il sait aussi gérer les liens symboliques)
- possibilité de *templatiser* facilement un fichier de configuration existant en ajoutant au préalable les valeurs des variables dans la config locale hors du dépôt Git *$HOME/.config/chezmoi/chezmoi.toml*

Je n'ai pas encore joué avec le *templating* avancé pour avoir des parties de configuration conditionnelles ou le chiffrement des données sensibles avec GPG, je découvrirai les fonctions avancées au fur et à mesure mais ChezMoi répond à mes besoins. 


