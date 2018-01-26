#!/usr/bin/env bash

docker stop registry && sudo docker rm -v registry
docker run -d -p 5555:5000 --restart=always --name registry registry:2
