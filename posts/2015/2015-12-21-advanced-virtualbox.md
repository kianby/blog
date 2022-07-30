<!-- title: Quelques astuces pour VirtualBox -->
<!-- category: Virtualisation -->
<!-- tag: planet -->

VirtualBox est un produit de virtualisation porté par Oracle qui a l'avantage
d'être multi-plateforme (Ms Windows, OS/X, GNU/Linux)<!-- more --> et qui est orienté
*Desktop*, destiné à s'installer sur une machine de bureau (par opposition à un
hyperviseur dédié à la virtualisation). Le client cible de VirtualBox c'est
l'utilisateur lambda qui a besoin de tester occasionnellement une distribution,
l'utilisateur professionnel de GNU/linux (félicitations tu fais partie des 1%)
qui a besoin régulièrement d'une machine virtuelle Ms Windows pour certaines
applications (comme Ms Office), le développeur ou le testeur de logiciel qui
utilise intensivement la virtualisation pour déployer des environnements de
test. J'appartiens aux trois catégories. Je ne vais pas détailler la création
d'une machine virtuelle mais quelques astuces utiles, fruit de mon expérience
... bon ok de mes galères :-)

Dans le cadre professionnel, j'ai une machine virtuelle Ms Windows qui me sert
à éditer et créer des documents Office. Pour éviter de dupliquer les documents,
j'avais créé un partage Samba entre ma machine hôte et la machine virtuelle.
J'étais fier de moi, cela fonctionnait bien... jusqu'à que j'essaie d'accéder à
mes documents dans le TGV. La machine virtuelle était configurée en mode pont
(*bridge*) sur l'interface Ethernet et Ms Windows configuré en IP fixe sur le
réseau d'entreprise. L'interface Ethernet de la machine hôte étant KO, le
partage Samba n'était pas accessible par la VM.

Une solution consiste à utiliser la fonctionnalité "Dossiers partagés" de
VirtualBox. Au niveau de la configuration de la VM, les dossiers partagés
permettent de créer un partage Ms Windows qui pointe sur un répertoire du hôte
et qui sera accessible quelle que soit la configuration réseau de l'hôte ou de
la VM : réseau configuré en mode pont ou en NAT, que le réseau soit accessible
ou non.

**Configuration des dossiers partagés dans VirtualBox :**

![Shared Folders](/images/2015/virtualbox-shared-folder.png "Shared Folders")

**Navigation du partage depuis la VM Ms Windows :**

![Windows Share](/images/2015/virtualbox-windows-explorer.png "Windows Share")

Quand je déploie des VMs sur mon poste de développement pour des tests, je
configure le réseau de la machine virtuelle en mode NAT pour ne pas consommer
d'adresse IP du réseau d'entreprise et je configure le système d'exploitation
virtualisé (généralement un Linux) en DHCP. Dans cette configuration, c'est
VirtualBox qui attribue une adresse IP dynamique à la VM sur un réseau NAT
partagé entre le hôte et ses VMs. Du coup, la VM a accès au hôte, à son réseau
local du hôte (et même à Internet) mais elle est *invisible*  pour les autres
machines du réseau local. L'avantage de cette configuration c'est qu'elle
fonctionne si la machine hôte n'a pas de réseau : la machine hôte et la VM
peuvent toujours communiquer. Pour que le hôte puisse se connecter à un service
de la VM, il faut configurer la redirection de port avec VirtualBox, c'est à
dire lier un port local de la machine hôte à un port de la VM. Par exemple, on
peut définir qu'on veut accéder à la VM en SSH en liant le port 2222 au port 22.

![Port forwarding](/images/2015/virtualbox-port-forwarding.png "Port forwarding")

Ainsi un *ssh -p 2222 user@localhost* se connecte à la VM et on peut copier des
fichiers par le même biais avec *scp*. La redirection du port Web (80) de la VM
vers le port 8080 de la machine hôte permet d'accéder à une éventuelle
application Web de la VM. Cela posera peut-être des soucis car cette application
ignore le NAT et elle risque de construire des liens vers des ressouces sur le
port 80 alors qu'on l'attaque sur le port 8080. Un moyen de contourner ce
problème si l'application n'est pas configurable, consiste à installer un NginX
sur la machine hôte pour faire office de proxy.

```nginx
# Proxy

upstream vbox-vm {
  server 127.0.0.1:8080;
}

##
# Virtual Host Config
##

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
      proxy_pass  http://vbox-vm;
    }

}
```

Ainsi, on peut attaquer le port HTTP de la machine locale et avoir ses requêtes
redirigées vers le port HTTP de la VM. On n'a plus de changement de port donc
les liens sont valides.

Ces deux astuces me permettent de travailler avec mes VMs sur mon laptop de
développement en mode déconnecté.  Si vous en avez d'autres je suis preneur :-)
