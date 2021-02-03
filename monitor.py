#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import requests 
import time
import json

def fread(filename):
    """Read file and close the file."""
    with open(filename, "r") as f:
        return f.read()

def get_nb_of_comments():
    req_url = params["stacosys_url"] + "/comments/count"
    query_params = dict(
        token=params["stacosys_token"]
    )
    resp = requests.get(url=req_url, params=query_params)
    return 0 if not resp.ok else int(resp.json()["count"])

def exit_program():
    sys.exit(0)

# Default parameters.
params = {
    "stacosys_token": "",
    "stacosys_url": "",
    "external_check": "",
}

# If params.json exists, load it.
if os.path.isfile("params.json"):
    params.update(json.loads(fread("params.json")))

external_check_cmd = params["external_check"]
initial_count = get_nb_of_comments()
print(f"Comments = {initial_count}")
while True:
    # check number of comments every 60 seconds
    for _ in range(15):
        time.sleep(60)
        if initial_count != get_nb_of_comments():
            exit_program()
    # check if git repo changed every 15 minutes
    if external_check_cmd and os.system(external_check_cmd):
        exit_program()
