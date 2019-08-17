<!-- title: Protégeons notre vie privée -->
<!-- category: Humeur -->
<!-- tag: planet -->

Framasoft [fête les 3
ans](https://framablog.org/2017/09/25/degooglisons-internet-cest-la-fin-du-debut)
de sa campagne [Dégooglisons Internet](https://degooglisons-internet.org). Le
nombre de services alternatifs aux GAFAM, libres et respectueux de la vie
privée, a grossi ainsi que le nombre d'utilisateurs.<!-- more --> Comme ils l'expliquent
eux-mêmes, le but n'est pas de devenir un hébergeur professionnel mais plutôt de
servir de catalyseur pour que les gens prennent conscience qu'il y a une autre
voie, décident de se libérer et auto-hébergent leurs services s'ils le peuvent
ou aient recours au tissu associatif à travers [le collectif des
Chatons](https://chatons.org) par exemple.

Chaque fin d'année je fais un don financier à un ou deux acteurs qui me semblent
cruciaux dans le monde du Libre ; c'est d'ailleurs généralement la période de
relance, chacun essayant de boucler son budget de fonctionnement pour l'année à
venir. Beaucoup ont besoin d'aide et ils sont à la fois nos bras armés et nos
boucliers. Je pense à Framasoft, à la Quadrature du Net, à l'APRIL, à Wikipedia, à
des équipes de développement, des distributions Linux. Bref il y a beaucoup à
soutenir et il faut faire des choix. Cette année je serais exclusif et ce sera
Framasoft pour rétribuer mon usage de [Framasphere](https://framasphere.org) et
soutenir la suite de la campagne.

Pour ma part, j'ai dégooglisé progressivement depuis un bout de temps les
services vitaux : contacts, agenda, mails. Ca ne veut pas dire qu'on peut
m'appeler [Richard](https://fr.wikipedia.org/wiki/Richard_Stallman) et que je
n'utilise aucun service GAFAM :  

- j'utilise Youtube, mais je n'ai pas envie qu'on me profile à travers mes recherches,
- la navigation Waze me sort régulièrement des soucis à Marseille,
- j'ai un compte Twitter pour participer à des concours et suivre quelques stars du Net (comme [Korben](https://korben.info) que je lis depuis des années et apprécie pour sa constance et sa franchise)

Comme en religion, chacun met la barre à son niveau et voit jusqu'où il veut /
peut aller... et on trouve aussi des extrémistes dans ce domaine.

Donc en plus d'ordinateurs sous Linux et OpenBSD, d'un téléphone génial utilisé
par 0,1% du marché, j'ai aussi une belle tablette Android déjà évoquée dans mes
articles autour de [Termux](https://termux.com) : bootloader verrouillé, ROM
Android du constructeur. Je surfe avec Firefox, j'utilise mes propres services
pour le mail, l'agenda, les contacts, le cloud. Mais je suis quand même sur un
système non maîtrisé qui :

- me propose tous les jours des mises à jour d'applications que je n'utilise pas : Gmail et consorts,
- m'a imposé une mise à jour Android qui a cassé la possibilité de me connecter au hotspot Wi-Fi de mon télphone donc adieu Internet quand je suis en vadrouille,
- rame de plus en plus, sans que je trouve d'explication, jusqu'à rendre la tablette inutilisable plusieurs minutes à chaque sortie de veille Wi-Fi,
- mange certains jours 1/4 de batterie alors qu'il est censé être en veille.

Bref, la coupe était pleine. La garantie de la tablette étant expirée, je me
suis décide à regarder ce qui est faisable : idéalement changer la ROM, à défaut
revenir à une version précédente du constructeur. Je passe les détails
techniques affligeants mais parti sur l'option 2, j'ai failli transformer la
tablette en brique et j'en suis sorti à force de parcourir le forum XDA à la
recherche d'infos. Pour les connaisseurs j'étais bloqué au BIOS dans l'EFI (car
oui ma tablette a un processeur Intel) et j'ai réussi à réinjecter ma ROM
d'origine (celle du constructeur) avec une manipulation tordue. Ce que j'ai
retenu c'est que monde Android c'est le monde Ms Windows tel que je lai quitté
il y a des années : la plupart des gens sur les forums ne connaissent pas grand
chose et préconisent d'appliquer des recettes de cuisine : installe tel soft,
fais telle manip. Ce n'est pas leur faute, on est sur un sytème fermé (pour ce
qui est du bootloader en tout cas) donc à part quelques initiés qui ont la
connaissance acquise par la sueur à force de *reverse-engineering*, la masse ne
fait que propager de l'information erronée et recopier des topics de forums.

Revenu donc au point de départ, j'ai tenté le *rootage* de la tablette ; c'est
moins risqué qu'un changement de ROM. Je l'ai réalisé et j'ai pu désinstaller
les applications Google de ma tablette gràce à un utilitaire nommé **/system/app
mover** trouvé sur le magasin d'applications [F-Droid](https://f-droid.org).
J'ai commencé petit, en virant les applications Google, puis j'ai carrément viré
le Playstore et surtout ses services. J'ai récupéré 300 Mo de mémoire (pas
négligeable sur une tablette de 2 Go) et je n'ai plus aucun ralentissement
depuis 3 semaines. Je me suis prouvé, au passage, que toutes les applications
dont j'ai besoin pour ma tablette sont sur F-Droid.

![Tablette](/images/2017/tablette-root.jpg)

Est-ce que c'est parfait ? Non pas du tout car j'ai enlevé les applications
Google et quelques services du système, mais je ne maîtrise pas ce qui reste :
il peut rester un service de pistage qui bouffe mes données et les envoie à
Google.

Une dégooglisation complète passe par plusieurs étapes :

1. se libérer des services GAFAM et mettre en place soi-même ou utiliser des alternatives.
2. utiliser un système d'exploitation libre ou *de confiance* :
    - un système GNU/Linux (pas n'importe lequel) ou un système BSD
    - en mobilité, sur Android :
        - *rooter* l'appareil pour pouvoir faire le ménage, c'est mieux que rien.
        - installer une ROM commmunautaire (pas n'importe laquelle) sans les Google Apps, c'est mieux.
3. utiliser du matériel libre grâce à l'Open Hardware

Je considérais, jusqu'à récemment, le 3ème point exagéré pour des équipements
domestiques mais j'ai largement changé d'avis.

Le ciblage publicitaire est de plus en plus précis. Ma moitié a reçu dans la
semaine un e-mail d'encouragement pour s'inscrire sur le site de la Française
des Jeux, probablement car elle est passée sur leur site pour consulter les
résultats. Elle navigue sur un Samsung A5 avec Chrome donc qu'ils aient obtenu
l'e-mail ne m'étonne pas, mais qu'ils connaissent mon prénom un peu plus. En bas
de l'e-mail, [la société tierce responsable de ce
profilage](http://www.eperflex.com/lg/fr/fonctionnalites) propose de se
désabonner de leurs services. J'aime me désabonner quand je n'ai jamais été
invité à m'abonner... Bref ma moitié navigue essentiellement en 4G donc cela
exclut le recoupement avec notre adresse IP domestique. Je penche plutôt pour un
recoupement entre son e-mail et d'autres données glanées à droite à gauche (???)
pour parvenir à lier nos identités.

La semaine d'avant nous avons été confrontés, toujours sur le Samsung, au
mini-scandale de l'enregistrement des visages, une sympathique fonctionnalité,
[découverte par Seb Sauvage](http://sebsauvage.net/links/?0vFdFg), destinée à
enrichir la base de reconnaissance faciale de Google. [Dans son dernier
article](http://standblog.org/blog/post/2017/09/29/Payer-son-smartphone-avec-ses-donn%C3%A9es-personnelles),
Tristan Nitot clarifie bien ce *deal* entre Google et les constructeurs de
téléphone.

Pour les appareils mobiles, le matériel est bien le souci principal. Et on peut
se demander jusqu'à quand certains constructeurs pourront continuer à fournir
des bootloader déverrouillés pour faire plaisir à quelques clients, sans que
Google durcisse sa position et l'interdise. De plus, installer une ROM
communautaire résoud partiellement le problème : il reste des bouts de code
propriétaires dans les composants électroniques du téléphone dont on ne connait
pas le fonctionnement. La solution ultime est un téléphone **Libre de A à Z** :
logiciel (Open Source / Libre) et matériel (Open Hardware).

On a assisté une succession de projets de téléphones plus ou moins libres depuis
quelques années : [OpenMoko](https://fr.wikipedia.org/wiki/OpenMoko),
[Maemo](https://fr.wikipedia.org/wiki/Maemo) et plus récemment, FirefoxOS et
Ubuntu Phone.

Ne nous voilons pas la face, ils ont tous échoué, mais ils ont apporté leur
pierre à l'édifice et participé à la prise de conscience du problème des GAFAM
et du marchandage de notre vie privée qui dépasse largement le cercle des geeks
aujourd'hui.

Le ~~buzz du moment~~ prochain téléphone libre serait [le
Librem](https://puri.sm/). Encore faut-il y croire suffisamment et avoir
confiance dans la société Purism pour mettre la main à la poche et subventionner
sa création.

En tout cas, avoir pris conscience du problème c'est déjà un grand pas et le
début de l'action pour reprendre sa vie numérique en main.

La route est longue mais la voie est libre !

![Phagocitage](/images/2017/phone-boss.jpg)

Source de l'image : [maymay](https://framasphere.org/people/f01a0d1e920196e5)
