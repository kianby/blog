<!-- title: Retour en auto-hébergement -->
<!-- category: Hébergement -->

Après une dizaine d'années à héberger mes services chez différents hébergeurs je reviens à de l'auto-hébergement sur du matériel à la maison. Et quelle évolution au niveau matériel : en 2013 c'était un portable Céléron peut véloce dans un placard. En cette fin d'année j'ai acquis un mini-pc sur les conseils avisés de [MiniMachines](https://www.minimachines.net) : un Beelink Mini S12 Pro: pour la taille d'un Rubik's Cube on a un processeur Intel N100 (de la famille Alder Lake) appuyé par 16 Go de RAM et 512 Go de stockage en M.2. Ça coûte un peu plus de 200 euros et c'est très raisonnable par rapport à ce qu'on obtient en retour : une machine avec une consommation électrique sobre, quasi-silencieuse et des performances suffisantes pour des usages standards en auto-hébergement.

Pour moi l'objectif est double : 
- financier d'abord avec l'opportunité de réduire mes factures bien que je sois très satisfait de mes services externes : résilier le cloud Infomaniak et le petit VPS me fera économiser d'une bonne centaine d'euros par an.
- apprendre en s'amusant : refaire de l'administration système, découvrir des nouveaux services à héberger, ça ouvre plein de possibilités. 

Joli projet sur le papier mais moins simple qu'en 2012 car l'Internet est sacrément plus hostile et une grosse réflexion sur la sécurité s'est imposée avant d’ouvrir quoi que ce soit sur Internet. Finalement la solution sera basée sur l'hyperviseur Proxmox qui apporte une souplesse sur les types de déploiement en permettant de mixer des conteneurs LXC et des machines virtuelles KVM et d'apporter une brique de sécurité avec un pare-feu à multiple niveaux. Le but étant d'isoler autant que possible les parties exposées du réseau domestique. Les machines virtuelles [regrouperont des services Docker](https://github.com/kianby/selfhosting/tree/config-vm1) exposés indirectement par un proxy NginX.

![Proxmox](/images/2024/proxmox.svg)

Le proxy NginX est directement exposé sur Internet via une redirection des ports HTTP / HTTPs depuis la box internet. C'est un container LXC Alpine avec une installation de [Nginx Proxy Manager](https://nginxproxymanager.com/) modifiée pour que les services ne s'exécutent par avec le super-utilisateur *root*. Le minimum de paquets est installé (surtout pas de service SSHD ni de SSH) et il s'administre par l'interface Web de Nginx Proxy Manager depuis le réseau local qui n'est évidemment pas exposée à l'extérieur. Il a deux cartes réseau virtuelles : une adresse sur le réseau local et l'autre sur le réseau privé constitué des machines virtuelles exécutant les services. Le proxy sert aussi de passerelle de sortie aux machines virtuelles : le routage est activé entre les deux interfaces et l'interface du réseau privé est *bridgée* sur l'interface réseau locale.

Les machines virtuelles exécutant les services appartiennent au réseau privé et le pare-feu de l'hyperviseur bloque le trafic pour qu'elles ne puisse communiquer qu'avec la passerelle. En cas de compromission elles n'ont accès ni au réseau local ni au bastion. Chaque machine virtuelle est accessible par SSH depuis le bastion, qui est un simple conteneur LXC Alpine avec deux cartes réseau qui permet par rebond d'accéder aux machines virtuelles depuis un PC du réseau local. Excepté la console Web de Proxmox c'est le seul moyen d'accéder aux machines virtuelles. Les accès SSH sont protégés par échange de clefs (aucun accès autorisé par mot de passe) et seul le bastion est autorisé. Corollaire : n'importe quelle machine du réseau local ayant un accès SSH au bastion peut accéder aux machines virtuelles.

![Archi réseau](/images/2024/archi-lan.svg)

Voilà c'est sûrement perfectible mais j'ai jugé la solution suffisamment sécurisée pour la mettre en service. La machine "vm2" avec Nextcloud et Immlich est encore un projet mais la machine "vm1" exécutant tous mes services de base est déjà opérationnelle.


