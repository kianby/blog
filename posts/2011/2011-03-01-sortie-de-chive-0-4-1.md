<!-- title: Sortie de Chive 0.4.1 -->
<!-- category: Archlinux -->

Une version mineure de [Chive](http://www.chive-project.com/), l'outil
d'administration mySQL, est sortie la semaine dernière<!-- more --> ; elle corrige un
certains nombre de bugs. Voici le change log officiel.

    Chive 0.4.1 is out, a minor bug-fix release for the 0.4 series.
    Bug-Fixes in this release:
    - FileImport broken
    - Explain not working with groupby
    - no server infos without selecting a schema first
    - class HttpRequest conflict with pecl http module
    - get error after login of version 0.4.0
    - it is better to use class CJSON instead of json_encode/json_decode

J'ai mis à jour le paquet AUR (lien obsolète: http://aur.archlinux.org/packages.php?ID=45734)
correspondant pour Archlinux :-)
