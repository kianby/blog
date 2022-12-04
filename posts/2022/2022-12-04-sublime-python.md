<!-- title: Sublime IDE pour Python -->
<!-- category: Développement -->

J'avais [délaissé Sublime depuis un bout de temps](https://blogduyax.madyanne.fr/2017/sublime-text-vs-atom/) pour VsCode comme éditeur polyvalent. L'intégration étroite de l'outil avec WSL, que j'utilise professionnellement, a facilité son adoption. Dans un usage quotidien, on trouve presque toujours un plug-in adapté au besoin : IDE multi-langage, analyse de CSV, prévisualisation de diagrammes PlantUML, de Markdown, OpenAPI, résolution de conflits Git. Je n'ai donc pas suivi le bout de chemin de Sublime en version 4 jusqu'à ce que je réinstalle ma version 3 en éditeur secondaire pour éviter de lancer VsCode dans certains cas car son démarrage est un peu lent (architecture Electron oblige) et ça ne se justifie pas toujours. 

Puis récemment j'ai eu une prise de tête avec VsCode et sa gestion foireuse des projets Python basés sur Poetry et un blocage pour choisir l'interpréteur Python de l'environnement virtuel du projet. J'ai voulu voir ce que pouvait faire Sublime en 2022... Pour moi, Sublime était un projet en perte de vitesse qui ne pouvait pas rivaliser avec le compresseur Microsoft ; et son modèle commercial en licence perpétuelle devait apporter des revenus très limités pour développer des nouvelles fonctionnalités. J'ai revu un peu mon jugement depuis...

J'ai donc joué à "construis un IDE pour Python avec Sublime". J'ai installé la version 4 et les plug-ins suivants : 
- LSP : ajout de la fonctionnalité [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) développée/standardisée par Microsoft
- LSP-pyright : support du langage Python pour LSP 
- Python black : formatage de code avec Black
- Python breakpoints : ajout de point d'arrêts **Pdb** rustiques dans le code 

et pour combler quelques manques pas encore intégrés à Sublime :
- SideBarTools : ajout d'actions de fichiers (renommer, dupliquer, déplacer)
- SyncedSideBar : synchroniser l'onglet ouvert avec la *side bar*

Cela peut sembler ironique d'intégrer LSP (qui s'exécute dans serveur NodeJS au lancement de Sublime) pour ajouter à Sublime les fonctions d'un IDE, mais le résultat n'est pas au rabais, loin s'en faut. LSP apporte une analyse du code et des dépendances, du contrôle de type, de la complétion intelligente, la documentation intégrée et des fonctions de refactoring. 

![sublime-ide](/images/2022/sublime.png)

C'est la meilleure partie de VsCode que Microsoft a libéré avec LSP, pour ses besoins propres au début, accélérer l'intégration de nouveaux langages dans VsCode mais c'est une technologie ouverte dont Vim ou NeoVim peuvent tirer parti pour proposer des fonctions d'IDE sur différents langages. Et différents contributeurs implémentent LSP pour des langages moins connus. C'est un bel exemple de devéloppement communautaire. 

Aussi, je pense que le petit poucet Sublime tire bien son épingle du jeu en capitalisant sur des plugins développés par des contributeurs et en se focalisant sur le coeur, son éditeur robuste, léger et bien optimisé. J'ai renouvelé ma license 4 en espérant qu'il n'est pas trop tard pour soutenir des développeurs talentueux.
