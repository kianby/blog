<!-- title: NginX est brillant -->
<!-- category: GNU/Linux -->

NginX est brillant ; à chaque fois que je me suis demandé "est-ce qu'il y a un moyen de faire ça ?", j'ai trouvé une solution assez rapidement. 

Ma dernière interrogation était de sécuriser un site avec une connexion par utilisateur / mot de passe mais désactiver cette authentification pour les connexions depuis une adresse IP de confiance. Et bien c'est faisable avec le module geo. 

```nginx
geo $authentication {
    default "Authentication required";
    # mes adresse de confiance
    127.0.0.1 "off";
    176.149.25.33 "off";
}

server {    
    location /monpetitsite {        
        auth_basic $authentication;
        auth_basic_user_file /etc/nginx/.htpasswd;
        # la suite
    }
}
```

et il n'y a plus qu'à créer le fichier .htpasswd avec mon USER et PASSWORD de connexion.

```sh
printf "USER:$(openssl passwd -crypt PASSWORD)\n" >>.htpasswd
```

Il y a des outils qui font aimer l'informatique, NginX en fait clairement partie.
