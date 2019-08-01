#!/usr/bin/env bash
set -e
set
gunicorn --bind=0.0.0.0:80 uk_improv_guide.wsgi