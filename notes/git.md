<!-- title: Les commandes de Git -->

# Git

Pousser nouvelle branche :

    git push -u origin <nom branche>

Lier branche locale à branche distante :

    git branch --set-upstream-to=origin/deployment deployment

Fusion sans fast-forward pour préserver les commits :

    git merge --no-ff <source branch>

Créer une nouvelle branche à partir d'un commit :

    git checkout <id de commit> && git branch -b <nom de la branche>

Annuler des changements :

    # committer l'annulation d'un commit : 
    git revert <id de commit>

    # restaurer l'état d'un fichier par rapport au dernier commit 
    git checkout -- <chemin du fichier>

    # annuler le dernier commit pour un fichier particulier (n° de checkout + ~1 pour reculer d'un commit)
    git checkout c5f567~1 -- file1/to/restore

Retrouver les branches qui contiennent un commit :

    git branch --contains <id de commit>

Récupérer toutes les branches localement :

    # ne pas récupérer les branches supprimées
    git fetch --prune

    # créer toutes les branches
    for BRANCH in $(git branch -a | grep remotes | grep -v HEAD); do git branch --track \"${BRANCH#remotes/origin/}\" \"${BRANCH}\"; done

Rechercher dans toutes les branches :

    git grep "the magic string" `git show-ref --heads`
    git rev-list –all | xargs git grep -F "the magic string"

La plupart des commandes peuvent être restreintes à un chemin de fichier :

    git stash push -- <filepath(s)>
    git diff <id commit 1> <id commit 2> -- <filepath(s)>

La gestion des stash :

    # voir le contenu d'un stash (0 est le plus récent)
    git stash show -p [stash@{<n>}]

    # appliquer un stash sans le supprimer
    git stash apply [stash@{<n>}]

    # mettre en stash les fichiers indexés en les conservant
    git stash push --keep-index -m "message"
 

Récupérer un fichier d'une autre branche :

    git checkout <branch> -- <path(s)>

Travailler sur plusieurs branches à la fois (pour comparer par exemple) :

    git worktree add ../my-other-awesome-feature my-other-awesome-feature-branch
    git worktree remove ../my-other-awesome-feature

Supprimer une branche distante

    git push origin --delete <remote_branch>

Lister les commits manquants sur la branche release par rapport à develop

    # depuis branche release
    git cherry develop
    git log release..develop
    # la version one-liner
    git log --oneline --graph --decorate --abbrev-commit release..develop

Créer un patch à partir du dernier commit 

    git format-patch -1 HEAD

Créer un patch à partir d'un id de commit

    git format-patch -1 <sha>

Créer un patch à partir d'une suite de commits consécutifs

    git format-patch cc1dde0dd^..6de6d4b06 --stdout > foo.patch

Extraire un diff d'un commit 

    git diff <sha>^ <sha> > stash.diff

Restaurer un fichier pendant une phase de merge

    git checkout -m FILE

Modifier l'historique des auteurs / e-mails avec git-filter-repo

    git filter-repo --mailmap my-mailmap

    # ficher my-mailmap de la forme : 
    # Proper Name <proper@email.xx> <commit@email.xx>

Créer un nouveau dépôt à partir de la ligne de commande

    echo "# test" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:user/project.git
    git push -u origin main

Pousser un dépôt existant depuis la ligne de commande

    git remote add origin git@github.com:user/projectgit
    git branch -M main
    git push -u origin main

Modifier la racine d'un dépôt

On peut modifier la racine pour un répertoire enfant sans perdre l'historique :

- déplacer le répertoire .git vers ce répertoire enfant
- ajouter tous les fichiers modifiés (git add) ce qui renomme les fichiers existants
- committer et pousser

Transformer un id long de commit en id court

    git rev-parse --short d40f13c5886a8f44e7653f68829dd094045a5499

Annuler un rebase avec reflog

```
$ git reflog

b710729 HEAD@{0}: rebase: some commit
5ad7c1c HEAD@{1}: rebase: another commit
deafcbf HEAD@{2}: checkout: moving from master to my-branch
...

$ git reset HEAD@{2} --hard
```


# GitHub

Générer un Personal Access Token pour les accès HTTPS

    git config --global credential.https://github.com.helper cache

    git credential approve <<EOF
    protocol=https
    host=github.com
    username=$GITHUB_USERNAME
    password=$GITHUB_TOKEN
    EOF

