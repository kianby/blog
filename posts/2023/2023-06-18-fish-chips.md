<!-- title: Fish sans chips -->
<!-- category: GNU/Linux -->

Une grande partie de ma vie sur écran se déroulant dans un terminal, [multiplexé de préférence](https://github.com/tmux/tmux), j'ai investi beaucoup de temps au fil des ans à sélectionner et à me former à des outils qui rendent l'expérience plus productive et agréable, ce dernier point ne valant que pour les aficionados de la console. C'est dans ce but que j'ai opté pour Tmux et constitué un lot de compagnons à Bash pour avoir un *prompt* à forte valeur ajoutée et de la navigation rapide avec Fzf. Tout était basé sur ce bon vieux Bourne Again Shell, pas que je sois féru ou doué pour l'écriture de shell scripts, mais parce que c'est le plus standard et que je suis certain de le retrouver partout. Bon Zsh me faisait un peu d'oeil avec sa grosse collection de plugins mais j'avais plus ou moins l'équivalent avec Bash et ses extensions. De temps en temps, je tombais sur une dépêche à propos de [Fish Shell](https://fishshell.com/) que je lisais par curiosité. Le fait que Fish ne suive pas les normes POSIX avait suffit pour que je range ce shell dans le rayon des alternatives exotiques développées par quelques passionnés mais pas assez sérieux pour devenir la pierre angulaire d'un système... après tout le shell c'est l'interface utilisateur principale en mode console.

Et puis, un week-end de désoeuvrement après la lecture d'une énième dépêche concernant Fish, j'ai décidé d'essayer juste pour voir. Première surprise, installé nu c'est-à-dire sans configuration spécifique, il comble plus de la moitié des personnalisations réalisées par Bash et ses copains [Starship](https://starship.rs/), [exa](https://github.com/rivy/rust.exa), [hishtory](https://github.com/ddworken/hishtory). Pris au jeu, j'ai commencé à lire sérieusement la documentation et à essayer de réaliser la moitié manquante avec  une configuration spécifique *config.fish*. j'ai adoré la facilité pour ajouter un déclencheur sur un changement de répertoire comme ici pour faire un *git fetch* et avoir un prompt à jour concernant les modifications de branches distantes : 

```shell
function __git_fetch_after_cd__on_variable_pwd --on-variable PWD
    if test -d .git
        git fetch
    end                    
end 
``` 

Avec moins de lignes de configuration j'ai obtenu un résultat similaire à ma configuration actuelle. J'ai aussi mis en place le gestionnaire de plugins fisher. Facile me direz-vous de réduire la configuration en s'appuyant sur des plugins et pourquoi des plugins si Fish est si... facile à personnaliser ? 

Et bien parce que je ne suis pas un cador : par exemple le choix d'utiliser un alias ou une abbréviation n'est pas encore évident pour moi. Et là où Fish pêche un peu c'est dans l'intégration du monde extérieur. Par exemple Fzf ou sdkman fournissent des shells d'init pour Bash et Fzf mais pas pour Fish. Une partie des plugins Fish installés réalisent l'intégration, parfois en exécutant les scripts Bash et en réexportant les variables nécessaires dans l'environnement Fish, d'autres fois en écrivant la couche d'intégration en Fish shell.

Finalement, une fois la configuration terminée, j'ai défini Fish comme shell par défaut sur deux de mes machines pour l'utiliser au quotidien. L'ensemble de mes configurations est toujours géré par [Chezmoi](https://www.chezmoi.io/) et s'il faut revenir en arrière il suffit de modifier le shell pour réactiver Bash. Pour l'instant je suis ravi.
