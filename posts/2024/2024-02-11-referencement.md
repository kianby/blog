<!-- title: Référencement influencé -->
<!-- category: Hébergement -->

Tout est parti d'un service en bêta de surveillance des liens morts promu par Korben, [Bernard](https://bernard.app/) pour ne point le nommer. J'aime bien les chiens et j'utilise déjà [Bruno](https://www.usebruno.com/), le rapport est mince car Bruno est une alternative à Postman, une application de test des API Rest. Néanmoins cela m'a engagé à lancer Bernard sur la piste de mon blog et de constater qu'il tombe en décrépitude avec une centaine de liens cassés pour seulement 200 articles. Mon amour-propre a pris le dessus sur ma flemme et j'ai commencé réviser mes articles, d'abord avec Bernard puis très vite avec [Dead Link Checker](https://www.deadlinkchecker.com/) dont l'usage n'est pas limité. 

Pour les liens externes cassé, soit j'ai trouvé l'équivalent sur le site actuel quand cela avait du sens au vu du contexte où l'article a été rédigé à l'époque et j'ai corrigé le lien, soit j'ai supprimé le lien et laissé apparaître son URL en clair (pour les aficionado de Archive.org).

J'avais aussi plusieurs liens externe cassés aussi suite [à la dernière migration](/2020/bilan-hebergement-2020/). Facile à réparer et l'occasion de constater que cette migration a aussi fait disparaître beaucoup images, celles insérées sous forme de balise HTML "img src" car le rustique [Makesite](https://github.com/kianby/blog) supporte uniquement Markdown ; et c'est très bien ainsi. 

Néanmoins j'avais trois effets de présentation incroyables dans mes articles : l'image alignée à gauche entourée de texte, celle alignée à droite et l'image centrée. Après une consultation astrale sur... StackOverflow, j'ai retenu une solution que je trouve élégante à base de CSS en utilisant les ancres.  


```css
img[src*='#left'] {
    float: left;
    margin-left: 20px;
    margin-right: 20px;
}
img[src*='#right'] {
    float: right;
    margin-left: 20px;
    margin-right: 20px;    
}
img[src*='#center'] {
    display: block;
    margin: auto;
}
```

Exemple de source Markdown : 

```
![Jenkins Logo](/images/06x/jenkins-logo.png#left) Voici un logo 
centré à gauche et mon texte qui commence à coté. Incroyable !   
```

J'avoue que le coup des images disparues m'a déçu de moi-même. Et quand j'ai réparé tant bien que mal mes liens externes, j'ai constaté qu'énormément de petits sites avaient disparu ou avaient changés sans assurer des liens permanents eux-aussi. J'ai donc analysé les liens que je cassais pour autrui. J'ai commencé par un coup d’œil sur [ahrefs](https://ahrefs.com/broken-link-checker) qui effectue le même travail que Bernard : lancer des bots et fournir une offre tarifée pour consulter ses liens cassés : les liens sortants mais aussi les liens entrants. Ils peuvent proposer cela car ils ratissent l'Internet périodiquement donc les sites qui vous référencent. 

La version gratuite donne un aperçu des dégâts. Je n'ai effectivement pas tenté de préserver quoi que ce soit d'une migration à l'autre (Pelican, Hugo, Makesite). Même pas à minima l'adresse du flux RSS qui remplit mes logs NginX d'erreurs HTTP 404. J'ai commencé par fournir quelques redirections au niveau de la configuration NginX et je prévois de l'enrichir périodiquement en analysant les logs access de NginX. 


```nginx
# redirections to preserve inbound links
rewrite ^/feeds/all.atom.xml$ https://blogduyax.madyanne.fr/rss.xml redirect;
rewrite ^/migration-du-blog-sous-pelican.html$ https://blogduyax.madyanne.fr/2013/migration-du-blog-sous-pelican/ redirect;
rewrite ^/2017/nextcloud-securite/$ https://blogduyax.madyanne.fr/2017/securite-des-donnees-focus-sur-nextcloud/ redirect;
``` 

L'objectif n'était pas d'améliorer le référencement mais c'est une maintenance nécessaire pour ne pas disparaître des moteurs de recherche pour les quelques articles toujours d'actualité et aussi par respect pour les sites qui m'ont lié dans leurs articles.

