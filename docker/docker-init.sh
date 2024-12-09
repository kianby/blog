#!/bin/bash

python -V

# clone and build  blog
cd / 
rm -rf /blog
git clone https://github.com/kianby/blog.git
cd /blog
uv python pin 3.12.8
uv sync
uv run make

# nginx serve
#nginx -g 'daemon off;'
nginx

# exit on change in stacosys or Git repo
uv run python monitor.py