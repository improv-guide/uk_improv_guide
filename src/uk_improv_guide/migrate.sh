#!/usr/bin/env bash
echo "Generating migrations..."
python manage.py makemigrations
echo "Running database migrations..."
python manage.py migrate
echo "Creating revisions..."
python manage.py createinitialrevisions
echo "Setting permissions on migrations"
chmod o+rw uk_improv_guide/migrations/*.py