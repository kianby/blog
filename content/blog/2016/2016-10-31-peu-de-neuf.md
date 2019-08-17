---
layout: post
title: Peu de neuf
category: Hébergement
tag: planet
---

Déjà Halloween ! Le temps à filé depuis mon dernier article sur ce blog.<!-- more --> J’écris
surtout des articles techniques à propos d’expérimentations système ou de
projets personnels en programmation. Et visiblement je suis plus fainéant depuis
le printemps dernier. Une autre excuse est que mon activité sur le réseau social
Diaspora, par mon compte sur [Framasphère](https://framasphere.org) (déjà 2 ans,
merci encore Framasoft) est devenue plus régulière, mais pas encore chronophage.
Parfois je balance une idée et un lien et cela aurait pu donner un vrai article
sur le blog avec un peu d’effort. C’est le plaisir de l’instantanéité qui
l’emporte sur la réflexion et le labeur. Et puis il y a aussi l’impression que
beaucoup de sujets sont déjà traités, des nouvelles plumes apparaissent dans le
flux du Planet, et c’est très bien.

De fait, je n’ai pas fait grand-chose de nouveau depuis le printemps.

J’ai tâté un peu de la gestion de conteneur LCX dans Debian et caressé l’idée de
cloisonner mes services hébergés. Mais rien n’est décidé pour l’instant. N’ayant
pas encore eu d’occasion d’expérimenter Docker professionnellement, je l’ai
aussi envisagé comme une opportunité de casser l’installation monolithique de
mon serveur et de tout repenser en services éclatés dans des conteneurs légers.
L’idée fait lentement son chemin. Docker c’est tout un univers avec ses outils
de déploiement, de supervision, d’orchestration, [sûrement pas un outil
parfait](https://blog.imirhil.fr/2016/10/09/docker-container-hell.html), mais il
est sûr que la conteneurisation succède à la virtualisation, comme elle-même
s’est imposée, sans équivoque, en son temps.

Ah, j’ai enfin installé une instance de Wallabag sur ma stack NginX / PHP /
MySQL, la moindre des choses après avoir profité plus d’un an du service
Framabag.

Et, surtout, j’ai repris la main sur mes e-mails. Depuis ma période
auto-hébergement un peu chaotique à cause d'une ligne ADSL peu fiable, j’avais
décidé de ne plus gérer mon propre serveur de mail car c’est un service trop
critique et j’avais laissé Gandi s’en occuper pour moi (c’est inclus avec la
gestion de mon nom de domaine). Au passage, le service Gandi est impeccable, ça «
juste marche » :-) Bref, le serveur étant désormais chez un hébergeur avec un
réseau fiable, j’ai remonté un serveur de mail avec la stack habituelle :
postfix, dovecot, spamassassin, roundcube. C’est toujours les mêmes outils, la
difficulté aujourd’hui, c’est d’avoir l’air honnête pour ne pas voir ses e-mails
refoulés : ce fut l’occasion de [s’intéresser à SPF, DKIM et DMARC](http://www.badsender.com/2014/01/13/delivrabilite-spf-dkim-dmarc) pour
authentifier ses e-mails.

Voilà, cela commence à faire une belle liste de services hébergés sur mon
serveur : le blog, son système de gestion des commentaires, les flux RSS (avec
TT RSS), les fichiers, les contacts et l’agenda synchronisés (grâce à Cozy
Cloud), et puis les e-mails.

Bon je vous laisse, on vient de sonner, c’est pour du racket de bonbons :-)
