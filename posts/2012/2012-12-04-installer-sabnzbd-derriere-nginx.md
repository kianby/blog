<!-- title: Installer SABnzbd derrière Nginx -->
<!-- category: Hébergement -->

[SABnzbd](http://sabnzbd.org/), comme son nom ne l'indique pas vraiment, est un
lecteur de news binaires. <!-- more -->Il permet de récupérer des fichiers depuis
[Usenet](http://fr.wikipedia.org/wiki/Usenet). C'est une application serveur,
qu'on héberge derrière un serveur Web, et qui offre une interface de gestion
depuis un navigateur. Il faut bien sûr l'associer à un compte chez un
fournisseur Usenet. Je ne détaille pas plus l'utilisation de l'outil, le site
officiel est suffisamment documenté, mais plutôt son installation dans le
cadre de l'auto-hébergement avec le serveur Web Nginx en frontal et non pas le
traditionnel Apache.

Depuis [la page de téléchargement](http://sabnzbd.org/download/) on peut
télécharger les sources Python. Les manipulations suivantes sont réalisées
sur une Debian 6 avec Python, Nginx et OpenSSH installés.


```shell
# on installe sous /srv
cd /srv
wget http://sourceforge.net/projects/sabnzbdplus/files/sabnzbdplus/0.7.6/
        SABnzbd-0.7.6-src.tar.gz/download -O SABnzbd-0.7.6-src.tar.gz
tar xvf SABnzbd-0.7.6-src.tar.gz &&  rm -f SABnzbd-0.7.6-src.tar.gz
# on crée un lien symbolique /srv/sabnzbd pour gérer aisément les futures mises à jour
ln -s SABnzbd-0.7.6 sabnzbd
```

L'étape suivante consiste à démarrer SABnzbd pour définir sa configuration
générale et **aussi restreindre l'adresse d'écoute** à l'interface localhost
(127.0.0.1) pour forcer le passage par Nginx et son authentification que nous
allons mettre en place par la suite. On peut automatiser le démarrage en
rajoutant un script sabnzbd sous /etc/init.d tel que celui-ci :

```shell
### BEGIN INIT INFO
# Provides:          sabnzd
# Required-Start:    $local_fs $remote_fs
# Required-Stop:     $local_fs $remote_fs
# Should-Start:      $all
# Should-Stop:       $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop Sabnzbd
# Description:       Start/stop Sabnzbd
### END INIT INFO

PATH=/sbin:/bin:/usr/sbin:/usr/bin

. /lib/lsb/init-functions

if [ "$#" -ne 1 ]; then
  log_failure_msg "Usage: /etc/init.d/sabnzd" \
      "{start|stop}"
  exit 2
fi

case "$1" in
  start)
        python /srv/sabnzbd/SABnzbd.py -d -f /root/.sabnzbd/sabnzbd.ini
  exit $?
  ;;
  stop)
    /usr/bin/wget -q --delete-after "http://localhost:7777/sabnzbd/api?mode=shutdown
                                        &apikey;=24be83f61210daad59aa0e90223ccd4f"
  exit $?
  ;;
  *)
        log_failure_msg "Usage: /etc/init.d/sabnzbd" \
                        "{start|stop}"
        exit 2
        ;;
esac

log_failure_msg "Unexpected failure, please file a bug."
exit 1
```

On active ce script sous Debian avec update-rc.d sabnzbd defaults. Finalement on
configure Nginx comme proxy. Je me suis borné à un accès HTTP protégé par
une authentification utilisateur / mot de passe mais HTTPS est recommandé.

```nginx
server {
    listen 80;
    server_name www.yourserver.yourdomain;
    root /var/www/www;
    access_log /var/log/nginx/www.access.log;
    error_log /var/log/nginx/www.error.log;

    location /sabnzbd {
        auth_basic "Restricted area";
        auth_basic_user_file /var/www/htpasswd;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:7777/sabnzbd;
    }
}
```

Pour la création du fichier d'authentification **htpasswd** je vous renvoie à
la [FAQ de Nginx](http://wiki.nginx.org/Faq#How_do_I_generate_an_htpasswd_file_w
ithout_having_Apache_tools_installed.3F) car plusieurs méthodes sont possibles.
Gare à sécuriser son accès et à le placer hors des répertoires servis par
Nginx. A ce stade SABnzbd fonctionne à moitié :-) En effet SABnzbd ne va pas
servir toutes les ressources (HTML / CSS) et il faut les lier statiquement à
Nginx.

```shell
# on lie les ressources statiques du thème Plush
mkdir -p /var/www/www/sabnzbd
ln -s /srv/sabnzbd/interfaces/Plush/templates/static /var/www/www/sabnzbd/static
ln -s /srv/sabnzbd/interfaces/Config/templates/staticcfg /var/www/www/sabnzbd/staticcfg
```
