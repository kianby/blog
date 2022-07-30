<!-- title: Il court, il court, le furet -->
<!-- category: Humeur Containers -->

Il court, il court, le furet... ça résume à peu près mes semaines en ce moment.<!-- more --> Le thème de celle-ci (oui j'ai des semaines à thème) est la vente d'électro-ménager sur le site du Bon Coin (à ne pas confondre avec le bon sens près de chez vous) pour cause de rénovation. D'ailleurs si quelqu'un veut un frigo pas cher qu'il me contacte ;-) 

Mon expérience passée des annonces m'a définitivement vacciné d'afficher mon téléphone ou mon e-mail principal. Heureusement on peut masquer son téléphone le temps de s'assurer que la personne est vraiment interessée. Quant à l'e-mail, un jetable ferait l'affaire. Bon un jetable du style [10 minutes e-mail](https://10minutemail.com) c'est un peu court pour une annonce destinée à être publiée une semaine. Du coup il me reste deux options : 

1. créer un alias ou un e-mail chez moi puisque je suis maître de mon ~~destin~~ domaine
2. créer une boite chez un fournisseur

Je cherche un fournisseur respectable qui propose le service de transfert des e-mails pour tout rediriger sur mon e-mail principal. Je pensais que La Poste propose ce service mais il semble que cette époque soit révolue. Après quelques égarements avec des offres floues qui annoncent des options qui s'avèrent finalement payantes (n'est-ce pas Net-C) je finis chez un GAFAM et tant qu'à faire le plus gros de tous : Google... *applaudissements du lectorat en liesse, perte de ceux qui manquent d'humour* 

Alors Google c'est *all inclusive* : récupération des autres boites e-mail (miam miam de la donnée), transfert vers une autre boite (pas grave j'ai tout lu au passage), toutes les options avancées sont offertes. Au moins le contrat est clair : tu as un service haut de gamme mais tu paies avec tes données. Pas de souci, ils vont se régaler avec mes conversations dartyesque :-)

Bon utiliser Google d'accord, mais soyons un peu parano en évitant de transférer les e-mails vers ma boite principale ;  inutile de donner un lien facile à établir, faisons transpirer un peu leur IA. Je peux récupérer les e-mail à distance mais GMail râle dès qu'on active IMAP ou POP3 qu'il considère, à raison, comme des protocoles moins sécurisés. Je vais donc faire un rebond : GMail transfère tous les e-mails vers ma vénérable boite e-mail Free et je prévois de rapatrier celle-ci vers mon e-mail principal par POP3.

Bon rapatrier une boite e-mail par POP3 et faire un transfert SMTP c'est pas sorcier, il y a plein de documentation sur fetchmail / procmail / les relay MTA. C'est vrai et j'ai passé un couple d'heures à paramétrer tout cela pour finalement jeter l'éponge : manque de temps sur mon planning de furet et moins de goût à peaufiner une config système au poil pendant des heures. Du coup, j'ai mis ma casquette de codeur et réglé le problème par code en une heure de temps avec Python et ses librairies SMTP et POP3 incluses dans un projet nommé [popforward](https://github.com/kianby/popforward) ; *vous apprécierez ma créativité pour le nommage*. 

A ce stade, vous pensez : *"c'est bizarre il ne nous a pas encore bassiné avec Docker"*... j'y viens :-)

La mise en prod a pris 15 minutes chrono : écriture d'un docker-compose en utilisant [mon image pour les applications Python](https://hub.docker.com/r/kianby/pythonapp/) et déploiement sur le serveur de containers.

```docker
popforward:
  image: kianby/pythonapp:latest
  environment:       
    APP_NAME: popforward
    APP_CONFIG: /app/config.ini     
  volumes:
    - ${SOURCEDIR}/popforward:/app/popforward
    - ${DATADIR}/popforward/popforward.config.ini:/app/config.ini 
```

Bon... je retourne courir ! 

![furet](/images/2018/furet.jpg)

*[Photo by Alex Makarov on Unsplash](https://unsplash.com/photos/pIarqh5GU0I?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*

