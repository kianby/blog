<!-- title: Rester discret sur GitHub -->
<!-- category: Développement -->

C'est un peu l'article complémentaire [à celui de Korben](https://korben.info/trouver-adresses-emails-utilisateurs-github.html) qui explique comment joindre les contributeurs de projets en retrouvant l'adresse e-mail de leurs commits. Si on est un utilisateur lambda qui utilise GitHub pour ses projets personnels, on n'a pas forcément envie que notre e-mail soit récupéré par des bots pour nous spammer.

Heureusement, c'est prévu par la plateforme et cela demande très peu de configuration.

![github-email-settings](/images/2021/github-email-settings.png)

En cochant la case "Keep my email adresses private", on nous attribue une adresse *somebody@users.noreply.github.com* qu'il reste à configurer dans notre client Git.

    git config user.email somebody@users.noreply.github.com

Et le tour est joué :-)
