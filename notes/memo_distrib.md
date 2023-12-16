<!-- title: Mémo par distrib -->

# Arch

## Supprimer des paquets

Supprimer un paquet et ses dépendances 

    pacman -Rs package_name

Supprimer les dépendances des paquets orphelins

    pacman -Rsn $(pacman -Qtdq)

## *Downgrader* des paquets

Récupérer la liste des upgraded ([source](https://wiki.archlinux.org/title/Downgrading_packages))

    grep -i upgraded /var/log/pacman.log

Réinstaller un paquet

    pacman -U file:///var/cache/pacman/pkg/package-old_version.pkg.tar.type

Rollbacker plusieurs paquets par date d'installation ([source](https://linuxconfig.org/how-to-rollback-pacman-updates-in-arch-linux))

```shell
# exemple avec les paquets installés le 15/11/2023
grep -a upgraded /var/log/pacman.log| grep 2023-11-15 > /tmp/lastupdates.txt
awk '{print $4}' /tmp/lastupdates.txt > /tmp/lines1;awk '{print $5}' /tmp/lastupdates.txt | sed 's/(/-/g' > /tmp/lines2
paste /tmp/lines1 /tmp/lines2 > /tmp/lines
tr -d "[:blank:]" < /tmp/lines > /tmp/packages
cd /var/cache/pacman/pkg/
for i in $(cat /tmp/packages); do sudo pacman --noconfirm -U "$i"*.zst; done
```

(potentiel problème d'ordre, réarranger le fichier /tmp/packages en fonction des dépendances entre les paquets)

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

    select vdisk file "C:\yax\Arch\ext4.vhdx"
    compact vdisk

Source :  https://stephenreescarter.net/how-to-shrink-a-wsl2-virtual-disk/

# Fish Shell 

pas une distribution mais une exoplanète ;-) 

Profiler le temps de démarrage 

    fish --profile-startup /tmp/fish.profile -i -c exit

Supprimer le 3ème élément du path (index de 1 à n)

    set --erase --universal fish_user_paths[3]

# Gnome

Désactiver les raccourcis CTRL+ALT LEFT ou RIGHT pour changer de workspace car ils ont priorité sur mes raccourcis de Tmux (source : [stackoverflow](https://stackoverflow.com/questions/47808160/intellij-idea-ctrlaltleft-shortcut-doesnt-work-in-ubuntu))

Supprimer les raccourcis :

    gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-left "[]"
    gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-right "[]"

Restaurer les raccourcis :

    gsettings reset org.gnome.desktop.wm.keybindings switch-to-workspace-left
    gsettings reset org.gnome.desktop.wm.keybindings switch-to-workspace-right
