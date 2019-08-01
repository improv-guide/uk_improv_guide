#!/usr/bin/env bash
docker service create \
    --name portainer2 \
    --publish 9001:9000 \
    --constraint 'node.role == manager' \
    --mount type=bind,src=/host/data,dst=/data \
    --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
    portainer/portainer \
    -H unix:///var/run/docker.sock