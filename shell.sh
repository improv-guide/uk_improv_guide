#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose -f docker-compose.dev.yaml exec site /bin/bash "$@"