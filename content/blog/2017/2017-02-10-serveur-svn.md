---
layout: post
title: Un serveur SVN en 5 minutes
category: Développement
tag: planet
---

Bien qu'on soit en 2017, on peut avoir besoin d'un gestionnaire de source
centralisé et Subversion reste une valeur sure.<!-- more --> On va donc s'installer un
serveur SVN sur Debian Jessie en 5 minutes chrono.

D'abord on installe SVN et on crée un répertoire pour les données.

    $ apt-get install subversion
    $ mkdir -p /srv/svn/repos

Et on initialise un dépôt (aka *repository*) nommé "yaxsoft".

    $ svnadmin create /svn/repos/yaxsoft

On ajoute des droits d'accès simples : un utilisateur en lecture-écriture, pas
d'accès anonyme.

Editer */srv/svn/repos/yaxsoft/svnserve.conf* :

    [general]
    password-db = passwd
    authz-db = authz
    realm = Yax Repo

Editer */srv/svn/repos/yaxsoft/conf/authz* :

    [groups]
    dev = yannic

    [/]
    * =
    @dev = rw

Editer */srv/svn/repos/yaxsoft/conf/passwd* :

    [users]
    yannic = mon_mot_de_passe

On crée un répertoire pour les logs :

    $ mkdir -p /var/log/svn

On ajoute un utilisateur UNIX *svn* qui va lancer le serveur et aura les
permission sur les fichiers de données :

    $ adduser svn --system --disabled-login --no-create-home --group
    $ chown -R svn:svn /srv/svn /var/log/svn

On crée le fichier avec les paramètres de lancement du service */etc/default/svnserve* :

    DAEMON_ARGS="--daemon --pid-file /srv/svn/svnserve.pid --root /srv/svn/repos --log-file /var/log/svn/svnserve.log"

Enfin, on définit le recyclage des logs avec un fichier */etc/logrotate.d/svn* :

    /var/log/svn/*.log {
        daily
        missingok
        rotate 10
        compress
        notifempty
        create 640 svn svn
        sharedscripts
        postrotate
            if /bin/systemctl status svnserve > /dev/null ; then \
                /bin/systemctl restart svnserve > /dev/null; \
            fi;
        endscript
    }

Il reste à créer un fichier de lancement pour **systemd** : */etc/systemd/system/svnserve.service* :

    [Unit]
    Description=Subversion daemon
    After=syslog.target network.target

    [Service]
    Type=forking
    PIDFile=/srv/svn/svnserve.pid
    EnvironmentFile=/etc/default/svnserve
    ExecStart=/usr/bin/svnserve $DAEMON_ARGS
    ExecReload=/bin/kill -s SIGHUP $MAINPID
    User=svn
    Group=svn
    KillMode=process
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target

Finalement, on met le service en démarrage automatique et on lance notre serveur SVN :

    $ systemctl daemon-reload
    $ systemctl enable svnserve
    $ systemctl start svnserve

Notre SVN est accessible en **svn://mon_serveur/yaxsoft**.
