#!/usr/bin/env bash
set -e
./migrate.sh
./compile_css.sh
echo "Collecting static files..."
yes yes | manage collectstatic
echo "Starting development server..."
manage runserver 0.0.0.0:8000