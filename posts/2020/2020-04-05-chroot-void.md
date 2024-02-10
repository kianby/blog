<!-- title: Installation de Void sur un VPS -->
<!-- category: Hébergement --> 

L'objectif est d'utiliser une distribution Void Linux  non proposée en standard  sur [un VPS Contabo](https://contabo.com/?show=vps) en réalisant une installation via CHROOT. <!-- more -->

Cet article a été écrit sur  la base de [la procédure du wiki](https://docs.voidlinux.org/installation/guides/chroot.html) et de [cet article du blog mitchriedstra.com](https://mitchriedstra.com/2018/12/void-on-digital-ocean) en adaptant à mes besoins et en mettant à jour certaines opérations obsolètes. 

## Procédure d'installation

Chaque hébergeur propose un mode de secours (souvent nommé *rescue* dans l'interface d'administration du serveur) pour reprendre la main sur un serveur en cas de souci. Cela consiste à démarrer un système minimal à partir duquel on pourra monter les partitions du disque principal pour essayer de réparer les choses. C'est cette porte de secours qui va nous servir à réaliser une installation manuelle de Void.

Au préalable j'ai réalisé une première installation standard avec une distribution supportée : Debian 10. Ainsi j'ai pu noter le paramètrage réseau configuré par Contabo sur le VPS : adresse IP, masque réseau, adresse de la passerelle, serveurs DNS. Ensuite j'ai redémarré en mode secours.

### Partitionnement et installation de l'image

Le partitionnement simple défini par Debian me suffit, je n'ai pas besoin de LVM ni de chiffrement.

	root@sysresccd /void % fdisk -l
	Disk /dev/loop0: 469.9 MiB, 492683264 bytes, 962272 sectors
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes


	Disk /dev/sda: 400 GiB, 429496729600 bytes, 838860800 sectors
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disklabel type: dos
	Disk identifier: 0x54d070ad
	
	Device     Boot   Start       End   Sectors   Size Id Type
	/dev/sda1  *       2048   1953791   1951744   953M 83 Linux
	/dev/sda2       1953792 838858751 836904960 399.1G 83 Linux

On reformate les deux partitions en EXT4 avec la commande *mkfs.ext4* : 

- sda1 qui contient */boot*
- sda2 qui contient */*

Ensuite on monte la partition */* dans laquelle on télécharge et décompresse l'image ROOTFS de Void Linux.

    mkdir /void
    mount /dev/sda2 /void
    cd /void
    wget https://a-hel-fi.m.voidlinux.org/live/current/void-x86_64-ROOTFS-20191109.tar.xz
    tar xJf void-x86_64-ROOTFS-20191109.tar.xz
    rm -f void-x86_64-ROOTFS-20191109.tar.xz

### Chrootage et installation du système de base  

On se chroote en quelques commandes :

    mount -t proc none proc
    mount -o bind /sys sys
    mount -o bind /dev dev
    chroot /void /bin/bash
    export PS1="(CHROOT) # ""

Le système cible a sa configuration IP mais plus sa configuration DNS ; on rémédie à cela en configurant le DNS Google.

    echo nameserver 8.8.8.8 > /etc/resolv.conf

On peut aussi éditer */etc/hostname* pour personnaliser le nom local de la machine avant d'installer le système de base de Void.

    echo repository=https://a-hel-fi.m.voidlinux.org/current/ >/etc/xbps.d/00-repository-main.conf
    xbps-install -Syu base-system curl wget grub gptfdisk lzop lzip xz libressl dracut sudo 

On génère le fichier */etc/fstab* 

    cat /proc/mounts | grep -E '(xfs|ext4)'  >> /etc/fstab

On vérifie quand même le contenu ;-) 

    (CHROOT) # cat /etc/fstab 
    #
    # See fstab(5).
    #
    # <file system>	<dir>	<type>	<options>		<dump>	<pass>
    tmpfs		/tmp	tmpfs	defaults,nosuid,nodev   0       0
    /dev/sda2 / ext4 rw,relatime,data=ordered 0 0

### Noyau et amorçage avec Grub

C'est le bon moment pour monter la partition */boot*

    mount /dev/sda1 /boot

On installe le kernel LTS puis on configure le boot

    xbps-install -S linux-lts
    grub-install --target=i386-pc /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg

>  Ne pas oublier de fixer un mot de passe pour le compte *root* avec la commande *passwd*

### Finalisation de l'installation

A cette étape, on a un serveur fonctionnel mais on ne pourra pas prendre la main si on redémarre. Il faut terminer la configuration réseau et configurer l'accès par SSH.

Sur Void, une configuration réseau statique se configure en éditant */etc/rc.local* 

    # Static IP configuration via iproute
    ip link set dev eth0 up
    ip -4 addr add 62.xxx.xxx.xxx/xxx dev eth0
    ip -4 route add default via 62.xxx.xxx.xxx dev eth0

On installe la configuration DNS préconisée par le fournisseur dans */etc/resolv.conf*  

    search invalid
    nameserver 213.xxx.xxx.xxx

Enfin on configure l'accès distant par SSH. Normalement, sshd a été installé avec le système de base, on n'a qu'à mettre le service en démarrage automatique :

    ln -sv /etc/sv/sshd/ /etc/runit/runsvdir/default/

Et on autorise la connexion du compte *root* par mot de passe en éditant */etc/ssh/sshd_config*

    permitRootLogin
    PasswordAuthentication yes

On renforcera la configuration SSH plus tard et on installera les outils de sécurité habituels (shorewall, fail2ban). Là, on peut tenter un redémarrage et vérifier qu'on peut accéder au serveur. 

Si ce n'est pas le cas, c'est qu'une étape a grandement foiré. On relance le serveur en mode *rescue*, on chroote et on analyse les logs pour essayer de comprendre ce qui a échoué. Mais il aussi possible que l'échec soit survenu avant le démarrage du serveur et un accès type KVM proposé par certains hébergeurs peut aider à comprendre. Chez Contabo, c'est un accès VNC qui m'a mis le nez sur mon Grub incorrectement installé le premier coup.  

![Grub cassé](/images/2020/broken-grub.png)

Bonne Void, une distribution qui mérite d'être connue !

 