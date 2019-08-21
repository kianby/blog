<!-- title: Performance Python Web -->
<!-- category: Développement Hébergement Blog -->

J'ai terminé l'article précédent en évoquant le [système de gestion des
commentaires Stacosys](https://github.com/kianby/stacosys) et sa mise en place
sur le blog propulsé par [Hugo](https://gohugo.io).<!-- more --> Il est installé sur le même
serveur que le blog mais il pourrait tout à fait être déporté car le blog
statique interagit avec lui par du code JavaScript qui envoit des requêtes
RESTful afin de :

- récupérer le nombre de commentaires d'un article
- récupérer les commentaires d'un article
- soumettre un nouveau commentaire

Avant de migrer vers Hugo, les commentaires étaient visibles seulement à
l'intérieur des articles. C'est à dire qu'une page de blog affiche un extrait de
l'article, à raison de 10 articles par page, et une pagination (page précédente /
page suivante) permet de naviguer. C'est seulement quand on lit un article
particulier qu'en fin de page on a un bouton *"voir les XX commentaires"* qui
affiche le nombre de commentaires de l'article. Donc en navigation, on n'a
aucune requête vers Stacosys. C'était un choix technique pour ne pas le
surcharger de requête. En réécrivant le thème, j'ai trouvé sympa d'ajouter
l'affichage du nombre de commentaires de chaque article sur la page principale,
ce qui se fait un peu de partout.

Cela ressemble à ceci :

![Nombre de commentaires sur la page](/images/2017/page-comments.png)

La récupération du nombre de commentaires des 10 articles de la page est
réalisée en JavaScript donc de manière asynchrone et on envoie 10 requêtes vers
le serveur HTTP de Stacosys qui est celui du framework Python Flask. J'ai voulu
tester un peu les limites du système pour avoir une idée de ce le blog est
capable de supporter.

Le test consiste à effectuer le plus de requêtes possible pendant 1 minute avec
une charge de 250 clients simultanés par seconde. Avec 10 articles par page,
cela correspond à 25 lecteurs simultanés et particulièrement excités qui tapent
frénétiquement sur la touche F5 pour rafraichir la page du navigateur donc
beaucoup plus de lecteurs avec un comportement *normal*. Sur une base de 8
secondes de visite par page, cela correspond à 200 visiteurs simultanés. J'en
suis loin, c'est mon nombre de visites par jour :-) mais cela donne un objectif
de charge à tenir.

Quand la minute est écoulée on regarde **combien de requêtes** on a pu
satisfaire et **le temps de réponse moyen** pour les satisfaire. La qualité du
résultat dépend de ces deux variables. J'ai fixé arbitrairement 10 secondes
comme temps de traitement acceptable. Les requêtes non honorées dans ce laps de
temps sont marquées en erreurs. N'ayant pas 250 volontaires, j'ai utilisé une
plate-forme de test non libre (oui je sais
[Richard](https://fr.wikipedia.org/wiki/Richard_Stallman)...)

Comment lire le tableau des résultats :

- La colonne *workers* indique le nombre de processus ou threads travaillant en
parallèle pour traiter les requêtes.
- Le temps de réponse est en millisecondes avec le temps minimum, le temps moyen et le temps maximum.
- Les erreurs sont des timeout : la requête n'a pas pu être honorée en moins de 10 secondes.

J'ai d'abord fait un test dans l'état actuel avec Stacosys en HTTPS et le
résultat est assez décevant. Pour le test, j'ai repassé Stacosys en HTTP et le
résultat m'a étonné :  

    |   Serveur   | Workers |  Temps de réponse  | Requêtes | Erreurs |
    | ----------- | :-----: | :----------------: | -------: | ------: |
    | Flask HTTP  | 1       | 95 > 2595 > 20000  | 7169     | 197     |
    | Flask HTTPS | 1       | 104 > 4194 > 32000 | 4043     | 326     |

On constate un écroulement complet en HTTPS. Je sais qu'il y a un coût, mais la
gestion SSL étant portée par le serveur HTTP en frontal, je n'aurais pas pensé à
une telle baisse de performance.

Comme on récupère un nombre de commentaires par article, une information non
critique, j'ai envisagé de demander cette information en HTTP. Ca n'aurait pas été
glorieux mais la différence de performance est telle que je l'ai envisagé avec
deux options qui ne peuvent pas fonctionner.

**Option 1** : le blog reste en HTTPS et fait des appels CORS en HTTP à Stacosys.
Ce n'est pas autorisé par les navigateurs car on n'a pas le droit de baisser la sécurité.

**Option 2** : le blog revient en HTTP, après tout ce ne sont que des articles et il
appelle Stacosys tantôt en HTTP, tantôt en HTTPS, en fonction de la criticité de
l'information. On posterait les commentaires en HTTPS mais on fournirait le
nombre de commentaires par article en HTTP. Et bien c'est impossible aussi car
avec une configuration SSL un peu sérieuse, le paramètre
[HSTS](https://fr.wikipedia.org/wiki/HTTP_Strict_Transport_Security) est activé
pour éviter les attaques du type
[man-in-the-middle](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu)
et, dans mon cas, j'ai fixé la durée HSTS à 1 année. Donc si je désactive HTTPS,
les navigateurs de mes lecteurs continueront à se connecter en HTTPS, à moins de
purger leur paramétrage. N'ayant pas les numéros de téléphone de tout le monde,
c'est foiré. C'est à garder en mémoire pour ceux qui envisageraient de passer à
HTTPS avec Let's Encrypt pour voir... Le retour en arrière n'est pas évident si
HSTS est en place.

Donc il va falloir vivre avec HTTPS et essayer d'améliorer les performances !

![Speedy](/images/2017/speedy.png)

Il est vrai que le serveur HTTP de Flask est préconisé pour le développement et
pas la production. On recommande d'utiliser [Gunicorn](http://gunicorn.org) ou
[Uswgi](https://uwsgi-docs.readthedocs.io/en/latest) qui sont optimisés (avec
des parties écrites en langage C ou C++), fournissent de la concurrence dans le
traitement. J'ai testé Uswgi qui m'a donné beaucoup de fil à retordre par sa
complexité de configuration. J'ai fait un test un peu meilleur mais avec une
charge CPU beaucoup plus lourde. Il faut trouver un équilibre entre le gain de
performances Web et l'impact sur la charge CPU du serveur en rajoutant des
processus *workers*.

Ces deux serveurs Web sont probablement très bien et tout le monde semble les
utiliser pour la mise en production d'application Python Web sérieuses mais pour
mon besoin plus humble, ça me gêne de modifier l'application à cause du
déploiement. Alors à force de chercher j'ai déniché une alternative qui
s'appelle [Sanic](http://sanic.readthedocs.io) : un serveur HTTP en pur Python
qui utilise les capacités de traitement asynchrones de Python 3.5 ce qui lui
permet avec 1 worker, de doubler les performances de Flask. Remplacer Flask par
Sanic dans une application Flask c'est galette : les développeurs de Sanic ont
défini une API très proche, pensée pour que la migration se fasse rapidement.

Voici les résultats de Sanic avec différentes configurations de *workers* :

    |   Serveur   | Workers |  Temps de réponse  | Requêtes | Erreurs |
    | ----------- |:-------:|:------------------:| --------:| -------:|
    | Flask HTTPS |    1    | 104 > 4194 > 32000 |     4043 |     326 |
    | Sanic HTTPS |    1    | 85 > 2657 > 20023  |     8741 |     123 |
    | Sanic HTTPS |    2    | 85 > 2087 > 23634  |     7048 |     198 |
    | Sanic HTTPS |    4    | 86 > 1777 > 18936  |     8102 |     191 |

On constate que le nombre de requête traités grimpe et que le temps de réponse
moyen s'améliore. Par contre, le nombre d'erreur augmente un peu. La performance
HTTP progresse car le serveur est capable de gérer plus de requêtes mais le
temps de traitement ne progresse pas et il faut toujours effectuer une requête
dans la base de données pour renvoyer le nombre de commentaires. Pire, cette
partie requête en base n'est pas asychrone donc on bloque un *worker*. Pour la
1ère page du blog qui est la plus consultée, ce sont les mêmes compteurs qui
sont demandés par chaque visiteur. Il y a un réel intérêt à mettre en cache ces
valeurs pour diminuer le temps de traitement. C'est ce que j'ai fait
programmatiquement dans Stacosys avant de relancer un test de performance avec
le cache activé.

    |       Serveur       | Workers |  Temps de réponse  | Requêtes | Erreurs |
    | ------------------- |:-------:|:------------------:| --------:| -------:|
    | Flask HTTPS         |    1    | 104 > 4194 > 32000 |     4043 |     326 |
    | Sanic HTTPS         |    4    | 86 > 1777 > 18936  |     8102 |     191 |
    | Sanic HTTPS + cache |    4    | 81 > 1152 > 12408  |    13558 |     210 |
    | Sanic HTTPS + cache |    1    | 81 > 1367 > 18869  |    11589 |     171 |

On traite plus de requêtes en moins de temps, le gain est palpable. Le cache est
pour beaucoup dans le gain et pour le dernier test je suis revenu à 1 worker
seulement pour limiter la charge CPU du serveur. Le résultat est honorable avec
plus de 11000 requêtes traitées et un taux d'erreur assez bas. C'est cette
configuration que j'ai mis en place sur le blog.

Après avoir rédigé cet article, j'ai effectué un test basique (pas dans le
contexte Stacosys) avec le serveur HTTP du langage Golang et le résultat m'a
ramené à mes lectures du moment sur les architectures microservices, les couches
protocolaires optimisées comme [nanomsg](http://nanomsg.org) et les langages
compilés. Il n'est pas exclu que je réécrive mes outils différemment.
