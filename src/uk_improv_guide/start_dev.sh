#!/usr/bin/env bash
set -e
cd ..
echo "This is environment ${ENVIRONMENT_NAME}..."
python setup.py develop
cd uk_improv_guide
./migrate.sh
./compile_css.sh
echo "Collecting static files..."
yes yes | manage collectstatic
echo "Starting development server..."
manage runserver 0.0.0.0:8000