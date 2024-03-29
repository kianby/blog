<!-- title: Surveiller sa ligne ADSL avec Munin -->
<!-- category: Hébergement -->
<!-- tag: planet -->

Je me suis intéressé à la supervisition de ma box ADSL afin de grapher la
bande passante montante et descendante ainsi que les valeurs de bruit et
d'atténuation<!-- more -->, ceci dans le but de vérifier la stabilité des valeurs dans le
temps et de corréler des impressions de dégradation avec des mesures
concrètes.

La première étape nécessite de trouver un protocole fournissant les
informations nécessaires. Etant abonné Orange je suis équipé d'une livebox 2
qui fournit un service [HTTP](http://fr.wikipedia.org/wiki/HTTP) et un service
[TELNET](http://fr.wikipedia.org/wiki/TELNET). Sur l'ancienne génération le
mot de passe du compte root était connu et on pouvait tirer les informations
nécessaires depuis le service TELNET. De ce que j'ai lu dans les forums, le mot
de passe est inconnu sur la nouvelle génération et la seule option reste
l'interface HTTP, pas vraiment le protocole idéal pour de la supervision. Fort
heureusement, un script PERL pour piloter la box a été écrit par
[teebeenator](http://www.forum-orange.com/forums/profile.php?id=29572) et
sympathiquement fourni à la communauté des utilisateurs. Ce script est
téléchargeable [ici](http://www.forum-
orange.com/forums/viewtopic.php?id=32420).

![Munin Logo](/images/06x/munin-logo.png#right) La deuxième étape consiste à choisir un
outil de supervision capable de collecter des valeurs et de créer des graphes,
un outil de la famille [MRTG](http://fr.wikipedia.org/wiki/MRTG) : après un
test de [Cacti](https://www.cacti.net/) qui est un bon outil mais que j'ai jugé
trop complexe par rapport à mon besoin initial, mon choix s'est porté sur
[Munin](http://munin-monitoring.org/) : un outil simple (voire rustique) écrit
en PERL, aucune interface graphique d'administration, une interface Web 1.0
(sans JavaScript) qui présente des graphes à la journée, consolidés à la
semaine, au mois et à l'année générés statiquement en tant qu'images
bitmap. L'installation est triviale et correctement documéntée pour Debian sur
[le Wiki de Munin](http://munin-monitoring.org/wiki/Documentation). Dans mon
cas, je déploie sur mon petit serveur Debian Squeeze et j'utilise
[NginX](http://fr.wikipedia.org/wiki/Nginx) en tant que serveur HTTP. Faire un
lien symbolique de /var/www/... vers le répertoire www de Munin
(/var/cache/munin/www) est suffisant pour lier le serveur Web à Munin.

La troisième et dernière étape consiste à étendre Munin en créant des
plugins. D'abord on collecte les données, c'est réalisé par un shell script
qui appelle le script PERL de teebeenator et qui sauve les donnée dans un
fichier texte. Cette collecte est réalisée toutes les 5 minutes grâce à
CRON.

```shell
perl livebox.pl --user=admin --pass=<VotreMotDePasse>
    -page=infosys_main -v 2>/dev/null | html2text >/adsl_stats.txt
```

Je sauve les données dans un fichier texte car 3 plugins Munin vont les
consommer :

* un plugin qui graphe la bande passante descendante (download) en kb/s
* un plugin qui graphe la bande passante montante (upload) en kb/s
* un plugin qui graphe le bruit montant / descendant ainsi que l'atténuation montante / descendante en dB.

Un plugin est un exécutable (Bash, Perl, Python, ce que vous préférez) qui
doit répondre à deux types de requêtes :

- avec l'argument 'config' il renvoie la configuration du graphe : titre, les
unités, le libellé de chaque variable graphée
- sans argument il renvoie une nouvelle valeur pour chaque variable du graphe.

Voici shell script du plugin adsl_download qui collecte la valeur de la bande
passante descendante :

```shell
if [ $# = 1 ]; then
    echo "graph_title Bandwidth - Download"
    echo "graph_category ADSL"
    echo "graph_vlabel kb/s"
    echo "down.label download"
else
    grep "bit descendant maximum" adsl_stats.txt | cut -s -d: -f2
    | sed 's/\s*\([0-9]\+\).*/down.value \1/'
fi
```

L'enregistrement du plugin auprès de Munin est très simple :

-    on rajoute l'exécutable ou un lien symbolique dans /etc/munin/plugins
-    on configure les droits d'exécutions dans /etc/munin/plugin-conf.d/munin-node

Mes plugins s'appellent adsl_download, adsl_upload et adsl_noise, j'ai donc
rajouté la section suivante à /etc/munin/plugin-conf.d/munin-node :

```
[adsl*]
user root
```

Le séquenceur de Munin appelle chaque plugin toutes les 5 minutes.

Voici le genre de graphe qu'on obtient :

![ADSL Download](/images/06x/download.png)

L'ensemble des fichiers qui composent les plugins sont disponibles [dans cette
archive](/documents/munin.zip).
