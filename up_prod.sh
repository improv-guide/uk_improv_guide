#!/usr/bin/env bash
. ~/.secret/uk_improv_guide_prod.sh
docker-compose down
docker-compose up "$@"