---
layout: post
title: Grub Gfx … j'aurais aimé être un artiste
category: GNU/Linux
---

Je ne suis pas un graphiste, loin de là et me familiariser avec The Gimp et Inkscape fait partie de ma TODO
liste. Un exercice pratique a consisté à personnaliser un splash screen pour
Grub. <!-- more --> J'ai d'abord installé [grub-gfx](http://wiki.archlinux.org/index.php
/Grub-gfx) puis j'ai récupéré ce splash screen minimaliste et sympathique sur
le site [schultz-net](http://www.schultz-net.dk/grub.html).

![Grub](http://www.schultz-net.dk/images/grub/black.gif)

Le but que je me suis fixé est d'ajouter le logo Toshiba en bas à droite. Je suis parti du [logo
Toshiba](http://fr.wikipedia.org/wiki/Fichier:Toshiba_logo.svg) disponible au
format [SVG](http://fr.wikipedia.org/wiki/Svg) sur Wikipedia. Je l'ai chargé
dans Inkscape et je l'ai exporté en bitmap à la taille désirée. Puis j'ai
fait mon assemblage sous Gimp. Enfin j'ai réduit le nombre de couleurs à 14
comme l'impose Gfx par le menu "Image" / "Mode" / "Couleurs indexées" avant de
sauvegarder en XPM.

![My Grub image](/images/01x/my_grub_image.jpg)

Rien de bien sorcier mais je pars de très loin sur le sujet "graphisme"  :-)
Je suis assez content du résultat et surtout je me suis bien amusé.

Pour les possesseurs d'un Toshiba interessés par ce splash screen il est
téléchargeable [ici](/documents/my_grub_image.xpm).
