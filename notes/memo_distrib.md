<!-- title: Mémo par distrib -->

# Arch

Supprimer les dépendances des paquets orphelins

    pacman -Rsn $(pacman -Qtdq)

# Fedora 

Historique des transactions **dnf** 

    dnf history list

Liste des paquets installés

    dnf list installed

Liste des dépôts installés 

    dnf repolist

Désactiver un dépôt 

    sudo dnf config-manager --set-disabled zing

Grub EFI 

    grub2-mkconfig -o /boot/grub2/grub.cfg
    dnf reinstall grub2-efi shim

([Source](https://docs.fedoraproject.org/en-US/fedora/latest/system-administrators-guide/kernel-module-driver-configuration/Working_with_the_GRUB_2_Boot_Loader/))

#  Nix 

Recherche des paquets disponibles (ou [sur le site officiel](https://search.nixos.org/packages))

    nix-env -qa --description '.*libtmux.*'

Installer un paquet 

    nix-env -i <nom du paquet>

Désinstaller un paquet

    nix-env --uninstall <nom du paquet>

lister les paquets installés 

    nix-env -qa --installed "*"

lister les canaux 

    nix-channel --list

Mettre à jour tous les canaux

    nix-channel --update 

Mettre à jour tous les paquets 

    nix-env -u    

Gérer les versions 

    nix-env --list-generations    
    nix-env --delete-generations old

Rollbacker

    nix-env --rollback 

# WSL

pas une distribution mais un cheval de Troie ;-)

## Problème de tail entre WSL et NTFS 

    tail -F ---disable-inotify <mon_fichier>

## Transfert entre machines 

Pour transférer une machine WSL sur une autre machine, il faut compresser avec le mode "sensitive case mode" : 

    7z.exe a  debian.7z Debian\* -ssc -r

## Distribution recommandée 

[ArchWSL](https://github.com/yuk7/ArchWSL)

## Ne pas alourdir le PATH WSL 

Ne pas alourdir le PATH WSL avec le PATH de Windows. Editer */etc/wsl.conf* et ajouter : 

    [interop]
    appendWindowsPath = false

Source : https://stackoverflow.com/questions/51336147/how-to-remove-the-win10s-path-from-wsl

## Compacter le disque WSL2 

Lancer l'outil diskpart et exécuter les deux commandes suivantes :

    select vdisk file "C:\Users\yannic.arnoux\Documents\Arch\ext4.vhdx"
    compact vdisk

Source :  https://stephenreescarter.net/how-to-shrink-a-wsl2-virtual-disk/

# Fish Shell 

pas une distribution mais une exoplanète ;-) 

Profiler le temps de démarrage 

    fish --profile-startup /tmp/fish.profile -i -c exit

