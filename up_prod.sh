#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose -f docker-compose.prod-new.yaml  down
docker-compose  -f docker-compose.prod-new.yaml up "$@"