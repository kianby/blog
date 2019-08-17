---
layout: post
published: true
title: Refonte complète du blog
categories: Blog
tags: ''
---
Le blog a pris son envol et il a désormais son propre nom de domaine **blogduyax.fr**. 

Ce n'est qu'un changement parmi une multitude, et un drôle de cheminement qui d'une idée de base un peu floue a mené à une refonte complète du blog<!-- more --> : 

- abandon du moteur de blog [Hugo](https://gohugo.io/) pour [Jekyll](https://jekyllrb.com/)
- mise à la retraite du système maison de commentaires **Stacosys** pour [Isso](https://posativ.org/isso/)
- hébergement sur GitHub Pages

Certains diront que j'ai mis de l'eau dans mon vin et ils n'auront pas tort ;-) 

Comment en suis-je arrivé là ? Et bien j'avais en idée de faciliter la chaîne de publication des articles. J'adore ce qu'apporte un moteur statique : l'écriture des articles en Markdown et une génération en pages statiques, la facilité à publier le contenu sous gestion de sources (GIT). Mais la publication nécessite d'allumer un ordinateur de peaufiner le brouillon et de de faire un *git push* pour publier. Rien de complexe mais la nécessité de repasser par un PC pour publier alors que ma vie est plutôt mobile.

J'ai envisagé de coder une interface d'administration Web avec un éditeur Markdown (on en trouve plusieurs en JavaScript sous licence Open Source) et une interaction avec GIT pour fluidifier la publication. Mais je n'ai pas trouvé l'étincelle pour démarrer donc j'ai fait des recherches pour voir si ça n'existe pas prêt à l'emploi, j'étais même prêt à changer de moteur de blog si nécessaire. J'ai regardé les extensions de Hugo, [les autres moteurs statiques](https://www.staticgen.com/) et même [les CMS en fichier à plat](https://www.flatphile.co/). J'ai installé beaucoup de containers Docker pour évaluer les fonctionalités. Grav, Bludit, PhileCMS... beaucoup de moteurs avec des atouts mais aucun ne m'a vraiment enthousiasmé. 

Puis j'ai découvert [Prose.io](http://prose.io) qui donne tout son potentiel avec Jekyll. Je m'étais intéressé à Jekyll avant de choisir Pelican en 2013 et c'est l'écosystème Python que je connais bien qui avait orienté mon choix en défaveur de Ruby. Pas de regret mais là j'ai regardé Jekyll en détail et je l'ai trouvé très attractif : simple, cohérent,  mature, bien documenté et extensible par des plugins. Alors au niveau des performances, on génére les pages du blog en 15 secondes plutôt que 5 mais ce n'est pas un critère important pour mon utilisation. J'ai choisi un thème et j'ai commencé la migration de mes pages. On reste sur du Markdown donc le gros du travail c'est la migration des *metadata* et l'adaptation du thème.

Il y a possibilité d'héberger Prose sur ses propres serveur mais j'avais déjà passé un cap et accepté l'idée d'héberger le blog sur GitHub Pages ce qui me permet de préserver le fonctionnement actuel, à savoir pouvoir écrire mon article en Markdown depuis mon PC et générer le blog localement avec mon Jekyll en mode développement avant de publier avec un *git push*. Mais je peux aussi écrire un article en mobilité depuis Prose et publier directement l'article. Choquant ? pas tant que ça ! je sépare l'hébergement du blog du reste de mon infrastructure et je garde la main sur les données. Si l'orientation de GitHub ne me plait pas ou s'ils changent les règles d'hébergement, je récupère mon blog Jekyll et je l'héberge sur mon serveur dédié. 

Et quid des commentaires ? Les URLs des articles ont bougé donc j'ai bousillé tout le référencement et je n'avais pas envie de me casser la tête à maintenir des redirections entre les anciennes URLs et les nouvelles. J'aurais pu adapter la partie *front-end* de Stacosys pour qu'elle devienne full JavaScript et soit intégrable dans le blog mais il aurait aussi fallu modifier l'ensembles des URLs. J'ai évalué Isso et j'ai décidé que Stacosys pouvait prendre sa retraite. Né au moment où il n'y avait pas beaucoup de solutions pour les blogs statiques, il n'a plus d'avantages fonctionnel. Isso a une administration Web en plus des notifications par e-mail, ce que j'avais prévu de développer... un jour. Inutile de réinventer la route, j'héberge Isso sur mon serveur dédié et il sert les commentaires du blog sur l'autre domaine. J'ai migré les commentaires existants car l'histoire d'un blog ce ne sont pas que des articles. 

![Sea Bird]({{site.baseurl}}/images/2019/sea-bird-night-water-9012.jpeg)






