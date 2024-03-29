<!-- title: Migration du blog sous Pelican -->
<!-- category: Blog Hébergement -->
<!-- tag: planet -->

Et oui, un de plus à migrer son blog sous [Pelican](http://docs.getpelican.com) !<!-- more -->
J'ai lu plusieurs récits de migration depuis trois mois, ce qui dénote un
engouement certain pour ce moteur de blog par... essentiellement des développeurs.
La perspective de gérer ses articles comme du code, avec un
article par fichier, de construire le blog avec une commande 'make' et
publier dans un gestionnaire de source nous ramène en terrain familier.

Les points suivants ont achevé de me convaincre :

*   l'écriture dans une syntaxe simplifiée (un markup langage) ; j'ai opté pour
    [Markdown](http://daringfireball.net/projects/markdown/). Je peux commencer
    l'écriture d'un article depuis n'importe quel équipement, même l'application mémo
    de mon téléphone.
*   la possibilité de tout gérer depuis un terminal en mode texte, de
    l'écriture d'un article à sa publication. Ce qui me permet de travailler
    facilement depuis n'importe où avec une connexion SSH sur mon serveur
*   La génération de pages statiques. Adieu PHP, on peut héberger encore plus
    facilement.

En fait c'est le prolongement du raisonnement qui m'avait fait passer de
WordPress à [PluXml](http://www.pluxml.org).

L'import depuis PluXml est faisable par l'import RSS mais la conversion en Markdown est
approximative. J'ai donc écrit un outil de migration dédié en langage Python. Ce
qu'il apporte c'est une mise en forme plus fidèle lors de la conversion en
Markdown, une gestion des catégories **et des tags**. Il ne couvre peut-être
pas tous les cas mais il m'a permis de migrer mes articles sans retouche
manuelle (obsolète : Cet outil est disponible sur mon compte GitHub).

Pour les thèmes c'est selon les goûts de chacun. Pelican fournit un langage de
templating Python [Jinja 2](http://jinja.pocoo.org).
A chacun de voir s'il veut un thème simple ou un thème plus dynamique avec du
JavaScript. Quelques thèmes d'exemple sont fournis sur
[GitHub](http://github.com/getpelican/pelican-themes). Pour ma part, Je suis parti d'un thème
basé sur [Bootstrap](https://getbootstrap.com), le kit CSS qui permet
facilement de faire du Responsive Design afin d'avoir un site qui s'adapte à
tous les périphériques Web (ordinateurs de bureau, tablettes, téléphones) et je
l'ai adapté à ma sauce.

En résumé, Pelican est un très beau projet. Sous le capot, on trouve un outil
bien pensé, dans l'esprit du langage Python. Il est possible de développer des
plugins qui effectueront des actions à différentes phases de la génération des
pages HTML. Le seul point manquant, c'est le support des commentaires.
Normal pour un outil qui génère des pages statiques. La solution proposée consiste
à déléguer cette tâche à Disqus, un service Web privé. Cela ne me convient pas du tout,
je me suis auto-hébergé pour garder la main sur mes données. J'ai gardé les
commentaires de tous les articles et je cogite à une solution alternative....
En attendant, j'ai ouvert un email pour le blog qu'on peut utiliser pour
échanger : <i class="icon-envelope"></i> blogduyax at madyanne.fr
