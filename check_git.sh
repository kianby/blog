#!/bin/bash

git fetch
HEADHASH=$(git rev-parse HEAD)
UPSTREAMHASH=$(git rev-parse master@{upstream})

if [ "$HEADHASH" != "$UPSTREAMHASH" ]
then
  echo "remote has changed"
  exit 0
else
  echo "no change"
  exit 1
fi 