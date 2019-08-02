#!/usr/bin/env bash
set -e
export NEW_RELIC_CONFIG_FILE=/src/uk_improv_guide/newrelic.ini
newrelic-admin run-program gunicorn --bind=0.0.0.0:80 uk_improv_guide.wsgi