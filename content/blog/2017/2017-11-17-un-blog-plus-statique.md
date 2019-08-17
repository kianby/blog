---
layout: post
title: Un blog plus statique
categories: Hébergement Blog
tag: planet
---

Un échange avec [Bruno Adelé](http://bruno.adele.im), qui fut l'initiateur du
projet CaCause à une époque (déjà 5 ans) où les blogs statiques n'avaient pas
d'autre alternative que Disqus, a titillé mon intellect.<!-- more --> Bruno envisage de
migrer son blog vers [Hugo](https://gohugo.io) et d'utiliser le gestionnaire
de commentaires [staticman](https://staticman.net) dont la particularité est
de soumettre les commentaires par des pull-request GIT. 

Cela m'a rappelé [le projet Pecosys](https://blogduyax.madyanne.fr/2014
/pecosys-les-commentaires-avec-pelican) qui avait une approche similaire : les
commentaires étaient partie intégrante du blog, publiés dans GIT sous forme de
fichiers au format Markdown et convertis en HTML par le moteur de blog
Pelican. La complexité de mise en oeuvre de Pecosys (un dépôt GIT privé, un
e-mail dédié, un plugin spécifique pour Pelican) ont eu raison du projet. Deux
ans plus tard, je codais Stacosys en simplifiant un peu les pré-requis
système. Entre temps, des alternatives crédibles à Disqus avaient vu le jour
comme [Isso](https://posativ.org/isso) notamment. Stacosys est donc resté un
projet personnel et depuis, il gère les commentaires de ce blog.

Dans Stacosys, les commentaires ne font plus partie des sources du blog. le
navigateur Web du lecteur communique directement avec Stacosys via une API
REST et une instance de Stacosys peut être partagée entre plusieurs sites par
[des requêtes CORS](https://fr.wikipedia.org/wiki/Cross-
origin_resource_sharing). Stacosys stocke les commentaires dans sa base de
données et il ne fait plus de GIT. Contrairement à Pecosys (PElican COmment
SYStem), Stacosys n'est pas lié à un moteur de blog particulier, il est
facilement intégrable dans une page HTML par un peu de JavaScript.

![Architecture actuelle Stacosys](/images/2017/schema-stacosys-avant.jpg)

Au vu de mon utilisation mono-site de Stacosys je me suis demandé si je ne
pourrais pas revenir à une génération des commentaires en pages statiques.
Cela apporte plusieurs avantages :

- une plus grande rapidité de navigation : au lieu d'ajouter les commentaires à la page en asynchrone par JavaScript, ils font partie de la page
- la capacité à supporter plus d'utilisateurs simultanés car le serveur HTTP ne sert que des ressources statiques
- plus de sécurité sur mon serveur grâce une surface d'attaque réduite : plus besoin d'une application HTTP REST accessible sur Internet

L'idée n'est pas réécrire Stacosys mais de pouvoir l'utiliser dans les deux cas
de figure : mono-site et multi-site.

Le moteur de blog Hugo fournit une solution technique élégante à travers [les
data templates](https://gohugo.io/templates/data-templates). Il s'agit de
récupérer de l'information pendant la construction du blog pour enrichir les
pages avec une information dynamique (qui peut changer à chaque build). On
peut lire des fichiers JSON sur disque, ou mieux, faire des requêtes HTTP pour
récupérer du JSON.

Ca tombe bien, Stacosys fournit une API REST qui renvoie du JSON :-) Ni une ni
deux, j'ai adapté mes modèles pour que Hugo interroge Stacosys pendant sa
phase de build et génère les articles en incluant les commentaires en fin de
page.

Voici le *template* Hugo des commentaires qui utilise la fonction **getJSON** pour récupérer les commentaires
de la page en cours :

``` html
{% raw %}
    <div id="stacosys-comments">
      {{ $restParam := (printf "/comments?token=%v&url=%v" .Site.Params.widgets.stacosys_token .URL) }}
      {{ $resp := getJSON .Site.Params.widgets.stacosys_url $restParam }}
      {{ range $resp.data }}    
      <hr>
      <div class="inline">
        {{ if isset . "site" }}
          <a href="{{ .site }}">
        {{ end }}
        <img src="http://www.gravatar.com/avatar/{{ .avatar }}.jpg" style="float:left; margin-right:10px" height="32" width="32">
        {{ if isset . "site" }}
          </a>
        {{ end }}
          <span class="title">{{ .author }}</span>
          <span> - {{ .date }}</span>
      </div>
      <p>
      {{ .content | markdownify }}
      </p>
      {{ end }}
    </div> 
{% endraw %}    
```

et un exemple de données renvoyée par Stacosys :

``` json
{% raw %}
    {
      "data": [
        {
          "author": "Bruno",
          "avatar": "b97a3605714350fdad083394c974a9b4",
          "content": "Ça donne effectivement envie de se laisser convaincre par un Librem. Le seul problème c'est que c'est déjà limite si j'ai un téléphone mobile et payer un tel prix alors que je pourrais pratiquement avoir un nouvel ordinateur au même montant, ça ne donne pas trop envie. Quand mon téléphone actuel cessera de fonctionner, peut-être que je choisirai plutôt de ne pas en racheter.",
          "date": "2017-10-01 20:03:46"
        },
        {
          "author": "Yax",
          "avatar": "308a3596152a79231f3feedc49afa4ef",
          "content": "Je comprends c'est pas mon budget téléphone non plus. Une alternative acceptable c'est le reconditionné de téléphones éprouvés et connus pour être bien supportés par les ROMs communautaires. Ça fait un peu d'écologie en prime.",
          "date": "2017-10-01 22:20:37"
        }
      ]
    }
{% endraw %}
```

Il reste une interaction entre le serveur HTTP et Stacosys pour poster des
commentaires via le formulaire mais on n'a plus besoin que Stacosys ait son nom
FQDN propre et soit exposé sur Internet.

Le nouveau système ressemble à ceci :

![Nouvelle architecture Stacosys](/images/2017/schema-stacosys-apres.jpg)

Les sources complets sont sur [mon Github](https://github.com/kianby).

C'est en place depuis le début de la semaine et je suis ravi du résultat.
Combiné avec un Firefox Quantum pour la navigation ça roxe du poney !

