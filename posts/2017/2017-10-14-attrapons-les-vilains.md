<!-- title: Attrapons les vilains -->
<!-- categories: Hébergement BSD -->

A la fin de [mon article sur le blocage des attaques de brute
force](/2017/nextcloud-securite/), j'étais resté sur l'envoi quotidien d'un
e-mail avec le log des attaques de la journée, histoire d'avoir une idée de ce
qui s'est passé.<!-- more --> Pour rappel, mon serveur tourne sous OpenBSD et l'outil de
protection contre les attaques est Vilain, un équivalent de Fail2ban sous Linux.
Le log de la journée est fastidieux à lire et j'ai eu envie de construire un
rapport avec les informations suivantes :

- liste des adresses IP bloquées
- répartition horaire des attaques
- top des adresses IP les plus agressives

Après un échange avec [Thuban](http://yeuxdelibad.net), le créateur de Vilain,
nous convenons que Vilain doit rester
[KISS](https://fr.wikipedia.org/wiki/Principe_KISS), qu'il n'est pas souhaitable
de compliquer son code pour générer un rapport. Il est préférable de réaliser le
travail en externe en analysant les logs. C'est ainsi que j'ai écrit
**vilainreport** (une centaine de lignes en Python), qu'on peut lancer
quotidiennement avec une tâche CRON pour recevoir le rapport du jour :

    cat /var/log/vilain | vilainreport | mail -s "Vilain rapport du jour" admin

**vilainreport** est intégré au [dépôt de Vilain sur Framagit](https://framagit.org/Thuban/vilain).

Voici un exemple de rapport généré par *vilainreport*:

    ### Date 2017-10-12
    00:17:00 blacklist IP 156.196.136.52 (ssh)
    01:26:17 blacklist IP 115.249.139.206 (ssh)
    02:31:08 blacklist IP 218.62.64.179 (ssh)
    02:35:16 blacklist IP 91.223.167.69 (ssh)
    02:46:54 blacklist IP 27.102.203.180 (ssh)
    ...

    Probe 'ssh' : 137 attacks

    ### Attacks per probe
    Probe 'ssh': 137 attacks

    ### Hourly repartition
    Hour 00 - 01: 1
    Hour 01 - 02: 1
    Hour 02 - 03: 4
    Hour 03 - 04: 4
    ...

    ### Top attackers
    IP 195.184.191.147 : 6
    IP 81.4.110.104    : 5
    IP 90.63.248.112   : 5
    IP 176.31.126.176  : 5
    ...

Ma configuration personnelle de Vilain est la suivante : je bannis pendant 1
heure toute adresse après sa deuxième tentative erronée de connexion à un de mes
services. Donc un *Top attacker* qui a été banni 6 fois dans la même journée n'a
pas  fait d'erreur de connexion. Il a vraiment l'intention de s'introduire dans
mon serveur. Je pourrais durcir ma configuration pour bannir beaucoup plus d'une
heure mais ça ne m'arrange pas car je partage des documents avec des gens qui
peuvent se tromper une fois ou deux en saisissant leurs identifiants Nextcloud.
J'ai donc décidé de mettre en place une sanction plus dure pour les récidivistes :
les jeter dans un puits sans fond, concrètement, une blackliste définitive au
niveau du pare-feu OpenBSD.

![Prison de Bane](/images/2017/darkknight-prison.jpg)

J'ai appliqué une logique similaire à *vilainreport*. Je réinjecte le rapport
dans un petit shell script **supervilain** qui identifie les récidivistes et les
jette dans le puits, où il resteront... jusqu'au prochain redémarrage du serveur.  

Voici le script en Korn Shell :

``` shell
#!/bin/ksh

if [ $# != 1 ]; then
  echo "Usage: $0 logfile"
  exit 1
fi

file=${1--}
while read line
do
  line=`echo $line | tr -d '\r'`
  if [[ $line = IP* ]]; then
    ipend="${line##+(IP )}"
    ip="${ipend%%+( ):*}"
    count="${ipend##*\: }"
    if [ "$count" -gt "2" ]; then
      echo "Ban supervilain ${ip} (${count})"
      `pfctl -t supervilain  -T add ${ip}`
    fi
  fi
done <"$file"
```
