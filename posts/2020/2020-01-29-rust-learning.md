<!-- title: Apprentissage de Rust -->
<!-- category: Développement -->

Pas de voeux sinistres cette année même si l'année écoulée n'a fait que [conforter ce que je pense](https://blogduyax.madyanne.fr/2019/sarah-connor/). Il n'empêche que la vie est belle, avec ses projets, ses espoirs et ses petits malheurs :-) 

Pour revenir dans le domaine de l'informatique on va parler code<!-- more -->, ma passion, devenue mon gagne-pain depuis fort longtemps. En dehors des tâches professionnelles, j'ai toujours été actif avec des *side projects* pour découvrir un langage, une techno ou une méthodologie. Mais l'année 2019 a été plutôt creuse, j'ai sûrement trop donné au taf, il n'y avait plus de neurones en sortant le soir ;-) et c'est la musique et les séries TV qui gagnaient. 

Java, Python, JavaScript, HTML & consorts sont mes langages réguliers depuis des années. Une indigestion de NodeJS avec son outil à remplir l'écran de warnings *indiquant que tout va bien* (qu'on appelle aussi NPM) et la lecture d'articles à la mode du style *"Comment devenir riche en 2020 en apprenant un nouveau langage hype recherché par toutes les entreprises du Fortune 500"* m'ont donné envie de voir autre chose. J'aurais pu choisir un langage listé dans le top 3 pour devenir riche mais j'ai décidé de me former au langage Rust, présent quand même dans le top 10, qui me fait de l'oeil depuis un bail. 

Pourquoi Rust m'a attiré ? 

- parce que c'est différent de JAVA où l'on se préoccupe de la conception, de la responsabilité de chaque classe, des objets échangés, de leur cycle de vie mais où les allocations de mémoire sont simples et le ramasse-miette (garbage collector) fait le ménage. 
- parce que c'est très différent de PYTHON où on a une productivité énorme et on détecte les problèmes lors du développement avec une batterie de tests unitaires où... à l'exécution si on a été négligent car le typage dynamique nous a pris par surprise. 
- parce que ça n'a rien à voir avec NodeJS dont l'usage côté serveur est réservé à des applications centrées autour du Web (à moins de vouloir se punir en codant en asynchrone des traitements conçus pour le séquentiel). 

Soyons clair, j'aime ces trois langages même si j'ai lancé une pique sur NodeJS et Rust n'est pas une solution universelle qui fait mieux que tout ce qui existe, absolument pas : un bon artisan doit utiliser l'outil le mieux adapté à la tâche qu'il doit réaliser. 

> Et la solution universelle c'est Golang, enfin d'après Google ;-)

J'ai très peu codé en langage C (uniquement pendant mes études) et jamais mis en pratique mes lectures sur C++. Revenir à un langage fortement typé, non objet mais avec des concepts permettant l'abstraction, centré sur les vérifications à la compilation, ça m'a vraiment intéressé par sa différence avec ce que je fais d'ahabitude. C'est un retour à une certaine programmation qui demande de l'effort pour maîtriser ses allocations mémoire (stack / heap, concept de *borrowing*), maîtriser les pointeurs et autres joyeusetés.

Pour démarrer, j'ai lu avec attention les 3/4 du [Rust Book](https://doc.rust-lang.org) et survolé le quart restant qui abordait des concepts très avancés en retenant que ça existe et que je pourrais m'y référer plus tard. Ce qui m'a plu d'entrée, c'est la qualité de ce livre. Je fais un parallèle avec Golang qui est un langage plein de qualité mais dont la doc officielle est vraiment pas terrible et nécessite de trouver d'autres ressources. Le Rust Book est complet, on aborde les concepts un par un. On sent le langage Rust bien né, bien pensé avec une cohérence entre les concepts démontrant que les concepteurs savent exactement où ils vont avec leur langage. 

Du coup je prend mon temps pour absorber ; j'ai lu le livre par étapes pendant deux semaines avant d'écrire une ligne de code. J'ai choisi de réécrire [un de mes projets Python](https://github.com/kianby/stacosys) vers Rust. [Mon projet](https://github.com/kianby/stacorust) est modeste en nombre de lignes et il mixe un serveur HTTP, des templates, de la gestion d'e-mails. C'est un bon petit projet pour comprendre, expérimenter et essayer d'écrire du code Rust dans les règles de l'art. Si l'apprentissage est fructueux je publierai quelques articles sur des éléments du langage Rust.
