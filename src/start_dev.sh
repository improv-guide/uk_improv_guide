#!/usr/bin/env bash
set -e
migrate.sh
uk_improv_guide/compile_css.sh
echo "Starting development server..."
manage runserver 0.0.0.0:8000