#!/usr/bin/env bash
. ~/.secret/uk_improv_guide.sh
docker-compose run --entrypoint=/usr/local/bin/python python ./manage.py shell "$@"