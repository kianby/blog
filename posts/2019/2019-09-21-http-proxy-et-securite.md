<!-- title: Proxy HTTP et sécurité -->
<!-- category: Hébergement -->
<!-- tag: planet -->

Dans une modeste configuration d'hébergement de services Web, à moins de faire tourner ses services [monolithiquement]({{ site_url }}/2018/choix-du-systeme-pour-sauto-heberger/), on a souvent un serveur HTTP frontal qui porte le certifical SSL et redispatche les requêtes vers des applications réparties dans des machines virtuelles ou des containers. <!-- more -->

![Architecture Proxy HTTP]({{ site_url }}/images/2019/http-proxy.png)

La sécurité de mon serveur est assurée par le pare-feu (qui laisse passer uniquement les flux autorisés) et l'outil [fail2ban](https://github.com/fail2ban/fail2ban) qui rajoute des règles de blocage dans iptables en scrutant les logs systèmes et applicatifs. Les applications sont distribuées dans des containers et produisent leur log applicatif. Cela pose deux problèmes : 

1. le log de l'application est dans un container applicatif alors que l'outil de blocage fail2ban est dans le container frontal
2. le serveur HTTP du frontal fait office de proxy donc l'application ne connaît que l'adresse IP du frontal ; le log est  inexploitable pour bannir des intrusions.

Pour résoudre le point 1, il faut rapatrier les logs du container applicatif vers le frontal. C'est faisable de plusieurs manières, une simple, préservant l'indépendance du container, consiste à exporter le log en TCP/IP avec [rsyslog](https://www.rsyslog.com) et à configurer son écoute dans le container frontal.

Pour le point 2, il faut acheminer l'adresse IP réelle du visiteur vers le container applicatif. Techniquement, c'est déjà le cas en utilisant l'entête HTTP *X-Forwarded-For* dans la configuration HTTP mais l'application n'en tire pas forcément parti pour ses logs. C'est là que NginX propose un génial module [ngx_http_realip](https://nginx.org/en/docs/http/ngx_http_realip_module.html) qui permet au container applicatif de remplacer l'adresse IP reçue (celle du frontal) avec l'adresse IP réelle. 

Sur le NginX du frontal, on passe l'adresse IP réelle dans l'entête **X-Real-IP** :

    proxy_pass http://10.10.10.2;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP  $remote_addr;

Sur le NginX applicatif, on remplace l'adresse IP par l'adresse réelle :

    set_real_ip_from 10.0.0.0/8;
    real_ip_header X-Real-IP;
    real_ip_recursive on;

Avec cette configuration, le log applicatif contient les adresses IP réelles. Il est exporté vers le container frontal et des règles fail2ban peuvent être ajoutées pour l'exploiter et bannir des tentatives d'intrusion. 