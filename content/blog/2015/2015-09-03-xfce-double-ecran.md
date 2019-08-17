---
layout: post
title: Configuration de XFCE avec deux écrans
category: GNU/Linux
tag: planet
---

J'ai un portable fraîchement installé sous Debian Jessie avec l'environnement
de bureau XFCE<!-- more --> que j'utilise soit en itinérance, soit en poste fixe avec un
moniteur externe en configuration *double écran*. La configuration brute des
écrans sous GNU/Linux passe par l'utilisation de la commande **xrandr** pour
définir leur nombre, la résolution de chacun et leur position respective. Pour
se faciliter la vie, on peut installer **arand** qui fournit une interface
pour définir ces réglages et les sauvegarder sous forme de shell script dans
un fichier.

Voici une capture d'écran de arandr :

![alt text](/images/2015/arandr.png "Arandr")

Et un exemple de script généré pour une configuration en double écran avec le
moniteur externe à droite de l'écran LCD du portable :

    xrandr --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal
          --output DP1 --off --output VGA1 --mode 1920x1080 --pos 1366x0 --rotate normal

En utilisant arand je vais facilement générer les deux scripts dont j'ai besoin :

- une configuration simple avec l'écran du portable
- une configuration en double écran

Pour savoir lequel appliquer, on va tester si le moniteur externe est connecté
en analysant le résultat de la commande xrandr. Au démarrage du portable, le
gestionnaire de connexions **lightdm** clone l'affichage des deux moniteurs
connectés. On peut corriger cela en appliquant notre joli script qui teste si
le moniteur externe est connecté et applique la bonne commande xrandr. Pour
cela, on édite le fichier de configuration **/etc/lightdm/lightdm.conf** et on
ajoute la directive *display-setup-script* dans la section SeatDefaults :

    [SeatDefaults]
    ...
    display-setup-script=/usr/local/bin/lightdm-monitor.sh

et voici le script **lightdm-monitor.sh** :

``` shell
if (xrandr | grep "VGA1 disconnected"); then
    xrandr --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 0x0 \
            --rotate normal --output DP1 --off --output VGA1 --off
else    
    xrandr --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 0x0 \
            --rotate normal --output DP1 --off --output VGA1 \
            --mode 1920x1080 --pos 1366x0 --rotate normal
fi
```

Le réglage est valable pour lightdm mais quand on ouvre une session XFCE, il
est perdu et on revient à la configuration par défaut à savoir l'affichage
cloné sur les deux écrans. On pourrait appliquer le même script pour la
session, en utilisant la directive *session-setup-script* prévu par ligthdm ou
en mettant le script en démarrage automatique dans la configuration **Session
et démarrage** de XFCE. Dans mon cas, je souhaite ajouter quelque chose au
script de session : déplacer le tableau de bord XFCE sur le moniteur externe,
quand il connecté. C'est possible grâce à la commande **xfconf-query** (le
programme en ligne de commande de configurationde XFCE) adéquate.

Finalement, cela donne le script **xfce-monitor.sh** au démarrage de la session:

``` shell
sleep 3
if (xrandr | grep "VGA1 disconnected"); then
    xrandr --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 0x0 \
            --rotate normal --output DP1 --off --output VGA1 --off
    xfconf-query -c xfce4-panel -p /panels/panel-1/output-name -s LVDS1
else    
    xrandr --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 0x0 \
            --rotate normal --output DP1 --off --output VGA1 \
            --mode 1920x1080 --pos 1366x0 --rotate normal
    xfconf-query -c xfce4-panel -p /panels/panel-1/output-name -s VGA1
fi
```

Le *sleep* en début de script n'est pas élégant. Sans lui, l'exécution du
script intervient avant que la session XFCE soit initialisée et les commandes
xfconf-query ne sont pas appliquées. Si quelqu'un a une solution plus
élégante, je suis intéressé.

Si la connexion / déconnection des écrans a lieu pendant qu'une session est
ouverte, il suffit de relancer le script depuis un terminal pour reconfigurer
l'affichage.

![XFCE](/images/2015/xfce.png)
