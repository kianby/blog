#!/bin/sh
[ ! -d "ssl" ] && mkdir ssl
cd ssl
wget -N https://traefik.me/cert.pem 
wget -N https://traefik.me/chain.pem 
wget -N https://traefik.me/fullchain.pem 
wget -N https://traefik.me/privkey.pem
cd -

