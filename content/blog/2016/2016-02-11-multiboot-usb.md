---
layout: post
title: Construire sa clef USB multiboot
category: GNU/Linux
tag: planet
---

J'ai essayé quantité d'utilitaires pour créer facilement une clef USB multiboot
et aucun ne fonctionne correctement sur des serveurs racks<!-- more --> (du type Dell
PowerEdge). Ces utilitaires ont en commun d'utiliser syslinux et de proposer
une interface graphique conviviale pour glisser-déposer des ISO sur la clef. Je
ne suis pas (encore) expert en partitionnement et boot mais je m'y intéresse
beaucoup en ce moment par la force des choses et on voit beaucoup de subtilités
pour booter sur du GPT au lieu de MBR. A force de chercher le bon utilitaire,
je suis tombé sur de la doc Archlinux (et oui encore) qui propose de créer
soi-même sa clef avec **GRUB** au lieu de **syslinux**. Cela veut dire qu'on ne
peut démarrer que des GNU/Linux et pas des utilitaires DOS (comme il y en a
quantité pour tester les disques ou la mémoire), c'est parfait, c'est la seule
chose que je fais. Cette documentation ArchLinux [est accessible à cette
adresse](https://wiki.archlinux.org/index.php/Multiboot_USB_drive).

Cet article est donc surtout un mémo pour moi même qui reprend les parties de
cette doc pertinentes pour mon cas d'usage  J'ai besoin d'avoir le live CD de
CloneZilla et Knoppix ainsi que le DVD d'installation de CentOS 7 et Debian 8.
Je suis parti d'une clef de 16 Go sur laquelle j'ai une table de partition GPT
et une partition unique formatée en EXT2. J'avais commencé avec une partition en
FAT32 mais on ne peut pas copier un fichier de plus de 2Go. Hors dans notre
cas, on va copier les ISO sur la clef et laisser GRUB les monter pour y
accéder. C'est différent des solutions basées sur syslinux où l'ISO est
désarchivée sur la clef dans un répertoire  Bref une ISO DVD d'installation de
CentOS pèse 4 Go donc on formate en EXT.

Voici ma table de partition :

    $ fdisk -l /dev/sdf

    Disque /dev/sdf : 14,5 GiB, 15504900096 octets, 30283008 secteurs
    Unités : secteur de 1 × 512 = 512 octets
    Taille de secteur (logique / physique) : 512 octets / 512 octets
    taille d'E/S (minimale / optimale) : 512 octets / 512 octets
    Type d'étiquette de disque : gpt
    Identifiant de disque : 34793BF6-88B6-4325-98D8-BD79DC297619

    Device     Start      End  Sectors  Size Type
    /dev/sdf1   2048 30282974 30280927 14,4G Linux filesystem

Ensuite, on crée un répertoire pour accueillir GRUB et les ISO :

    $ mount /dev/sdf1 /mnt
    $ mkdir -p /mnt/boot/iso

Et on installe GRUB :

    grub-install --force  --target=i386-pc --recheck --boot-directory=/mnt/boot /dev/sdf

Il reste à copier les ISO dans le répertoire */mnt/boot/iso* et à créer un
fichier *mnt/boot/grub/grub.cfg*. Tout le problème est de configurer correctement
GRUB pour monter chaque type de distribution. Pour certaines, il n'y a pas de
solution pour que ça fonctionne. Le documentation ArchLinux liste la
configuration GRUB pour un certain nombre de distributions.

Voici ma configuration **/mnt/boot/grub/grub.cfg** pour les distributions installées sur ma clef :

    # path to the partition holding ISO images (using UUID)
    set imgdevpath="/dev/disk/by-uuid/53ac1278-3d48-4528-a348-2eb3b7b8dc93"

    # define globally (i.e outside any menuentry)
    insmod search_fs_uuid
    search --no-floppy --set=isopart --fs-uuid 40c8461c-a5fd-4b3b-9a78-f8e92275ea98
    # later use inside each menuentry instead
    loopback loop ($isopart)$isofile

    menuentry "Live clonezilla-live-2.4.2-61-amd64" {
        set isofile="/boot/iso/clonezilla-live-2.4.2-61-amd64.iso"
        loopback loop $isofile
        linux (loop)/live/vmlinuz findiso=$isofile boot=live union=overlay username=user config
        initrd (loop)/live/initrd.img
    }

    menuentry "Live clonezilla-live-2.2.2-32-i686-pae" {
        set isofile="/boot/iso/clonezilla-live-2.2.2-32-i686-pae.iso"
        loopback loop $isofile
        linux (loop)/live/vmlinuz boot=live live-config noswap nolocales edd=on nomodeset ocs_live_run=\"ocs-live-general\" ocs_live_extra_param=\"\" ocs_live_keymap=\"\" ocs_live_batch=\"no\" ocs_lang=\"\" GRUB_GFXMODE=1024x768 ip=frommedia nosplash toram=filesystem.squashfs findiso=$isofile
        initrd (loop)/live/initrd.img
    }

    menuentry "Live Knoppix_v7.6.1DVD-2016-01-16-EN" {
            set isofile="/boot/iso/KNOPPIX_V7.6.1DVD-2016-01-16-EN.iso"
            loopback loop $isofile
            linux (loop)/boot/isolinux/linux bootfrom=/mnt-iso/$isofile acpi=off keyboard=fr lang=fr
            initrd (loop)/boot/isolinux/minirt.gz
    }

    menuentry "Install CentOS-7-x86_64-DVD-1511" {
        set isofile="/boot/iso/CentOS-7-x86_64-DVD-1511.iso"
        loopback loop $isofile
        linux (loop)/isolinux/vmlinuz noeject inst.stage2=hd:UUID=53ac1278-3d48-4528-a348-2eb3b7b8dc93:/$isofile
        initrd (loop)/isolinux/initrd.img
    }

    menuentry 'Install Debian-8.3.0-amd64-firmware' {
        set isofile='/boot/iso/firmware-8.3.0-amd64-netinst.iso'
        set initrdfile='/boot/iso/debian-8.3.0-am64-initrd.gz'
        loopback loop $isofile
        linux (loop)/install.amd/vmlinuz vga=791 iso-scan/ask_second_pass=true iso-scan/filename=$isofile
        initrd $initrdfile
    }

Pour trouver l'identifiant UUID de la clef qu'on claque dans la variable
*imgdevpath* en début de config et qu'on passe à *inst.stage2* dans la section
CentOS ou l'identifiant de la partition *fs-uuid* qu'on passe à la commande search,
on utilise la commande **blkid** :

    blkid /dev/sdf1: UUID="53ac1278-3d48-4528-a348-2eb3b7b8dc93" TYPE="ext2" PARTUUID="40c8461c-a5fd-4b3b-9a78-f8e92275ea98"
