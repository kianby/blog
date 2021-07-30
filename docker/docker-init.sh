#!/bin/bash

# clone and build  blog
cd / 
rm -rf /blog
git clone https://github.com/kianby/blog.git
cd /blog
make

# nginx serve
#nginx -g 'daemon off;'
nginx

# exit on change in stacosys or Git repo
python3 monitor.py