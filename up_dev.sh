#!/usr/bin/env bash
set -e
. ~/.secret/uk_improv_guide.sh
docker-compose -f docker-compose.dev.yaml  down
docker-compose  -f docker-compose.dev.yaml up "$@"