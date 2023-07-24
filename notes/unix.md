<!-- title: Des commandes Linux -->

# Shell

Relancer la dernière commande : !!

Relancer la dernière commande en sudo : sudo !!

Template Bash ([source betterdev.blog](https://betterdev.blog/minimal-safe-bash-script-template/))

```shell
#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

usage() {
  cat << EOF # remove the space between << and EOF, this is due to web plugin issue
Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-v] [-f] -p param_value arg1 [arg2...]

Script description here.

Available options:

-h, --help      Print this help and exit
-v, --verbose   Print script debug info
-f, --flag      Some flag description
-p, --param     Some param description
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -f | --flag) flag=1 ;; # example flag
    -p | --param) # example named parameter
      param="${2-}"
      shift
      ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
  [[ -z "${param-}" ]] && die "Missing required parameter: param"
  [[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}

parse_params "$@"
setup_colors

# script logic here

msg "${RED}Read parameters:${NOFORMAT}"
msg "- flag: ${flag}"
msg "- param: ${param}"
msg "- arguments: ${args[*]-}"

``` 

# Les fichiers

All directories will be 775. All files will be 664 except those that were set as executable to begin with

    chmod -R a+rwX,o-w <directory>

# Compression

Compresser en préservant les permissions

    tar cvpzf put_your_name_here.tar.gz .

Compresser en splittant par fichier de 2 Mo

    tar cvzp source/  | split -b 2MiB - backup_part.tgz_

et décompression

    cat backup_part.tgz_* | tar xz

Compression moins efficace mais plus rapide avec LZOP :

    tar --lzop -cvf archive.tar.lzo dossier/
    tar xvf archive.tar.lzo

# Les processus
  
Lister les ports ouverts et l'application :    

    sudo netstat -pntul


Donner accès aux ports réservés (<1024) à un processus exécuté par un utilisateur standard

    setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/python3.9

# Listage

Lister par date de modif du - récent au + récent

    ls -lrth

Lister récursivement par taille ascendante

    find . -type f -exec ls -lSr {} +
    

Lister les plus gros fichiers ou répertoires 

```shell
du -cks * | sort -rn | head

# Lister les 15 plus gros fichiers ou répertoire en excluant des répertoires
du -ah --exclude=mnt --exclude sys --exclude proc | sort -hr | head -n 15
```

# Conversion 

du format HEIF (Apple) vers JPEG

    for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done

# Historique

Vider l'historique de Bash (source [StackOverflow](https://askubuntu.com/questions/191999/how-to-clear-bash-history-completely)) 

    cat /dev/null > ~/.bash_history && history -c && exit


[source](https://serverfault.com/questions/746909/journalctl-stop-following-without-exiting-pager)

```
# ^C after Shift-F does not completely quit
journalctl -u nginx | less -FRSXM
```

# Nvim

Supprimer les configurations 

```shell
rm -rf ~/.config/nvim
rm -rf  ~/.local/share/nvim
rm -rf  ~/.local/state/nvim
rm -rf ~/.cache/nvim
```

Installer [NvChad](https://nvchad.com/)
