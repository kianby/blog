<!-- title: Jouons avec Awk, Bash et Owncloud -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

Un souci de synchronisation du calendrier entre Owncloud et mon téléphone a
été le prétexte à bidouiller une fonctionnalité de rappel des événements par
e-mail.<!-- more --> Pourquoi des e-mail ? Parce que je suis un fana de ce moyen de
communication, la preuve [ici](http://blogduyax.madyanne.fr/du-nouveau-sur-
pecosys.html) et [là](http://blogduyax.madyanne.fr/srmail.html).

Donc ce que je veux c'est un joli e-mail le lundi matin qui résume mes rendez-
vous de la semaine (description, date et heure) et puis chaque matin au réveil
un e-mail par événement avec le fichier ICS en pièce jointe. [ICS
késako](https://fr.wikipedia.org/wiki/ICalendar) ? Un vieux mais très actuel
standard de description d'un événement reconnu par la plupart des calendriers.
L'intérêt d'avoir le fichier ICS c'est de pouvoir l'ajouter au calendrier
local du téléphone en un clic et de paramétrer le rappel en connaissance de
cause (le matin on a une petite idée de comment va se profiler sa journée).

Plutôt que de coder dans un langage évolué, je me suis amusé à réaliser cela
avec les outils présent en standard sur GNU/Linux (**Awk** et **Bash**) pour
le backend MySQL d'Owncloud. C'est didactique car il est toujours préférable
de privilégier l'accès aux données par une API qui sera plus ou moins bien
maintenue dans le temps par les développeurs que d'attaquer directement la
base de données. D'abord jetons un oeil à structure de la base de donnée
Owncloud.

La table *oc_clndr_calendars* permet de retrouver l'id de calendrier de notre
utilisateur.

    mysql> SELECT * FROM oc_clndr_calendars;
    +----+------------+-------------+-----------+--------+------+---------------+---------------+----------+-----------------------+
    | id | userid     | displayname | uri       | active | ctag | calendarorder | calendarcolor | timezone | components            |
    +----+------------+-------------+-----------+--------+------+---------------+---------------+----------+-----------------------+
    |  1 | yax        | Personnel   | personnel |      1 |  196 |             0 | NULL          | NULL     | VEVENT,VTODO,VJOURNAL |
    +----+------------+-------------+-----------+--------+------+---------------+---------------+----------+-----------------------+

Et la table *oc_clndr_objects* contient les évènements :

    mysql> DESC oc_clndr_objects;
    +--------------+------------------+------+-----+---------------------+----------------+
    | Field        | Type             | Null | Key | Default             | Extra          |
    +--------------+------------------+------+-----+---------------------+----------------+
    | id           | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
    | calendarid   | int(10) unsigned | NO   |     | 0                   |                |
    | objecttype   | varchar(40)      | NO   |     |                     |                |
    | startdate    | datetime         | YES  |     | 1970-01-01 00:00:00 |                |
    | enddate      | datetime         | YES  |     | 1970-01-01 00:00:00 |                |
    | repeating    | int(11)          | YES  |     | 0                   |                |
    | summary      | varchar(255)     | YES  |     | NULL                |                |
    | calendardata | longtext         | YES  |     | NULL                |                |
    | uri          | varchar(255)     | YES  |     | NULL                |                |
    | lastmodified | int(11)          | YES  |     | 0                   |                |
    +--------------+------------------+------+-----+---------------------+----------------+

On peut récupérer les évènements du jour courant avec la requête suivante :

    mysql> SELECT startdate,summary,calendardata FROM oc_clndr_objects WHERE calendarid = 1 AND DATE(startdate) = DATE(NOW()) ORDER by startdate \G;
    *************************** 1. row ***************************
       startdate: 2015-09-14 10:30:00
         summary: Déjeuner avec M.
    calendardata: BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:ownCloud Calendar
    CALSCALE:GREGORIAN
    BEGIN:VEVENT
    UID:95d9221d97
    DTSTAMP:20150914T103206Z
    CREATED:20150913T170426Z
    LAST-MODIFIED:20150914T103206Z
    SUMMARY:Déjeuner avec M.
    DTSTART;TZID=Europe/Paris:20150914T123000
    DTEND;TZID=Europe/Paris:20150914T140000
    LOCATION:
    DESCRIPTION:
    CATEGORIES:
    CLASS:PUBLIC
    END:VEVENT
    END:VCALENDAR
    *************************** 2. row ***************************
       startdate: 2015-09-14 16:15:00
         summary: RV dentiste
    calendardata: BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:ownCloud Calendar
    CALSCALE:GREGORIAN
    BEGIN:VEVENT
    UID:1958bfe4a9
    DTSTAMP:20150914T103134Z
    CREATED:20150914T103134Z
    LAST-MODIFIED:20150914T103134Z
    SUMMARY:RV dentiste
    DTSTART;TZID=Europe/Paris:20150914T181500
    DTEND;TZID=Europe/Paris:20150914T183000
    LOCATION:
    DESCRIPTION:
    CATEGORIES:
    END:VEVENT
    END:VCALENDAR

Les colonnes intéressantes sont :

- *calendarid* pour filtrer les évènements de notre utilisateur Owncloud
- *summary* : le libellé de l'évènement
- *startdate* : la date de début de l'évènement
- *calendardata* : l'évènement au format iCalendar

Ce qu'on veut c'est générer un shell script qui récupère les informations du
jour et envoie un e-mail par évènement avec le fichier ICS en pièce jointe.
L'envoi est réalisé par l'utilitaire **mpack**. Le résultat final espéré pour
notre exemple est ce script :

``` shell
#
STARTDATE="`date -d '2015-09-14 10:30:00-000' '+%a %e %b %R'`"
SUMMARY="Déjeuner avec M."
echo "BEGIN:VCALENDAR" >event.ics
echo "VERSION:2.0" >> event.ics
echo "PRODID:ownCloud Calendar" >> event.ics
echo "CALSCALE:GREGORIAN" >> event.ics
echo "BEGIN:VEVENT" >> event.ics
echo "UID:95d9221d97" >> event.ics
echo "DTSTAMP:20150914T103206Z" >> event.ics
echo "CREATED:20150913T170426Z" >> event.ics
echo "LAST-MODIFIED:20150914T103206Z" >> event.ics
echo "SUMMARY:Déjeuner avec M." >> event.ics
echo "DTSTART;TZID=Europe/Paris:20150914T123000" >> event.ics
echo "DTEND;TZID=Europe/Paris:20150914T140000" >> event.ics
echo "LOCATION:" >> event.ics
echo "DESCRIPTION:" >> event.ics
echo "CATEGORIES:" >> event.ics
echo "CLASS:PUBLIC" >> event.ics
echo "END:VEVENT" >> event.ics
echo "END:VCALENDAR" >>event.ics
mpack -s "$SUMMARY - $STARTDATE" event.ics $1
#
STARTDATE="`date -d '2015-09-14 16:15:00-000' '+%a %e %b %R'`"
SUMMARY="RV dentiste"
echo "BEGIN:VCALENDAR" >event.ics
echo "VERSION:2.0" >> event.ics
echo "PRODID:ownCloud Calendar" >> event.ics
echo "CALSCALE:GREGORIAN" >> event.ics
echo "BEGIN:VEVENT" >> event.ics
echo "UID:1958bfe4a9" >> event.ics
echo "DTSTAMP:20150914T103134Z" >> event.ics
echo "CREATED:20150914T103134Z" >> event.ics
echo "LAST-MODIFIED:20150914T103134Z" >> event.ics
echo "SUMMARY:RV dentiste" >> event.ics
echo "DTSTART;TZID=Europe/Paris:20150914T181500" >> event.ics
echo "DTEND;TZID=Europe/Paris:20150914T183000" >> event.ics
echo "LOCATION:" >> event.ics
echo "DESCRIPTION:" >> event.ics
echo "CATEGORIES:" >> event.ics
echo "END:VEVENT" >> event.ics
echo "END:VCALENDAR" >>event.ics
mpack -s "$SUMMARY - $STARTDATE" event.ics $1
```

Comment fait-on ? On exécute la requête SQL et on la donne à manger à un
script **awk** qui a pour objectif de générer le shell script ci-dessus. Awk a
été inventé pour ce genre de tâche : prendre un fichier en entrée et le
modifier pour créer un fichier en sortie. Le script est assez opaque si on n'a
jamais pratiqué mais l'idée c'est de décrire la structure du document en
entrée (comment distinguer les enregistrements) et de faire correspondre des
traitements à certains enregistrements qu'on identifie par une expression
régulière.

Voci le script awk complet :

``` awk
BEGIN {
    FS="\n"    
    OFS=""
    ORS="\n"
    print "#!/bin/sh"
    print " "
}
# blank lines
/^$/ { next }
# record header
$1 ~ /^\*\*\*\*/ {
    next
}
# summary field
$1 ~ /^[ ]*summary\:/ {
    idx = match($1, /summary\:(.*)/)
    print "SUMMARY=\"" substr($1, idx + 9) "\""
    next
}
# startdate field
$1 ~ /^[ ]*startdate\: / {
    match($1, /startdate\: /)
    print "STARTDATE=\"`date -d '" substr($1, RSTART + RLENGTH) "-000' '+%a %e %b %R'`\""
    next
}
# vcalendar start tag
$1 ~ /^[ ]*calendardata\: / {
    match($1, /calendardata\: /)
    print "echo \"" substr($1, RSTART + RLENGTH) "\" >event.ics"
    next
}
# vcalendar end tag
$1 ~ /^END\:VCALENDAR/ {
    print "echo \"" $1 "\" >>event.ics"   
    print "mpack -s \"$SUMMARY - $STARTDATE\" event.ics $1"
    print ""     
    next
}
# vcalendar body
{            
    print "echo \"" $0 "\" >> event.ics"
}
```

Il ne reste plus qu'à orchestrer tout cela dans un shell script et de
l'appeler par une tâche **cron**. Le script complet gère les rappels du jour
et les rappels pour la semaine à venir. Il est disponible [sur mon compte
GitHub](https://github.com/kianby/owncloud_calremind).
