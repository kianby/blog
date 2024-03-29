<!-- title: Mise à jour de Fedora 17 vers Fedora 18 -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

15 Janvier 2013 : c'est la sortie officielle de la Fedora 18, très attendue car
sa sortie fût décalée plusieurs fois, ce qui est à l'honneur des
développeurs<!-- more --> : sortir quand le niveau de qualité est atteint malgré le fait
qu'on soit une distribution mainstream très attendue. Je vous renvoie à
[l'article très complet posté par Renault sur LinuxFR pour la liste des
nouveautés.](http://linuxfr.org/news/sortie-de-fedora-18-alias-spherical-cow).
Moi je faire un retour d'expérience rapide sur une mise à jour réussie depuis
le Spin XFCE de Fedora 17.

 [FedUp](http://fedoraproject.org/wiki/FedUp) est le nouvel outil pour gérer
les mises à jour de Fedora 17 et ultérieur. Voici les étapes que j'ai suivi
pour mettre à jour ma distribution :

*    s'assurer que le système est à jour : yum upgrade. Puis redémarrer la machine
si le Kernel a été mis à jour.
*    installer FedUp : yum --enablerepo=updates-testing install fedup
*    désactiver tous les dépôts tiers définis tels que RPM Fusion. En ligne de
commande, cela consiste à rajouter enabled=0 aux fichiers.repo que l'on trouve
sous /etc/yum.repos.d.
*    se déconnecter graphiquement et lancer FedUp en tant que root ou avec sudo
depuis un VTY : fedup-cli --network 18 --debuglog fedupdebug.log
*    s'armer de patience, les téléchargements des paquets F18 commencent. Quand
c'est terminé, FedUp demande de redémarrer la machine. C'est au redémarrage
que le processus de mise à jour est effectué. Je ne sais pas exactement
combien de temps cela prend, j'ai dormi ;-)

Si tout se passe bien, on se retrouve avec une Fedora 18 opérationnelle. La
commande **uname -r** indique qu'on est passé en kernel 3.7.2-201.fc18.x86_64.4
Pour être complet, on peut aussi mettre à jour Grub 2 manuellement [comme
indiqué sur la page Wiki de FedUp](http://fedoraproject.org/wiki/FedUp#How_Can_
I_Upgrade_My_System_with_FedUp.3F).

 **[EDIT]** J'ai remarqué que le nouveau pare-feu ne fonctionnait plus même
après l'installation des paquets firewall-config et firewall-applet. Le service
démarre, on peut modifier la configuration mais elle n'est pas prise en compte.
Il semble qu'un coup de **yum -y distro-sync** finalise la mise à jour en
supprimant les paquets obsolètes. Le pare-feu est opérationnel au
redémarrage. Ce nouveau pare-feu mériterait d'ailleurs un article : plus
simple et plus clair à configurer, gestion de 2 configurations (la courante et
la stockée).

Certains paquets obsolètes peuvent rester. Les [conseils de
llaumgui](http://www.llaumgui.com/post/fedora-17-in-da-place) restent
d'actualité.

J'ai aussi eu un problème avec la gestion de l'énergie interceptée par
systemd avant XFCE. C'est résolu dans ce post (lien obsolète : http://comments.gmane.org/gmane.linux.redhat.fedora.general/423516).
