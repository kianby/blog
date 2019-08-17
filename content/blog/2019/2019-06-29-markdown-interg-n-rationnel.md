---
layout: post
published: true
title: Markdown intergénérationnel
categories: Développement
---
Je suis un fan du Markdown depuis que je connais son existence : un langage de balise lisible, aisément mémorisable pour écrire sans distraction en se concentrant sur le contenu, pas sur la forme.<!-- more --> C'est le Markdown qui m'a intéressé aux générateurs de sites statiques. Il est parfait pour l'écriture mais il montre ses limites pour produire du document (ce pour quoi il n'a pas vraiment été conçu). Mais un langage de balise est par nature extensible donc des extensions ont vu le jour pour générer une table des matières, gérer des tableaux et d'autres trucs plus exotiques...

Mermaid permet de concevoir des diagrammes de flux, de séquence et de Gantt, sans application, car c'est un langage de script où l'on décrit le diagramme et Mermaid effectue le rendu graphique. Je vous renvoie [à la doc](https://mermaidjs.github.io) mais ça permet de faire des trucs cools. On n'a pas la main sur le rendu (car il est généré automatiquement), cela ne remplace donc pas un outil graphique pour les diagrammes complexes mais c'est idéal pour incorporer des diagrammes de moyenne complexité dans un document produit par un langage de balise comme Markdown, ou pour du rendu dynamique dans une application Web.

L'outil libre, véritable *couteau suisse* de la conversion de documents est [Pandoc](https://pandoc.org). Avec lui on peut convertir du LaTeX en PDF, du markdown en HTML, faire intéropérer des formats Wiki, les possibilités sont énormes. Un [filtre Mermaid pour Pandoc](https://github.com/raghur/mermaid-filter) existe donc on peut tirer parti de Mermaid dans la conversion d'un document Markdown vers HTML ou PDF.

C'est là que le titre de mon article intervient : Pandoc est écrit en Haskell, un langage des années 90 avec une version majeure par décennie, alors que Mermaid est écrit en Node.JS, un langage en plein bouillonnement qui revisite une partie de son éco-système chaque année. Il est génial que les deux langages s'allient pour fournir l'intégration de Mermaid dans Pandoc mais comment installer tout cela ?

Pandoc est un vétéran, on le trouve dans toute distribution GNU/Linux bien née. Node.JS c'est plus compliqué. J'avais une version plutôt récente et je me suis fait rejeter pendant l'installation de Mermaid par NPM. A mon avis, la meilleure approche avec Node.JS consiste à l'installer par un autre canal que les dépôts. J'ai viré toute installation venant des dépôts sur ma machine et j'ai installé un outil qui s'appelle [n](https://github.com/tj/n) via NPM dont le rôle est gérer les installations de Node.JS. Cerise sur le gateau, il permet de faire cohabiter plusieurs versions de Node.JS, par exemple la LTS 10.16.0 et la dernière version 11.x. 

Bien outillé, j'ai retenté l'installation du filtre : 

    npm install --global mermaid-filter
    
Mais elle échoue sur le téléchargement de chromium pendant l'installation d'une dépendance appelée *pupeteer* avec un message d'erreur abscons. La recherche de solution est un peu inquiétante : un gars aurait pu installer en utilisant un miroir chinois de npmjs, un autre l'a fait à la mano depuis une installation manuelle de chromium. Finalement c'est Stack Overflow qui fournit une solution plus acceptable en élevant les droits pendant l'installation du paquet : 

    npm install puppeteer --unsafe-perm=true --allow-root

Et là ça se passe bien ! 

Du coup je prépare un petit bout de Markdown avec du Mermaid dedans pour tester : 

	# Markdown et plus

    Un diagramme rendu par Mermaid.

    ~~~mermaid
    sequenceDiagram
        Alice->>John: Hello John, how are you?
        John-->>Alice: Great!
    ~~~

N'ayant pas installé le module node en tant que root mais sous mon utilisateur, mon test de Pandoc référence l'emplacement de l'installation : 

    pandoc -t html -F ~/node_modules/mermaid-filter/index.js -o mermaid.html mermaid.md

Et voici le rendu HTML:

![Rendu Mermaid]({{site.baseurl}}/images/2019/mermaid.png)

Bon markdown !
