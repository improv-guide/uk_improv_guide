#!/usr/bin/env bash
set -e
echo "****"
ls -al

./migrate.sh
./compile_css.sh
echo "Starting development server..."
manage runserver 0.0.0.0:8000