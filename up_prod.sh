#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml down
docker-compose  -f docker-compose.yaml -f docker-compose.prod.yaml up "$@"