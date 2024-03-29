<!-- title: Enfin le silence -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

J'ai effectué la mise à jour de mon *véloce serveur* <i class="icon-smile"></i>
(un Dell latitude D610 sous Céléron) vers Debian Wheezy.<!-- more --> Ca s'est plutôt bien passé
en suivant les conseils de Nicolargo (http://blog.nicolargo.com/2013/05/de-squeeze-a-wheezy.html).
J'ai seulement eu quelques problèmes avec l'interpréteur PERL, je me suis retrouvé
avec un mix : l'interpréteur 5.16.3 de Wheezy et d'anciens modules PERL.
Peut-être que j'avais installé ces librairies manuellement, je ne me souviens
pas trop. Ca c'est résolu avec un ménage à la mano des modules obsolètes et une
réinstallation propre avec CPAN. Désormais, tout est fonctionnel !

Jusqu'à aujourd'hui je limitais la charge processeur la nuit en stoppant
certains services pour éviter la nuisance sonore, typiquement, le serveur
Minecraft en JAVA qui consomme 3% de CPU quand personne n'est connecté.
J'utilise depuis longtemps le paquet **cpufrequtils** qui permet de moduler la
fréquence du processeur par un module du noyau selon une politique **on demand**
qui fait varier la fréquence du Celeron entre 800 Mhz et 1,6 Ghz. Mais j'ai
réalisé que malgré une charge minimale, la machine était souvent bruyante à cause du
ventilateur. Il devrait être régulé en fonction de la fréquence du
processeur, or ce n'est pas le cas.

En faisant des recherches sur le sujet, on
apprend que la partie régulation du processeur est souvent réalisée par ACPI,
une norme répandue de contrôle de la gestion de l'énergie par l'OS grâce à un
support ACPI dans le BIOS mais que la gestion du ventilateur n'est pas souvent
incluse. Cela va dépendre de l'implémentation ACPI d'un constructeur à l'autre.
[La documentation
ArchLinux](https://wiki.archlinux.org/index.php/Fan_Speed_Control) décrit
certaines méthodes qui vont dépendre du matériel et j'ai découvert **i8kmon** pour
mon petit Dell. Ca tourne en daemon dans le système et ça régule la vitesse du
ventilateur proportiennellement à la vitesse du processeur. Pour la
configuration, j'ai utilisé les seuils proposés dans le [post de ce
forum](http://forum.tinycorelinux.net/index.php?topic=10736.0) :

Fichier **/etc/i8kmon** :

```
# Kernel I8K status file
set config(proc_i8k)   /proc/i8k

# Kernel APM status file
set config(proc_apm)   /proc/apm

# Kernel ACPI status file
set config(proc_acpi)   /proc/acpi/ac_adapter/0/status

# External program to control the fans
set config(i8kfan)   /usr/bin/i8kfan

# Applet geometry, override with --geometry option
set config(geometry)   {}

# Run as daemon, override with --daemon option
set config(daemon)   1

# Automatic fan control, override with --auto option
set config(auto)   1

# Report status on stdout, override with --verbose option
set config(verbose)   0

# Status check timeout (seconds), override with --timeout option
set config(timeout)   5

# Temperature display unit (C/F), override with --unit option
set config(unit)   C

# Temperature threshold at which the temperature is displayed in red
set config(t_high)   80

# Minimum expected fan speed
set config(min_speed)   1800

# Temperature thresholds: {fan_speeds low_ac high_ac low_batt high_batt}
# These were tested on the I8000. If you have a different Dell laptop model
# you should check the BIOS temperature monitoring and set the appropriate
# thresholds here. In doubt start with low values and gradually rise them
# until the fans are not always on when the cpu is idle.
set config(0)   { {- 0}  -1  52  -1  52}
set config(1)   { {- 1}  44  60  44  60}
set config(2)   { {- 2}  60  80  60  80}
set config(3)   { {- 2}  70 128  75 128}
```

Fichier **/etc/default/i8kmon**

```
# Change to one to enable i8kmon
ENABLED = 1
```

Le résultat est au rendez-vous. Quand la CPU est basse, le volume sonore de la
machine est inaudible. Il reste à vérifier que les seuils sont adaptés et que
le processeur ne fond pas dans les prochaines semaines <i class="icon-smile"></i>
