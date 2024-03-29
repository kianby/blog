<!-- title: Compilation de Tuxboot sur Fedora 17 -->
<!-- category: GNU/Linux -->
<!-- tag: planet -->

Tuxboot est un fork de Unetbootin qui permet de créer une version USB de
**Clonezilla live** et **GParted live**, <!-- more -->ainsi que DRBL live et Tux2live. C'est
l'outil recommandé par Clonezilla pour créer une clef USB Clonezilla Live. Ils
fournissent des paquets pour Debian et les sources. Etant sur Fedora 17, j'ai
opté pour la compilation à partir des sources :

*    Récupérer les sources sur le site de Tuxboot (http://tuxboot.org) :
tuxboot-0.4.src.tar.gz
*    Installer les outils de développement QT nécessaires à la compilation : yum
install qt-devel
*    Installer les paquets 7z recommandés pour l'exécution : yum install p7zip
p7zip-plugins
*    Décompresser l'archive dans un répertoire de travail : tar xvf
tuxboot-0.4.src.tar.gz
*    Suivre la procédure du fichier INSTALL fourni en adaptant les noms des
exécutables pour Fedora

Voici le source du fichier INSTALL

```shell
cp tuxboot.pro tuxboot-pro.bak
sed -i '/^RESOURCES/d' tuxboot.pro
lupdate-qt4 tuxboot.pro
lrelease-qt4 tuxboot.pro
qmake-qt4 "DEFINES += NOSTATIC CLONEZILLA" "RESOURCES -= tuxboot.qrc"
make
mv tuxboot-pro.bak tuxboot.pro
```  

Si la compilation se passe bien, l'exécutable tuxboot est créé.
