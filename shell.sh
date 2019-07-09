#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose run --entrypoint=/bin/bash python "$@"