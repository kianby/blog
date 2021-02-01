#!/bin/bash

if git diff-index --quiet HEAD --; then
    # no change
    exit 0
else
    # change
    exit 1
fi