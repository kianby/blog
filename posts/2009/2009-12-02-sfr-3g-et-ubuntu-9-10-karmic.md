<!-- title: SFR 3G et Ubuntu 9.10 Karmic -->
<!-- category: GNU/Linux Mobilité -->

J'ai une clef 3G SFR obtenue pour 1 euro grâce au Pacte SFR (merci à eux) et
j'ai voulu valider qu'elle pouvait fonctionner avec Ubuntu pour le jour où ce
serait nécessaire. <!-- more --> J'ai donc fait le tour de Google et sélectionné parmi ce
qui a été discuté par beaucoup de gens compétents ayant fait la manip avec
des versions précédentes ou d'autres distrib les bonnes étapes pour Karmic.

D'abord il faut installer le paquet usb-modeswitch fourni dans les dépôts
standards (version actuelle 1.0.2-1) :

```shell
sudo apt-get install usb-modeswitch
```

Ensuite, on branche la clef 3G et on constate qu'elle monte comme un
périphérique de stockage et non pas comme un périphérique de communication.
C'est là  que la usb-modeswitch intervient... Cette commande doit être
lancée à chaque branchement de la clef :

```shell
sudo usb_modeswitch --default-vendor 0x19d2 --default-product 0x2000
    --target-vendor 0X19d2 --target-product 0x0052 -s 8 --message-endpoint 0x01
    --message-content 55534243123456782000000080000c85010101180101010101000000000000
```

On peut créer notre connexion mobile à large bande en n'oubliant pas
spécifier le point d'accès slsfr au lieu de websfr et de spécifier
manuellement le DNS 172.20.2.39.

Sur ma configuration c'est suffisant pour se connecter sur le réseau 3G de SFR :-)

Voici les threads du forum Ubuntu où j'ai pioché les infos :

- [http://forum.ubuntu-fr.org/viewtopic.php?id=316220](http://forum.ubuntu-
fr.org/viewtopic.php?id=316220)
- [http://forum.ubuntu-fr.org/viewtopic.php?id=193486](http://forum.ubuntu-
fr.org/viewtopic.php?id=193486)
