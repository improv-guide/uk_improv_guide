#!/usr/bin/env bash
set -e
. ~/.secret/uk_improv_guide_prod.sh
docker-compose down
docker-compose up "$@"