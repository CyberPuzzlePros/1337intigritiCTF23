#!/bin/bash

docker build -t ctf .
docker run --name=ctfc --rm -p1337:80 -it ctfc -d