<!-- title: Ne pas couper la branche -->
<!-- category: Hébergement -->
<!-- tag: planet -->

Je continue à héberger mes services personnels sur un serveur Dedibox propulsé
par une Debian.<!-- more --> En 2016, j'ai rajouté deux services : mon instance de
[Wallbag](https://wallabag.org) et le [serveur de
mail](/2016/peu-de-neuf/) du domaine *madyanne.fr* à
ceux existants : mon lecteur de flux RSS (Tiny Tiny RSS), mon cloud (NextCloud)
et ce blog. La reprise en main des e-mails a été une très bonne idée, c'est
formateur et on décide des limites : le nombre de comptes et d'alias, l'espace
de stockage alloué à chaque compte.

Mais il faut penser qu'en cas de panne du serveur, on n'a plus d'e-mail et
surtout pas d'alerte à moins d'utiliser un e-mail alternatif. J'utilise mon
e-mail *@madyanne.fr* pour l'ensemble des services mais il faut faire une
exception pour Gandi qui gère mes DNS et Online qui héberge mon serveur. Sinon,
je ne suis pas prêt de recevoir une notification en cas d'interruption de
service du serveur de mail. 

J'aurais pu me servir de mon e-mail Google, qui me sert seulement pour
accéder au Play Store avec mes équipements Android, mais ses e-mails sont
récupérés par *madyanne.fr* grâce à Fetchmail. J'ai donc dépoussiéré un vieil
e-mail Free, inutilisé depuis 15 ans, inconnu des spammeurs et je l'ai ajouté
comme e-mail d'alerte chez Online et Gandi. En prime, j'ai créé un compte sur
[Uptime Robot](https://uptimerobot.com) qui vérifie que le blog est accessible
toutes les 5 minutes et m'envoie une alerte e-mail sur mon compte principal et
chez Free.

Bon c'est pas mal, je n'ai pas coupé la branche sur laquelle je suis assis : si
le serveur de mail tombe, j'aurais des alertes... à condition de vérifier
régulièrement la boite de réception de mon e-mail chez Free. Ca veut dire
rajouter gérer deux comptes e-mails sur mon téléphone et je n'ai pas envie de
cette contrainte. L'idéal serait de recevoir un SMS si un e-mail arrive chez
Free, ce qui doit être exceptionnel car symptomatique de gros problème. Me
voici donc en quête d'un service gratuit d'envoi de SMS et après diverses
pérégrinations j'ai fini sur [IFTTT](https://ifttt.com). Bon c'est gratuit donc
c'est probablement moi le produit et ne sachant pas trop quel est le *business
model* de IFTTT je ne sais pas encore quelle part de mon âme j'ai bradé  Si
vous avez une alternative pas chère pour cette partie d'envoi de SMS je suis
intéressé.


