#!/usr/bin/env bash
set -e
set -e
. ./.env
. ~/.secret/uk_improv_guide.sh
export IMPROV_GUIDE_VERSIION
echo "Launching ${IMPROV_GUIDE_VERSION}"
echo ${IMPROV_GUIDE_VERSION} > ./src/version.txt

docker-compose -f docker-compose.dev.yaml  down
docker-compose  -f docker-compose.dev.yaml up "$@"