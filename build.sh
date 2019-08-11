#!/usr/bin/env bash
set -e
. ./.env
. ~/.secret/uk_improv_guide.sh
export IMPROV_GUIDE_VERSIION
echo "Building ${IMPROV_GUIDE_VERSION}"
echo ${IMPROV_GUIDE_VERSION} > ./src/version.txt
docker-compose -f docker-compose.yaml build --force
