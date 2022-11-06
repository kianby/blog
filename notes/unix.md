<!-- title: Des commandes Linux -->

# Shell

Relancer la dernière commande : !!

Relancer la dernière commande en sudo : sudo !!

# Les fichiers

All directories will be 775. All files will be 664 except those that were set as executable to begin with

    chmod -R a+rwX,o-w <directory>

# Compression

Compresser en préservant les permissions

    tar cvpzf put_your_name_here.tar.gz .

Compresser en splittant par fichier de 2 Mo

    tar cvzp source/  | split -b 2MiB - backup_part.tgz_

et décompression

    cat backup_part.tgz_* | tar xz

Compression moins efficace mais plus rapide avec LZOP :

    tar --lzop -cvf archive.tar.lzo dossier/
    tar xvf archive.tar.lzo

# Les processus
  
Lister les ports ouverts et l'application :    

    sudo netstat -pntul


Donner accès aux ports réservés (<1024) à un processus exécuté par un utilisateur standard

    setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/python3.9

# Listage

Lister par date de modif du - récent au + récent

    ls -lrth

Lister récursivement par taille ascendante

    find . -type f -exec ls -lSr {} +
    
Lister les plus gros fichiers ou répertoires 

    du -cks * | sort -rn | head

# Conversion 

du format HEIF (Apple) vers JPEG

    for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done

# Historique

Vider l'historique de Bash (source [StackOverflow](https://askubuntu.com/questions/191999/how-to-clear-bash-history-completely)) 

    cat /dev/null > ~/.bash_history && history -c && exit

