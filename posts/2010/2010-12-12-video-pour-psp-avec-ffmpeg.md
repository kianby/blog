<!-- title: Vidéo pour PSP avec ffmpeg -->
<!-- category: GNU/Linux -->

La Jackson-mania n'est pas prête de s'éteindre ;-) Mon fils m'a demandé
d'installer des clips Youtube de Michael sur sa PSP. <!-- more -->Pour télécharger du
YouTube il n'y a que l'embarras du choix : de l'extension Firefox à l'outil en
ligne de commande. Mon choix s'est porté sur ClipGrab qui permet de choisir la
qualité de vidéo désirée.

![Clip Grab](/images/03x/clipgrab-300x176.png)

Pour convertir au format PSP j'avais utilisé PSPVC disponible sur
[AUR](https://aur.archlinux.org) mais il ne fonctionne plus
depuis le passage d'Arch à Python2. J'ai donc fouillé du côté des forums
pour voir ce qu'on pouvait faire avec les 2 ténors de la conversion vidéo sur
GNU/Linux : mencoder et ffmpeg. La [documentation Ubuntu](http://doc.ubuntu-fr.org/ffmpeg) pour ffmpeg apporte l'essentiel de la solution à part une
coquille sur un paramètre et le nom des librairies h264 qu'il faut adapter. La
commande ultime est donc :

```shell
ffmpeg -i [input_file] -r 29.97 -vcodec libx264 -s 640x480 -aspect 16:9 -flags +loop -cmp
    +chroma -deblockalpha 0 -deblockbeta 0 -b 768k -maxrate 1500k -bufsize 4M -bt 256k
    -refs 1 -bf 3 -coder 1 -me_method umh -me_range 16 -subq 7
    -partitions parti4x4+parti8x8+partp8x8+partb8x8 -g 250 -keyint_min 25 -level 30
    -qmin 10 -qmax 51 -qcomp 0.6 -trellis 2 -sc_threshold 40 -i_qfactor 0.71 -acodec aac
    -ab 112k -ar 48000 -ac 2 -s 480x272 -aspect 4:3 -strict experimental [output_file.MP4]
```