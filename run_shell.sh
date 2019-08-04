#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose -f docker-compose.dev.yaml run --entrypoint=/bin/bash site "$@"