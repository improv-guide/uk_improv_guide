#!/usr/bin/env bash
python manage.py dumpdata uk_improv_guide --format=yaml > /backup/uk_improv_guide.yaml
