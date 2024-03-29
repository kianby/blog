<!-- title: Bilan de 6 mois d'auto-hébergement -->
<!-- category: Hébergement -->
<!-- tag: planet -->

Revenu à l'auto-hébergement depuis 6 mois, il est temps de faire un bilan.<!-- more -->
D'abord le domaine est passé de rognac.co.cc à madyanne.fr car [Google a exclu
co.cc](http://www.generation-nt.com/google-spam-phishing-domaine-co-cc-
desindexe-actualite-1229651.html) de son moteur de recherche. Je ne cours pas
après la popularité mais de là à devenir invisible... J'ai donc acheté un
domaine chez [Gandi](http://www.gandi.net/) et j'ai profité du pack Mail offert
pour leur confier mon adresse principale. Suite à de multiples soucis d'ADSL,
j'estime que le mail est trop critique pour être auto-hébergé.

Les principaux attraits de l'auto-hébergement sont :

*    la mise à disposition de ses services quand on est mobilité,
*    la liberté de faire tourner des services atypiques (hors du cadre LAMP ) qui
exigeraient un serveur dédié en hébergement classique,
*    le contrôle de ses données,
*    l'apprentissage de l'administration système.

Aujourd'hui j'héberge [PluXml](http://pluxml.org/) (moteur de blog),
[Piwik](http://fr.piwik.org/) (statistiques sur la fréquentation du blog),
[Tiny Tiny RSS](https://tt-rss.org/) (lecteur de flux RSS),
[Prosody](http://prosody.im/) (Jabber), [Subsonic](http://www.subsonic.org)
(streaming audio), [Shaarli](http://sebsauvage.net/wiki/doku.php?id=php:shaarli)
(partage des favoris), [Minecraft](https://www.minecraft.net/) (limité à 5
utilisateurs simultanés) et ses
[Mods](http://fr.wikipedia.org/wiki/Mod_%28jeu_vid%C3%A9o%29), [Mozilla
Sync](http://docs.services.mozilla.com/howtos/run-sync.html) (synchronisation
Firefox).

Au niveau administration j'apprends peu à peu. Je fais tourner
[logwatch](http://www.debianhelp.co.uk/logwatch1.htm) pour recevoir une analyse
journalière des logs par mail et depuis récemment
[fail2ban](http://www.fail2ban.org) qui scrute les logs et ajoute dynamiquement
des règles au firewall pour bannir des adresses qui tentent des accès non
autorisés. Je suis suffisamment en confiance pour avoir placé le serveur en
pseudo [DMZ](http://fr.wikipedia.org/wiki/Zone_d%C3%A9militaris%C3%A9e_%28inform
atique%29) (car j'ai un plan d'adressage unique) et autoriser un accès SSH à
distance. Bon j'ai aussi un système de sauvegarde à jour en cas de pépin ;-)
