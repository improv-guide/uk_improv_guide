#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose exec dev /bin/bash "$@"