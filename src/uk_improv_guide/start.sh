#!/usr/bin/env bash
set -e

echo "Generating migrations..."
python manage.py makemigrations
echo "Running database migrations..."
python manage.py migrate
echo "Creating revisions..."
python manage.py createinitialrevisions
echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000