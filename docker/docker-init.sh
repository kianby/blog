#!/bin/bash

#export POETRY_HOME=/opt/poetry

# clone and build  blog
cd / 
rm -rf /blog
git clone https://github.com/kianby/blog.git
cd /blog
uv sync
uv run make

# nginx serve
#nginx -g 'daemon off;'
nginx

# exit on change in stacosys or Git repo
uv run python monitor.py