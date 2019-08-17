---
layout: post
title: Choix du système pour s'auto-héberger
category: Hébergement
tag: planet
---

Suite à un échange intéressant sur le choix d’une distribution dans Diaspora,
j'ai eu envie de developper le sujet dans un article.<!-- more --> je restreins au choix
d'un système d'exploitation pour de l'auto-hébergement (à la maison ou chez un
hébergeur avec une offre de serveur physique dédié) car je ne me sens plus
assez qualifié pour parler de choix d'entreprise, m'étant recentré sur le
développement ; bon je glisserai quand même quelques avis et les adminsys en
activité commenteront.

En une quinzaine d’années, le choix d’un système a traversé trois phases
successives : de **"le meilleur système c'est Gloup"** (remplacez Gloup par
votre système d'exploitation préféré), à **"le meilleur système c'est TOUS"**,
nous sommes arrivés à **"le meilleur système c'est AUCUN"**.

### Phase 1 : le monolithe

<img src="/images/2018/monolithe.jpg" style="float:left; margin: 0px 20px;"/>Le serveur est monolithique donc le choix du système d'exploitation est crucial.

En entreprise, il dépend de la politique interne, des goûts et compétences des
administrateurs système. Généralement on limite la fragmentation des systèmes
déployés. On choisira par exemple RedHat pour les serveurs critiques et CentOS
pour les autres afin d'avoir une homogénéité. Des besoins particuliers (comme
le pare-feu) pourront amener à installer des systèmes spécifiques (comme
PFSense).

Dans le cas de l'auto-hébergement, c'est open bar et nul besoin de se
justifier. On choisit Gloup parce que c'est cool et qu'on veut appendre à le
maîtriser, ou bien parce qu'on pense que c'est le meilleur choix technique (ou
philosophique).

Ce qu'il faut savoir c'est que ce système fournit de base une logithèque plus
ou moins étendue par son gestionnaire de paquets. S'il manque des choses, on
peut ajouter d'autres sources, comme des dépôts tiers de contributeurs. En
dernier ressort, on peut compiler à partir des sources, ce qui peut être un
vrai travail de portage si le programme en question n'est pas prévu pour ce
système. On est très dépendant des versions proposées par le système
d'exploitation et si on a besoin de faire coexister plusieurs versions d'un
même programme, ça commence à se compliquer grandement. Quand on montera en
version le système d'exploitation, tous ces ajouts *non standard* (paquets non
officiels, programmes compilés à partir des sources) compliqueront la mise à
jour du système d'exploitation.

### Phase 2 : pas de limite

Et puis est apparue la virtualisation ! le choix du système d'exploitation
n'est plus une limitation, on mixe à son gré et le système hôte (appelé
hyperviseur) a le rôle principal d'exécuter avec célérité les machines
virtuelles. On a encore une petite adhérence à l'architecture matérielle : si
on tourne sur une architecture x86, on doit installer des systèmes supportant
cette architecture. La virtualisation a un coût même si elle s'appuie sur des
instructions dédiées du processeur pour être très performante.

Sur du matériel modeste, ce qui est souvent le cas en auto-hébergement, on
privilégiera les technologies de conteneurs (LXC pour Linux, Jails pour
FreeBSD) pour isoler ses services et faire cohabiter des versions spécifiques
ou différentes. Les conteneurs sont plus limités que les machines virtuelles
car ils partagent le kernel du système hôte. Sur un serveur Linux, des
containers LXC pourront exécuter différentes distributions GNU/linux, mais
seulement du Linux. Cela permet déjà de faire plein de trucs cool, chaque
conteneur a son IP, on choisit le système le plus adapté à ce qui sera
installé dessus (Debian CentOS, Alpine, ...).

Si on a confiance dans ce qui s'exécute sur ses conteneurs (ce qui devrait
être le cas en auto-hébergement perso), l'approche de la sécurité du serveur
est simple : un gros pare-feu au niveau du serveur physique pour n'ouvrir que
les ports publiques sur Internet et les conteneurs peuvent communiquer entre
eux par des adresses privées.  

### Phase 3 : centré sur l'application

Puis Docker a lancé sa technologie de conteneur d'application, basé
techniquement sur les conteneurs Linux LXC mais avec l'enjeu de faire oublier
le système sous-jacent :

- un conteneur Docker = une application (le processus en PID 1)
- un portail d'applications permet de télécharger des images prêtes à l'emploi
- les dépendances entre conteneurs sont déclarées explicitement

Le tout s'accompagne d'un ensemble de bonnes pratiques : pas de données dans
les conteneurs d'applications, une configuration passée au conteneur lors de
son initialisation. Bref je vais pas détailler, plein de bons articles sur le
sujet ont déjà été publiés. Mais c'est une technologie qui vaut la peine de
jouer d'être essayée. Elle ne révolutionne pas la technique sous-jacente qui
existait déjà mais les usages et la façon de repenser un déploiement de
services, réparti entre plusieurs conteneurs faciles à mettre à jour, une
abstraction totale par rapport au système hôte.

Ne nous voilons pas la face, Docker c'est la fin de la distribution serveur.
Est-ce que Debian est mieux que CentOS sur un serveur ? On s'en cogne car peu
importe la logithèque la distribution et les versions fournies de chaque
librairie. En installant Docker dessus, on en fait un chef d'orchestre dont le
rôle se limite à exécuter des dizaines ou des centaines de conteneurs. Et le
catalogue d'applications est énorme, comme les versions proposées. Et si on ne
trouve pas vie ou qu'on a besoin d'empaqueter ses propres applications en
conteneurs Docker, on apprend à fabriquer ses propres conteneurs en quelques
heures d'auto-formation.

Bon j'ai l'air emballé sur Docker et c'est le cas, d'un point de vue
professionnel. Ce n'est pas mon rêve pour mon auto-hébergement, les conteneurs
ont tous la même taille, ça manque de diversité et de fun pour moi.


<img src="/images/2018/havefun.jpg" style="float:left; margin: 0px 20px;"/>La
plupart des entreprises sont entre la phase 2 et la phase 3 : elle ont
virtualisé tout ce qui est possible et elles migrent des services sous
Docker.

Mais que choisir, au final, pour de l'auto-hébergement ? Et bien, je dirais :
**"faîtes vous d'abord plaisir"**. BSD, Linux, il y a de quoi faire. Quitter
le monolithique et passer à l'étape 2 ou 3 ouvre d'autres perspectives dans la
gestion de son serveur. Fan du pare- feu PF ? ajoutez une machine virtuelle
avec PFSense pour gérer la sécurité de votre serveur. Si professionnellement
vous risquez d'être concernés par Docker, formez-vous parce que c'est
intéressant et que ça peut être utile (mais ne baclez pas l'aspect sécurité
des containers). Moi j'ai une passion pour les conteneurs *maison* qui me
permettent de moduler à ma guise : des petits conteneurs avec l'esprit Docker
pour les micro- services (avec Alpine Linux), des gros conteneurs pour les
applications plus conséquentes (comme Nextcloud). Longue vie à l'auto-
hébergement, profitons-en tant que l'Internet n'est pas à péage :-)
