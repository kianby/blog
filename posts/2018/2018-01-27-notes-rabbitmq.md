<!-- title: Mes notes sur RabbitMQ -->
<!-- category: Développement -->

[RabbitMQ](https://www.rabbitmq.com) est un bus de messages Open Source qui
implémente le protocole Advanced Message Queuing (AMQP). Sa fonction est de
faire communiquer entre eux des programmes différents, potentiellement écrits
dans différents langages.<!-- more --> Le serveur RabbitMQ est lui-même écrit dans le
langage de programmation Erlang, ce qui est plutôt atypique. Aucune
connaissance de Erlang n'est nécessaire pour l'utiliser. C'est un produit
édité par Pivotal, un spin-off de VMWare et EMC, connu de tous les
développeurs JAVA pour son fabuleux framework
[Spring](https://en.wikipedia.org/wiki/Spring_Framework).

RabbitMQ demande une complexité de configuration proportionnelle aux exigences
demandées : queues de messages persistantes, dead letters, haute
disponibilité, optimisation des performances... Pour les configurations
compliquées et le support technique avancé dans des mises en oeuvre
d'entreprises, il y a des experts (j'ai une adresse pour ceux intéressés).
Pour une utilisation basique, dans un cadre de développement pépère à la
maison, RabbitMQ est très accessible, bien documenté et permet d'avoir
rapidement un bus de message pour faire communiquer ses applications.

Je m'en sers actuellement pour faire discuter mon petit éco-système hébergé. Dans ce cadre j'ai pris quelques notes sur sa mise en place, de l'installation à la configuration de base. 

### Installation 

Choix de l'OS : CentOS 7

Page d'aide de référence pour l'installation : https://www.rabbitmq.com/install-rpm.html

Pivotal fournit une installation d'une version allégée de Erlang avec les dépendances nécessaires à RabbitMQ : https://github.com/rabbitmq/erlang-rpm 

Et bien sûr, il fournissent aussi un RPM de RabbitMQ (actuellement en version 3.7.2-1) : https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.7.2/rabbitmq-server-3.7.2-1.el7.noarch.rpm

Gestion du service à la sauce CentOS : 

    # démarrer le service 
    /sbin/service rabbitmq-server start

    # stopper le service
    /sbin/service rabbitmq-server stop

    # démarrage automatique du service
    chkconfig rabbitmq-server on

Après avoir mis le service en démarrage automatique, on n'utilisa plus que l'outil *rabbitmqctl* :

    # démarrer le serveur rabbitmq
    rabbitmqctl start_app

    # stopper le serveur rabbitmq
    rabbitmqctl stop_app

### Droits et permissions 

Par défaut, un utilisateur *guest* (mot de passe idem) est créé et il est
attaché à l'interface réseau locale (localhost). Pour se connecter depuis une
autre machine, en distant, il faut créer un nouvel utilisateur.

    rabbitmqctl add_user admin <mot de passe dur>
    rabbitmqctl set_user_tags admin administrator
    rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

### Interface Web d'administration

Une belle interface permet de gérer la configuration et de visualiser des
indicateurs de fonctionnement. C'est un plugin qu'on active en ligne de
commande avec *rabbitmq- plugins*

    rabbitmq-plugins enable rabbitmq_management

L'interface Web répond à l'adresse *http://server-name:15672/cli/*

L'utilisateur *guest* n'a accès à l'interface que par localhost. Le nouveau compte admin est nécessaire pour se connecter en distant.

Si l'interface Web est derrière un proxy NginX et qu'elle répond à une sous-URL du domaine, la config pour pour une sous-url */rabbitwebmin* est la suivante : 

    location /rabbitwebmin/ {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        rewrite ^/rabbitwebmin/(.*)$ /$1 break;
        proxy_pass http://192.168.2.1:15672;
    }

Optionnellement, on peut installer [le CLI de rabbitmqadmin](https://www.rabbitmq.com
/management-cli.html) en téléchargeant le programme (Python) depuis
https://raw.githubusercontent.com/rabbitmq/rabbitmq-
management/v3.7.2/bin/rabbitmqadmin et en le plaçant dans */usr/local/bin*.

### Mise en oeuvre 

On crée un utilisateur technique pour nos applications dans un virtual host spécifique.

    rabbitmqctl add_vhost devhub
    rabbitmqctl add_user techuser tech
    rabbitmqctl set_permissions -p devhub techuser ".*" ".*" ".*"

A ce niveau, on peut essayer de faire communiquer deux applications à travers Rabbit avec un classique producteur-consommateur écrit en Python, utilisant [la librairie Pika](https://pika.readthedocs.io), dérivé du tutorial de RabbitMQ.

Code du producteur :

```python
#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('techuser', 'tech')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.2.1',credentials=credentials, virtual_host="devhub"))
channel = connection.channel()

channel.exchange_declare(exchange='hub.topic',
                            exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='hub.topic',
                        routing_key=routing_key,
                        body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
```

Code du consommateur :

```python
#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('techuser', 'tech')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.2.1',credentials=credentials, virtual_host="devhub"))
channel = connection.channel()

channel.exchange_declare(exchange='hub.topic',
                            exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print("Queue => " + queue_name)

# on s'abonne aux topics : 
binding_keys = ['mail.message', 'mail.command.*']

for binding_key in binding_keys:
    channel.queue_bind(exchange='hub.topic',
                        queue=queue_name,
                        routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(channel, method, properties, body):
    print("=>  %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                        queue=queue_name,
                        no_ack=True)

channel.start_consuming()
```

Quelques tests : 

    # le consommateur lancé dans un shell s'abonne aux topics mail.message et mail.command.*
    $ python3 consumer.py 

le consommateur doit recevoir le message suivant : 

    # le producteur produit dans le topic 'mail.message'
    $ python3 producer.py "mail.message"

le consommateur doit recevoir le message suivant : 

    # le producteur produit dans le topic 'mail.command.test'
    $ python3 producer.py "mail.command.test"

le consommateur ne doit pas recevoir le message suivant : 

    # le producteur produit dans le topic 'mail.rate'
    $ python3 producer.py "mail.rate"
