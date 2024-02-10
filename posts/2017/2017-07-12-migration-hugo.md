<!-- title: Migration du blog sous Hugo -->
<!-- category: Blog -->
<!-- tag: planet -->

J'ai remplacé le le moteur de blog statique Pélican par Hugo et à vrai dire, ce
n'était pas prévu.<!-- more --> Un peu cloué par le rhume pour le week-end, j'ai suivi la
recommandation du médecin de rester tranquille. La cervelle fonctionnant encore
un peu, j'ai consulté ma liste de projets pour l'année, vous savez cette liste
mi-voeux / mi-résolutions qu'on établit en début d'année. En bonne place,
j'avais noté *"apprentissage ou perfectionnement dans un langage informatique"*.
Les années précédentes, j'ai fait un peu de Javascript, notamment un prototype
de MVC avec MEAN, de la glue Web à droite à
gauche mais j'ai toujours l'impression de partir de zéro avec ce langage.
Pourtant Javascript est de plus en plus incontournable professionnellement, même
pour un développeur plutôt teinté backend. Mais pour bien progresser il aurait
fallu partir avec un objectif projet, pas des exemples.

Au lieu de ça, j'ai flâné sur Rust et Go, des langages bas niveau (rien de
péjoratif). Cela fait un moment que je lorgne sur Go et franchement ce qui me
retient c'est le fait que ce soit porté par Google. J'ai un peu en travers leur
habitude de balancer les projets quand ils n'en ont plus besoin ou leurs
ruptures sans compatibilité ascendante (hein Angular). Bref j'hésite à
m'investir... Mais il faut reconnaître que Go est sorti en 2007, ils l'utilisent
vraiment en interne (pas comme Angular) et ça me plairait de rajouter un langage
plus bas niveau que Java ou Python avec des performances supérieures à mon
catalogue. A force de traîner sur des sites qui parlent du langage Go je suis
tombé sur Hugo, un moteur de blog statique. J'ai trouvé la documentation très
bien écrite et c'est un point de plus en plus important pour moi. J'ai décidé de
l'essayer... juste pour voir.

Je ne vais pas refaire pas la pub du blog statique. Démarré sur la plate-forme
Blogger, j'ai successivement migré ce blog sous Wordpress, PluXml, puis Pélican
et je ne reviendrai pas en arrière. D'un blog statique avec des articles écrit
en Markdown il est aisé de migrer vers n'importe où et on maîtrise le code HTML
généré (celui de Wordpress était particulièrement dégueulasse). En pratique ça
m'a pris une heure pour écrire une moulinette qui a transformé mes articles au
format de Hugo, c'est-à-dire qui a transformé les metadata de chaque article, le
contenu restant [au format
Markdown](https://daringfireball.net/projects/markdown).

Ce qui m'a pris du temps c'est le thème. J'ai testé quelques thèmes de
contributeurs, beaucoup lu la documentation détaillant la création de son propre
thème et je me suis lancé en transposant mon thème de Pélican (enfin les parties
HTML CSS) en mieux : avec les parties spécifiques paramétrables, dans un esprit
de réutilisation et de partage (oui c'est beau) même si ça n'arrivera
probablement jamais car mon thème est.. moche mais beau pour moi, amélioré,
raffiné au fil des ans, allégé avec [Pure CSS](https://purecss.io). Si je devais
changer un truc ce serait ajouter un peu couleur sur la bannière de haut de
page, ça ferait moins de gris. Quand le thème a été achevé on aurait dit une
copie du blog original mais qui se **génère en 1/2 seconde au lieu de 5
secondes**, la rapidité du langage Go compilé est réelle. J'ai retravaillé les
catégories et utilise intelligemment les tags pour générer des flux RSS
spécifiques notamment celui du Planet Libre (lien obsolète : http://planet-libre.org). Le
résultat est propre, exempt des années de bidouilles et de verrues que j'avais
ajouté sur Pélican.

J'ai un peu tâtonné pour générer exactement les mêmes URL puis j'ai abandonné.
J'ai préféré ajouter l'année dans l'URL d'un article, adieu mon référéncement
Google et mes millions de lecteurs désorientés ;-) Pour limiter la casse, j'ai
rajouté une règle au niveau du serveur HTTP pour rediriger les erreurs 404 vers
la page d'accueil.

Dernière angoisse, est-ce que le langage Go allait être disponible sur OpenBSD ?
La réponse est oui, et encore mieux, le projet Hugo fournit un binaire pour
OpenBSD. La mise en place sur l'hébergement a été galette. Quant au [système de
gestion des commentaires](https://github.com/kianby/stacosys) il est à nouveau
opérationnel (c'est l'avantage de maîtriser sa stack de logiciels) mais ça m'a
donné un peu de fil à retordre...  Cela fera le sujet d'un prochain article.
