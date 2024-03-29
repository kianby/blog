<!-- title: Problème de résolution avec Xorg -->
<!-- category: GNU/Linux -->

Il arrive que la résolution native de mon écran 1280x800 ne soit pas reconnue
au démarrage. X démarre en 1024x768.<!-- more --> Il y a plusieurs façons de résoudre le
problème : on peut créer un fichier de configuration Xorg.conf ou bien
rajouter le mode dynamiquement. J'ai privilégié la seconde option. La commande
gtf permet de calculer les bons paramètres en fonction d'une résolution et
d'un taux de rafraîchissement :

```shell
$ gtf 1280 800 60
# 1280x800 @ 60.00 Hz (GTF) hsync: 49.68 kHz; pclk: 83.46 MHz
Modeline "1280x800_60.00"  83.46  1280 1344 1480 1680  800 801 804 828  -HSync +Vsync
```

Le résultat peut être passé à la commande xrandr pour ajouter le mode
dynamiquement. Voici le script complet à exécuter au démarrage :

```shell
xrandr --newmode "1280x800_60.00"  83.46  1280 1344 1480 1680  800 801 804 828  -HSync +Vsync
xrandr --addmode LVDS1 "1280x800_60.00"
xrandr --output LVDS1 --mode "1280x800_60.00"
```

Le nom de l'écran de sortie (LVDS1 dans mon cas) est donné par xrandr qui
résume la configuration.
