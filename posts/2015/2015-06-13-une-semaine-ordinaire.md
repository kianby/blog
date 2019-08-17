<!-- title: Une semaine ordinaire -->
<!-- category: Humeur -->
<!-- tag: planet -->

Toute ressemblance avec des événements réels s'étant déroulés cette semaine
dans ma sphère professionnelle n'est pas fortuite.<!-- more --> La semaine a été riche en
péripéties système et réseau, ce qui me conforte dans l'idée que gérer un
réseau de centaines de machines ça doit pas être facile tous les jours. Fou le
temps qu'on peut déjà passer avec une trentaine en faisant cela en dilettante
puisque mon métier principal c'est développeur.

Orange fournit un service d'adresse de messagerie pour les professionnels avec
une sécurité renforcée. Pour lutter contre le SPAM, ils s'assurent notamment
que les e-mails sont envoyés depuis une machine de confiance. L'envoi d'e-mails
de ma société est devenu erratique depuis mardi. Un message un peu cryptique du
support Orange nous informe que notre IP publique est *sur liste noire* donc
tout le trafic Internet qui sort de nos machines est suspect. Cela explique le
blocage des e-mails par le serveur SMTP Orange Business. Comment en est-on
arrivé à cette situation et comment en sortir ? Un tour sur [ce genre de site
]( http://whatismyipaddress.com/blacklist-check) permet de consulter les sites
de référence des *listes noires* et sur certains de connaître la cause. Dans
notre cas, le trafic Internet d'un virus sortant de notre réseau a été détecté,
ce qui nous a promu au rang de site louche. Pour sortir de cette situation il
faut résoudre le problème (éradiquer les machines infectées)  puis demander à
sortir de la liste noire sur sa bonne foi d'admin. Au bout de 24/48h tout
rentre dans l'ordre.  

Dans un autre registre, je constate que le voisinage réseau des machines Ms
Windows (en Workgroup) est parfois incomplet, ne présentant qu'un sous-ensemble
des machines. Un test depuis différents OS (Windows 7, Windows 2003) me
confirme que ce n'est pas particulier à ma Fedora et sa configuration Samba.
Pour ce que j'en sais, dans un réseau modeste en WORKGROUP, sans controlleur de
domaine, les machines participent à une élection pour élire un *master
browser*, celle qui va fournir la liste du voisinage réseau. Je crains qu'avec
nos machines de test à droite à gauche, on élise parfois une machine qui n'a
pas de visibilité complète sur l'ensemble du réseau. La commande **nmblookup**
des outils SAMBA permet de connaître l'adresse IP du *master browser* en cours,
sachant qu'il change régulièrement :

    nmblookup -S -M -- -.

Comme dans la vie réelle, une solution consiste à influer sur le résultat de
l'élection. C'est possible avec SAMBA et son paramétrage avancé qui lui permet
de concourir à l'élection du *Master Browser* avec une telle réputation qu'il
ne peut qu'être élu par ses pairs. J'ai utilisé un serveur NAS local (NAS4FREE
sous BSD, toujours en ligne) pour ce rôle d'élu. Le voisinage réseau est
désormais complet en toute circonstance.

Pour terminer la semaine en beauté, on me met le nez sur un problème de Wi-Fi
récurrent (et aléatoire sinon c'est pas drôle) : accroche du réseau mais pas
d'accès Internet. Le Wi-Fi n'est pas majoritairement utilisé dans la société
donc il impacte peu de monde et le problème traîne depuis un bail. J'avais
envisagé un dysfonctionnement des répéteurs sans fil et évacué le problème dans
ma tête. Mais vendredi, le problème est presque systématique je décide de le
prendre à bras le corps. Armé d'une tablette Lenovo (attention *placement de
produit* comme dirait mon fils) je regarde si je peux me connecter en DHCP mais
spécifier un autre serveur DNS quand l'adresse IP que le serveur m'a assigné
m'attire l'oeil : rien à voir avec notre réseau et non routable vers Internet.
Après recherche on découvre un petit routeur de test branché sur le réseau avec
la fonction "serveur DHCP" activée. Deux serveurs sur le même LAN : c'est le
plus rapide qui répond aux demandes, cela explique le côté aléatoire du
problème.

Ce qui me plaît dans l'administration système et réseau c'est la diversité des
problèmes et des solutions.
