<!-- title: Configuration de Fail2Ban -->
<!-- category: Hébergement -->
<!-- tag: planet -->

Après [l'aspect de la
sauvegarde](http://blogduyax.madyanne.fr/deploiement-et-sauvegarde.html) je me
suis attaqué à la sécurisation du serveur.<!-- more --> C'est un vaste sujet et on n'est
jamais certain d'être parfaitement protégé : on se documente et on essaie de
parer à l'essentiel. Je recommande cet article publié sur [Mes potes
Geek](https://mespotesgeek.fr/debian-8-jessie-securisation/) qui dresse un
panorama des outils couramment utilisés et leur mise en oeuvre. Un des piliers
de la sécurisation d'un serveur GNU/Linux est l'outil
[Fail2Ban](http://www.fail2ban.org) qui va surveiller les logs du serveur pour
trouver des traces d'attaque et contre-attaquer en bannissant le malotru.

Techniquement, l'outil parse les logs systèmes ou applicatifs à grand coup
d'expressions régulières et bloque les attaques avec le pare-feu
[iptable](https://fr.wikipedia.org/wiki/Iptables). Les règles de bannissement
sont configurables : nombre de tentatives de connexions infructueuses, durée du
bannissement. On peut facilement étendre Fail2Ban pour ajouter la  surveillance
d'une application *maison* pour peu qu'elle écrive dans un log les tentatives
ratées de connexion et on peut aussi personnaliser les notifications. En
standard, Fail2Ban envoie un e-mail à l'administrateur à chaque *ban*. En
pratique, un petit serveur comme le mien bannit une quinzaine d'adresses IP par
jour, essentiellement des tentatives ratées par SSH et c'est vite fastidieux de
recevoir autant d'e-mails. Fail2Ban propose un envoi groupé, c'est à dire qu'il
regroupe un nombre d'attaques paramétrable dans un seul e-mail. C'est mieux
mais je suis habitué à configurer mes outils pour recevoir des rapports à
fréquence fixe, journaliers ou hebdomadaires. N'ayant rien trouvé en standard,
j'ai décidé d'étendre Fail2Bane avec mon propre script de configuration pour
arriver au résultat voulu.

Sur Debian, la configuration est installée sous **/etc/fail2ban**. Dans ce
répertoire, on va trouver */etc/failban/filter.d/* qui contient les filtres de
détection et */etc/fail2ban/action.d/* qui contient les actions à appliquer.
Le fichier de configuration principal est *jail.conf* mais on ne le modifie
jamais (pour éviter de perdre les modifications lors des mises à jour de
fail2ban). On préfère redéfinir les parties de la configurations modifiées dans
un fichier *jail.local*. Pour rajouter une action personnalisée, on va donc
rajouter un fichier d'action dans */etc/fail2ban/action.d* et décrire quand et
comment l'appliquer dans *jail.local*.

J'ai donc dupliqué le fichier d'action *sendmail-buffered* et je l'ai adapté
pour créer *sendmail-cron*. Pourquoi CRON ? Et bien l'idée est la suivante :
chaque bannissement est écrit dans un fichier temporaire par
*sendmail-buffered* et quand le nombre de ligne configuré est atteint, ce
fichier est envoyé par e-mail. Je conserve ce fonctionnement mais je change le
déclencheur de l'envoi : ce n'est plus le nombre de lignes du fichier mais la
présence d'un fichier *mail.flag* dans un certain répertoire qui conditionne
l'envoi. Ce fichier *mail.flag* est créé par une tâche CRON. Ainsi, on délègue
à CRON la configuration de la fréquence d'envoi du rapport.

Quant au fichier d'action, il est simple : on conserve les IP bannies dans un
fichier temporaire avec le détail de l'opération (date de l'attaque, filtre
concerné, IP source) et on regarde si on a le feu vert pour créer le rapport en
testant la présence du fichier *mail.flag*. Si c'est le cas, on envoie le
rapport puis on supprime le fichier temporaire et le fichier *mail.flag*. Voici
le fichier */etc/fail2ban/action.d/sendmail-cron.conf* complet :

```
    # Fail2Ban configuration file
    #
    # Author: Yannic Arnoux
    #         Based on sendmail-buffered written by Cyril Jaquier
    #
    #

    [INCLUDES]

    before = sendmail-common.conf

    [Definition]

    # Option:  actionstart
    # Notes.:  command executed once at the start of Fail2Ban.
    # Values:  CMD
    #
    actionstart = printf %%b "Subject: [Fail2Ban] <name>: started on `uname -n`
                  From: <sendername> <<sender>>
                  To: <dest>\n
                  Hi,\n
                  The jail <name> has been started successfully.\n
                  Regards,\n
                  Fail2Ban" | /usr/sbin/sendmail -f <sender> <dest>

    # Option:  actionstop
    # Notes.:  command executed once at the end of Fail2Ban
    # Values:  CMD
    #
    actionstop = if [ -f <tmpfile> ]; then
                     printf %%b "Subject: [Fail2Ban] Report from `uname -n`
                     From: <sendername> <<sender>>
                     To: <dest>\n
                     Hi,\n
                     These hosts have been banned by Fail2Ban.\n
                     `cat <tmpfile>`
                     \n,Regards,\n
                     Fail2Ban" | /usr/sbin/sendmail -f <sender> <dest>
                     rm <tmpfile>
                 fi
                 printf %%b "Subject: [Fail2Ban] <name>: stopped  on `uname -n`
                 From: Fail2Ban <<sender>>
                 To: <dest>\n
                 Hi,\n
                 The jail <name> has been stopped.\n
                 Regards,\n
                 Fail2Ban" | /usr/sbin/sendmail -f <sender> <dest>

    # Option:  actioncheck
    # Notes.:  command executed once before each actionban command
    # Values:  CMD
    #
    actioncheck =

    # Option:  actionban
    # Notes.:  command executed when banning an IP. Take care that the
    #          command is executed with Fail2Ban user rights.
    # Tags:    See jail.conf(5) man page
    # Values:  CMD
    #
    actionban = printf %%b "`date`: <name> ban <ip> after <failures> failure(s)\n" >> <tmpfile>
                if [ -f <mailflag> ]; then
                    printf %%b "Subject: [Fail2Ban] Report from `uname -n`
                    From: <sendername> <<sender>>
                    To: <dest>\n
                    Hi,\n
                    These hosts have been banned by Fail2Ban.\n
                    `cat <tmpfile>`
                    \n,Regards,\n
                    Fail2Ban" | /usr/sbin/sendmail -f <sender> <dest>
                    rm <tmpfile>
                    rm <mailflag>
                fi

    # Option:  actionunban
    # Notes.:  command executed when unbanning an IP. Take care that the
    #          command is executed with Fail2Ban user rights.
    # Tags:    See jail.conf(5) man page
    # Values:  CMD
    #
    actionunban =

    [Init]

    # Default name of the chain
    #
    name = default

    # Default temporary file
    #
    tmpfile = /var/run/fail2ban/tmp-mail.txt

    # Default flag file
    #
    mailflag = /var/run/fail2ban/mail.flag
```

Dans mon cas, la tâche CRON est journalière :

``` shell
# fail2ban report
@daily touch /var/run/fail2ban/mail.flag
```

Ceux qui suivent ont remarqué que mon rapport ne sera envoyé que sur un
bannissement donc potentiellement longtemps après que la tâche CRON ait créé le
fichier *mail.flag*. Je fais confiance à mes intrus et à leurs tentatives
soutenues pour que ce rapport soit bien envoyé à une fréquence journalière ;-)

Il reste à configurer fail2ban pour utiliser cette nouvelle action. J'ai
redéfini dans ma configuration *jail.local* les actions à appliquer sur
détection d'attaque : d'abord on bloque, ensuite on informe :

    action_mwlc = %(banaction)s[name=%(__name__)s, port="%(port)s",
          protocol="%(protocol)s", chain="%(chain)s"]%(mta)s-cron[name=%(__name__)s,
          dest="%(destemail)s", logpath=%(logpath)s, chain="%(chain)s", sendername="%(sendername)s"]
    action = %(action_mwlc)s

Il reste à redémarrer Fail2Ban et à attendre l'envoi du prochain rapport.

Au fait, je reviens à peine de vacances où j'ai rencontré un postulant au rôle de mascotte de ce blog :D

![poulet](/images/2015/poulet.jpg)
