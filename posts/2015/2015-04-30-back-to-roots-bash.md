<!-- title: Back to roots, BASH -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

Quand on utilise un système GNU/Linux ou BSD quotidiennement, même si on n'est
pas un accro de la ligne de commande, on n'échappe pas à l'utilisation du
terminal<!-- more --> pour certaines tâches non graphiques. Le choix du shell, comme le
choix d'une distribution est question de goût personnel : les deux principaux
shell, BASH et ZSH ont chacun leurs supporters. Si vous utilisez un terminal
occasionnellement (qui a dit sous la contrainte) il y a fort à parier que vous
utilisez le shell proposé par la distribution, probablement **BASH** dans une
configuration standard qui vous convient tout à fait. Néanmoins, il est
intéressant de personnaliser la configuration de son shell pour se l'approprier.
C'est *fun à réaliser* et cela donne envie de faire plus de choses depuis le
terminal.

![un barbu](/images/2015/stallman-code.jpg#right) Bon si dans quelques mois, les annonces de sortie du nouveau KDE ou Gnome vous font ricaner, que vous ne jurez que par
[Awesome](http://awesome.naquadah.org),
[Rxvt](http://sourceforge.net/projects/rxvt) et
[Tmux](http://tmux.sourceforge.net), vous êtes au bout du chemin, peut-être un
peu trop loin d'ailleurs et vos contacts IRC ont tous une forte pilosité ;-)

### Le prompt PS1

Le prompt est l'invite répétée en début de ligne, entre chaque commande, un
truc du genre **bob@montux >**. Le prompt est porté par la variable PS1 dans le
fichier de config BASH de chaque utilisateur (~/.bashrc). En fonction des goûts
là encore, le prompt peut être synthétique et court ou afficher le maximum
d'informations et prendre une ligne entière. Le site
[Bashrcgenerator.com](http://bashrcgenerator.com) propose un générateur de
prompt par drag and drop qui couvre une petite partie de ce qui est possible.
On peut ajouter des codes ANSI pour coloriser certaines informations. [La doc
ArchLinux est exhaustive sur ces
codes](https://wiki.archlinux.org/index.php/Color_Bash_Prompt).  Il ne faut pas
oublier de réinitialiser la couleur en fin de prompt pour que ça ne coule pas
sur le reste de la ligne avec un reset. je suis adepte des prompts concis :

```shell
White='\e[0;37m'        # White
Red='\e[0;31m'          # Red
Reset=$(tput sgr0)
PS1="\[$White\]\u:\[$Red\]\w\[$White\] \$\[$Reset\] "
```

Pour des prompts plus sophistiqués, on peut utiliser des fonctions shell pour
ajouter des informations dynamiques en fonction du contexte, les infos GIT dans
le contexte d'un répertoire de source par exemple, la charge CPU, l'état de la
batterie. [Le projet LiquidPrompt](https://github.com/nojhan/liquidprompt) en
est un parfait exemple facile à configurer.

### Les alias et les fonctions

les alias sont des substitutions de commandes. On peut les utiliser pour éviter
de mémoriser des paramètres compliquées en définissant de nouvelles commandes :

```shell
alias la='ll -A'    # 'la' : voir les fichiers cachés
alias lk='ls -lSr'  # 'lk' : trier par taille
```

Ou bien on peut redéfinir le comportement d'une commande en créant un alias du
même nom forçant des paramètres :

```shell
# forcer une demande de confirmation pour éviter les boulettes
alias rm='rm --interactive --verbose'
alias mv='mv --interactive --verbose'
```

Quant aux fonctions, elles permettent de définir des commandes en langage shell
directement dans le fichier .bashrc. On peut facilement abuser de cette
possibilité et alourdir le fichier avec des commandes qu'on utilise une fois
l'an. Dans ce cas, il est préférable de les sortir et de créer des fichiers
exécutables accessibles dans le PATH (/usr/local/bin au hasard).

Voici les deux fonctions que j'utilise assez régulièrement :

```shell
function bak() { cp "$1" "$1_`date +%Y-%m-%d_%H-%M-%S`" ; }

function extract()      # Handy Extract Program
{
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)   tar xvjf $1     ;;
            *.tar.gz)    tar xvzf $1     ;;
            *.bz2)       bunzip2 $1      ;;
            *.rar)       unrar x $1      ;;
            *.gz)        gunzip $1       ;;
            *.tar)       tar xvf $1      ;;
            *.tbz2)      tar xvjf $1     ;;
            *.tgz)       tar xvzf $1     ;;
            *.zip)       unzip $1        ;;
            *.Z)         uncompress $1   ;;
            *.7z)        7z x $1         ;;
            *)           echo "'$1' cannot be extracted via >extract<" ;;
        esac
    else
        echo "'$1' is not a valid file!"
    fi
}
```

### Les couleurs de LS

[dircolors](http://linux.die.net/man/1/dircolors) est une commande qui permet
d'afficher le résultat de la commande **ls** en couleur. La plupart des config
bashrc testent si dircolors est présent et l'utilise en rajoutant --color à
ls par le biais d'un... alias (bravo à ceux qui n'ont pas lâché). Généralement,
on a une section de ce genre dans notre .bashrc :

```shell
# enable color support of ls
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
fi
```

Si vous avez une section de ce genre, vos commande ls sont déjà colorisées.
Mais le choix des couleurs et le style est configurable en exportant une
variable **LS_COLORS**. Son format est une liste séparée par des
':'. Chaque élément définit la couleur et l'effet d'un type de fichier ou d'une
extension.

Les types de fichiers :

- no  NORMAL, NORM    Global default, although everything should be something
- fi  FILE    Normal file
- di  DIR Directory
- ln  SYMLINK, LINK, LNK  Symbolic link. If you set this to ‘target’ instead of a numerical value, the color is as for the file pointed to.
- pi  FIFO, PIPE  Named pipe
- do  DOOR    Door
- bd  BLOCK, BLK  Block device
- cd  CHAR, CHR   Character device
- or  ORPHAN  Symbolic link pointing to a non-existent file
- so  SOCK    Socket
- su  SETUID  File that is setuid (u+s)
- sg  SETGID  File that is setgid (g+s)
- tw  STICKY_OTHER_WRITABLE   Directory that is sticky and other-writable (+t,o+w)
- ow  OTHER_WRITABLE  Directory that is other-writable (o+w) and not sticky
- st  STICKY  Directory with the sticky bit set (+t) and not other-writable
- ex  EXEC    Executable file (i.e. has ‘x’ set in permissions)
- mi  MISSING Non-existent file pointed to by a symbolic link (visible when you type ls -l)
- lc  LEFTCODE, LEFT  Opening terminal code
- rc  RIGHTCODE, RIGHT    Closing terminal code
- ec  ENDCODE, END    Non-filename text
- \*.extension Every file using this extension

les effets :

- 00  Default colour
- 01  Bold
- 04  Underlined
- 05  Flashing text
- 07  Reversetd
- 08  Concealed

Les couleurs :

- 30  Black
- 31  Red
- 32  Green
- 33  Orange
- 34  Blue
- 35  Purple
- 36  Cyan
- 37  Grey

les couleurs de fond :

- 40  Black background
- 41  Red background
- 42  Green background
- 43  Orange background
- 44  Blue background
- 45  Purple background
- 46  Cyan background
- 47  Grey background

Les couleurs suppplémentaires :

- 90  Dark grey
- 91  Light red
- 92  Light green
- 93  Yellow
- 94  Light blue
- 95  Light purple
- 96  Turquoise
- 97  White
- 100 Dark grey background
- 101 Light red background
- 102 Light green background
- 103 Yellow background
- 104 Light blue background
- 105 Light purple background
- 106 Turquoise background

Les couleurs par défaut de **dircolors** sont bien pensées mais je n'aime pas
l'utilisation abusive de l'empâtement gras. Je définis donc la couleur bleue
pour l'affichage des répertoire mais en style non gras, je mets par contre en
gras les répertoire ouverts à tous les vents (avec les droits d'écriture sur le
groupe *other*), et en rouge non gras les fichiers exécutables.

```shell
export LS_COLORS="di=00;34:ow=01;34:ex=00;31"
```

J'espère que ces quelques exemples donnent envie de plonger dans les arcanes du
fichier .bashrc pour l'ajuster à sa sauce et utiliser un peu plus la ligne de
commande. De plus en plus de monde conserve ses fichiers de configuration sur
GIT pour avoir un référentiel rapidement installable sur ses systèmes. C'est
une habitude à laquelle j'ai aussi succombé : j'ai un projet [dotfiles sous
GitHub](https://github.com/kianby/dotfiles).
