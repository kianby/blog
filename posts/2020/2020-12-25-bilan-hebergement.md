<!-- title: Bilan hébergement 2020 -->

<!-- category: Hébergement -->

Voici l'état de l'hébergement et un récapitulatif des changements survenus pendant l'année. Mon serveur est toujours un VPS de [Contabo](https://contabo.com/en/vps/) mais je suis passé au modèle supérieur avec 400 Go de disque SSD. Après plusieurs années d'installations hybrides avec une partie des services conteneurisés et une partie installée par le gestionnaire de paquets du système, j'ai profité du changement de serveur pour réaliser une installation 100% docker avec [Traefik](https://doc.traefik.io/traefik/) dans le rôle de *reverse proxy* et gestionnaire des certificats SSL Let's Encrypt, le tout propulsé par une [Devuan](https://www.devuan.org/).

Mes services hébergés restent essentiellement les mêmes : 

- l'excellent [Wallabag](https://wallabag.org) pour lire en différé mes articles rencontrés au détour d'une recherche,
- le fidèle [Selfoss](https://selfoss.aditu.de/) pour lire mes flux RSS,
- l'incontournable [Shaarli](https://sebsauvage.net/wiki/doku.php?id=php:shaarli) qui stocke mes favoris,
- j'ai opté pour le svelte [Baïkal](https://www.baikal-server.com/) pour synchroniser les contacts et les tâches,
- j'auto-héberge le très performant [Seafile](https://www.seafile.com) pour mes données et il est secondé par un modeste abonnement chez [Cozy Cloud](https://cozy.io) pour bénéficier de leurs services numériques,
- ma gallerie de photos est gérée avec brio par [PiGallery2](https://bpatrik.github.io/pigallery2/),  
- j'ai récemment installé un wiki semi-publique (ou semi-privé selon les points de vue) propulsé par le vénérable [DokuWiki](https://www.dokuwiki.org/dokuwiki),
- j'ai repris le contrôle de mes e-mails avec la gestion à portée de tous proposée par [poste.io](https://poste.io/), 
- enfin l'incontournable blog est généré par un dérivé de [makesite.py](https://github.com/fspaolo/makesite) et mon système de commentaires [Stacosys](https://github.com/kianby/stacosys) 

Bonnes fêtes de fin d'année. 

/Yax



