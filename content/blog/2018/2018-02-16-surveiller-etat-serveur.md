---
layout: post
title: Surveiller l'état du serveur
category: Hébergement
tag: planet
---

J'ai un peu compliqué l'installation de mon serveur en répartissant les
services dans des conteneurs. J'ai un serveur HTTP NginX en frontal qui
distribue les requêtes vers les bon conteneurs<!-- more --> en fonction du nom DNS (un
reverse proxy). Je me retrouve donc avec une dizaine de conteneurs, partageant
un même plan d'adressage IP, et presque autant de serveurs HTTP. J'ai eu
besoin d'un outil qui me donne une vision globale de l'état du serveur et soit
capable de m'alerter en cas d'incident.

J'aurais pu m'orienter vers des solutions de supervision (Nagios et autres),
surtout vu mon background sur le sujet, mais le besoin est simple et les
ressources de mon serveur sont limitées. Je n'ai pas jugé utile de dégainer
la grosse artillerie. J'avais noté l'existence de
[Cachet](https://cachethq.io), utilisé, notamment, [par
Framasoft](https://status.framasoft.org), qui fournit une page de statut et
gère les notifications (e-mail ou abonnement RSS). Cachet, pour les intimes,
se cantonne donc à la visualisation et la notification. On crée des
composants, on les regroupe à sa guise, et une API Rest permet d'alimenter en
événements : changer l'état d'un composant (opérationnel, hors service,
partiellement défaillant), déclarer une maintenance planifiée. Il y a aussi
des indicateurs mais je n'ai pas encore exploré cette possibilité.

Comme pleurniché dans Diaspora, le plus dur c'est de l'installer, surtout
quand je rate la ligne importante du manuel qui précise que PHP 5 est requis
(la version 7 n'est pas encore supportée). Je me retrouve avec des erreurs
bizarres sans lien évident avec la version (du moins quand on n'est pas
PHPiste confirmé). Après une relecture du guide d'installation, plutôt bien
fait, et correction de mon déploiement, l'installation se déroule sans
problème avec Composer qui télécharge et installe les dépendances. Cachet est
prévu pour un grand nombre d'utilisateurs donc une base MySQL ou PostgreSQL
est recommandée. Pour peu d'utilisateurs il peut fonctionner avec SQLite, mon
choix de prédilection, quand c'est possible, pour ne pas multiplier les
serveurs de base de données, ni partager un serveur de base de données entre
mes conteneurs.

Une fois installé et la configuration HTTP mise en place, on accède à
l'interface d'administration pour créer ses objets. J'ai créé un groupe
**Système** avec tous mes conteneurs et un groupe **Service** avec mes
services critiques.

![Cachet Admin](/images/2018/cachet-admin.png)

Pour animer les statuts des composants c'est donc indépendant de Cachet. L'API
REST de Cachet est bien pensée et bien documentée. Elle permet de créer /
modifier des objets ou de les animer. Je me suis limité à cette dernière
possibilité pour l'instant en développant un programme qui récupère l'état des
conteneurs, des services et envoie les changements d'etat à Cachet. Ce
programme est exécuté toutes les 5 minutes. C'est sans prétention et ça répond
à mon besoin ; le code source est [ici](https://github.com/kianby/cachetmonitor).

Ma page de statut est accessible ici : https://status.madyanne.fr

