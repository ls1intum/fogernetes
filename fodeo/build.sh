#!/usr/bin/env bash

docker build -f Dockerfile_Central -t fodeo-central:latest .
docker build -f Dockerfile_Fog -t fodeo-fog:latest .
docker build -f Dockerfile_Camera -t fodeo-camera:latest .

docker tag fodeo-central:latest ba-woebker-bruegge.in.tum.de:30500/fodeo-central:latest
docker tag fodeo-fog:latest ba-woebker-bruegge.in.tum.de:30500/fodeo-fog:latest
docker tag fodeo-camera:latest ba-woebker-bruegge.in.tum.de:30500/fodeo-camera:latest

docker push ba-woebker-bruegge.in.tum.de:30500/fodeo-central:latest
docker push ba-woebker-bruegge.in.tum.de:30500/fodeo-fog:latest
docker push ba-woebker-bruegge.in.tum.de:30500/fodeo-camera:latest