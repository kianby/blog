<!-- title: Performances, Golang à la rescousse -->
<!-- category: Développement Blog -->
<!-- tag: planet -->

Dans l'[article précédent](/2017/performance-python-web) j'ai optimisé le
[système de gestion des commentaires
Stacosys](https://github.com/kianby/stacosys)<!-- more --> en :

- remplaçant le serveur HTTP de [Flask](http://flask.pocoo.org) par [Sanic](http://sanic.readthedocs.io), un serveur HTTP Python tirant parti des capacités asynchrones de Python 3.5 et multi-processus (plusieurs *workers*)
- ajoutant un cache mémoire à la partie de l'API de Stacosys qui récupère le compteur de commentaires d'un article

J'ai terminé sur une performance bien améliorée :

- plus de 11000 requêtes traitées en 1 minute
- un temps de requête moyen de 1,3 seconde
- une répartition du temps de traitement entre 81 ms et 18 secondes (assez élevé)
- 171 des requêtes (soit 1,5 %) avec un temps de traitement supérieur à 10 secondes

L'architecture avec Sanic ressemble à ceci :

![Architecture Stacosys cache](/images/2017/diag-sanic-cache.png)

Pour être complet le serveur HTTPS NginX en frontal de Stacosys est configuré
avec 4 *workers*  et il déverse les requêtes sur Sanic configuré avec 2
*workers*, qui lui seul utilise 30% de la CPU lors du test. L'impact sur la CPU
est important et doit être mis en balance avec le gain en performance car
d'autres services tournent sur le même serveur.

[NginX](https://fr.wikipedia.org/wiki/Nginx) est un serveur Web très complet et
il y a des configurations avancées de mise en cache qui, d'après sa
documentation, pourraient s'appliquer à mon scénario : un serveur HTTP en mode
Proxy qui renvoie au format JSON les résultats d'une API. Si c'est le cas, cela
rendrait caduque la nécessité d'ajouter un cache au niveau du serveur HTTP de
Stacosys. J'ai fait quelques essais et je ne suis pas  arrivé à un résultat
fonctionnel. Si vous avez des retours d'expérience, j'aurais voulu mesurer les
performances de cette solution. Logiquement, elle devrait l'emporter sur les
autres.

Je cherchais depuis un petit moment une ~~occasion~~ excuse pour écrire un peu
de Golang. Un test HTTP (hors contexte) de Golang m'a convaincu que je pourrais
m'en servir. Le langage [Golang](https://golang.org) a la particularité d'être
compilé, typé, multi-plateforme et il fournit  en standard des fonctionalités de
haut niveau comme HTTP (client et serveur), de la crypto et de la compression,
le support du JSON. Le débat reste
ouvert (lien obsolète : http://spf13.com/post/is-go-object-oriented) sur le fait que Golang soit
un langage orienté objet. En tout cas, il propose un paradigme de programmation
simple et une richesse de librairies qui le rendent très intéressant pour du
développement généraliste où la performance compte.

J'ai donc restauré Stacosys en situation initiale (retour au serveur HTTP de Flask)
et j'ai ajouté un serveur HTTP avec cache en Golang qui sert de proxy à NginX pour
récupérer le compteur de commentaires. Les autres appels à l'API de Stacosys sont 
envoyés directement à Stacosys.

L'architecture devient ainsi :

![Architecture Golang HTTP/Cache](/images/2017/diag-go-http.png)

Dans cette configuration, j'ai relancé mon fameux test étalon. On éclate tout
avec + de 14000 requêtes traitées, un taux d'erreur équivalent mais surtout un
temps de réponse moyen divisé par 4 et une charge CPU d'à peine 7%. Le serveur
HTTP est mono-processus mais il utilise à fond les capacitéss des goroutines de
Golang pour gérer la concurrence de traitement.  

    |       Serveur       | Workers |  Temps de réponse  | Requêtes | Erreurs |
    | ------------------- |:-------:|:------------------:| --------:| -------:|
    | Flask HTTPS         |    1    | 104 > 4194 > 32000 |     4043 |     326 |
    | Sanic HTTPS + cache |    4    | 81 > 1152 > 12408  |    13558 |     210 |
    | Sanic HTTPS + cache |    1    | 81 > 1367 > 18869  |    11589 |     171 |
    | Golang HTTPS        |    ?    |  80 > 341 > 6745   |    14663 |     175 |

Pour les fans de code, voici celui du serveur HTTP avec cache :

```go
    package main

    import (
      "encoding/json"
      "flag"
      "fmt"
      "github.com/patrickmn/go-cache"
      "io/ioutil"
      "net/http"
      "os"
      "time"
    )

    // ConfigType represents config info
    type ConfigType struct {
      HostPort   string
      Stacosys   string
      CorsOrigin string
    }

    var config ConfigType
    var countCache = cache.New(5*time.Minute, 10*time.Minute)

    func die(format string, v ...interface{}) {
      fmt.Fprintln(os.Stderr, fmt.Sprintf(format, v...))
      os.Exit(1)
    }

    func commentsCount(w http.ResponseWriter, r *http.Request) {

      // only GET method is supported
      if r.Method != "GET" {
        http.NotFound(w, r)
        return
      }

      // set header
      w.Header().Add("Content-Type", "application/json")
      w.Header().Add("Access-Control-Allow-Origin", config.CorsOrigin)

      // get cached value
      cachedBody, found := countCache.Get(r.URL.String())
      if found {
        //fmt.Printf("return cached value")
        w.Write([]byte(cachedBody.(string)))
        return
      }

      // relay request to stacosys
      response, err := http.Get(config.Stacosys + r.URL.String())
      if err != nil {
        http.NotFound(w, r)
        return
      }
      defer response.Body.Close()
      body, err := ioutil.ReadAll(response.Body)
      if err != nil {
        http.NotFound(w, r)
        return
      }

      // cache body and return response
      countCache.Set(r.URL.String(), string(body), cache.DefaultExpiration)
      w.Write(body)
    }

    func main() {
      pathname := flag.String("config", "", "config pathname")
      flag.Parse()
      if *pathname == "" {
        die("%s --config <pathname>", os.Args[0])
      }
      // read config File
      file, e := ioutil.ReadFile(*pathname)
      if e != nil {
        die("File error: %v", e)
      }
      json.Unmarshal(file, &config)
      fmt.Printf("config: %s\n", string(file))

      http.HandleFunc("/comments/count", commentsCount)
      http.ListenAndServe(config.HostPort, nil)
    }
```

La démonstration ne vise pas à conclure qu'il faut tout réécrire en Golang car
Python est trop lent !

Hier, je lisais un article à propos de [Discord](https://discordapp.com/), une
application concurrente de Teamspeak avec de la VoIP, des gros besoins de
concurrence de traitement (5 millions de messages échangés en permanence), du
Web et de l'application mobile. Leur solution mixe 4 langages différents :
Python, NodeJS, Golang et Elixir (Erlang) ; chacun a son rôle et son champ
d'application dédié. Plus on acquiert une culture large de l'informatique et
plus on sera capable de choisir le bon langage / paradigme de
programmation / framework en fonction de la tâche à accomplir, ce qui rejoint ce
dicton anglo-saxon que j'aime bien même s'il est un peu galvaudé : *if all
you have is a hammer, everything looks like a nail*.
