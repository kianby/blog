#!/bin/bash

# clone and build  blog
cd / 
rm -rf /blog
git clone https://github.com/kianby/blog.git
cd /blog
~/.poetry/bin/poetry install
~/.poetry/bin/poetry run make

# nginx serve
#nginx -g 'daemon off;'
nginx

# exit on change in stacosys or Git repo
~/.poetry/bin/poetry run python3 monitor.py