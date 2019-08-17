<!-- title: SMTP Relay avec Postfix -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

On trouve de l'information sur le relais SMTP avec Postfix un peu partout mais
pas toujours adapté à son cas.<!-- more --> Voici donc mon mémo, compilé à partir de
plusieurs sources, pour utiliser Postfix comme relais SMTP avec le fournisseur
Orange (sur le port 25 et authentifié en clair par un nom d'utilisateur et un
mot de passe).

Ajouter dans **/etc/postfix/main.cf** :

    # SMTP relay
    relayhost = smtp.orange.fr

    smtpd_sasl_auth_enable = yes
    smtp_sasl_security_options = noanonymous
    smtp_sasl_tls_security_options = noanonymous

    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    sender_canonical_maps = hash:/etc/postfix/sender_canonical

Créer un fichier pour définir l'authentification SMTP : **/etc/postfix/sasl_passwd**

    smtp.orange.fr [utilisateur]:[mot de passe]

Créer un fichier pour définir le *mapping* des expéditeurs : **/etc/postfix/sender_canonical**

    root [adresse expéditeur]

Ensuite il rester à créer une version *hash* des fichiers *sasl_passwd* et
*sender_canonical* et à relancer Postfix :

    $ postmap hash:/etc/postix/sasl_passwd
    $ postmap hash:/etc/postfix/sender_canonical
    $ /etc/init.d/postfix restart

On peut tester l'envoi d'un e-mail et vérifier dans le log **/var/log/mail.log** que l'envoi se passe bien :

    $ mail -s "Test depuis Postfix" [someone@somewhere.com]
    is it working?
    I hope so^D
