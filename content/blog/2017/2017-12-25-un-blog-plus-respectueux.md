---
layout: post
title: Un blog plus respectueux
category: Blog
tag: planet
---

Je suis allé plus loin dans le respect de la vie privée sur le blog.<!-- more --> 

Quand on laisse un commentaire, l'adresse e-mail a toujours été optionnelle.
Elle sert à retrouver un avatar sur [Gravatar](https://fr.gravatar.com) et à
informer les abonnés de la parution d'un nouveau commentaire pour un article.
J'ai ajouté à [mon gestionnaire de
commentaires](https://github.com/kianby/stacosys) un mode *privé* qui
désactive la fonction d'abonnement et se passe de l'e-mail. En fait, l'e-mail
est résolu en avatar dans le navigateur avec quelques lignes de JavaScript et
il n'est pas pas envoyé au serveur, donc jamais stocké.

Le nouveau formulaire de ressemble à ceci : 

![Commentaire en JS](/images/2017/commentaire-js.jpg)

L'autre nouveauté, dans la même veine, c'est le support des navigateurs avec
le JavaScript désactivé. Mon article précédent [*un blog plus statique*](/2017/un-
blog-plus-statique/) a fait la moitié du travail en générant en pur HTML les
commentaires déjà postés. Il restait à donner la possibilité de laisser un
commentaire sans JavaScript, c'est chose faite avec un mode dégradé : 

- sans gestion de l'avatar
- sans prévisualisation en Markdown 

Le formulaire sans JavaScript ressemble à ceci :

![Commentaire sans JS](/images/2017/commentaire-nojs.jpg)

Il me semble normal de ne pas empêcher les lecteurs les plus soucieux de leur
vie privée d'accéder aux commentaires, c'est en phase avec les valeurs que je
prône ici.


