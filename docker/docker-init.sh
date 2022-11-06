#!/bin/bash

export POETRY_HOME=/opt/poetry

# clone and build  blog
cd / 
rm -rf /blog
git clone https://github.com/kianby/blog.git
cd /blog
$POETRY_HOME/bin/poetry install
$POETRY_HOME/bin/poetry run make

# nginx serve
#nginx -g 'daemon off;'
nginx

# exit on change in stacosys or Git repo
$POETRY_HOME/bin/poetry run python3 monitor.py