#!/usr/bin/env bash
echo "Generating migrations..."
manage makemigrations
echo "Running database migrations..."
manage migrate
echo "Creating revisions..."
manage createinitialrevisions
echo "Setting permissions on migrations"
chmod --recursive o+rw uk_improv_guide/migrations