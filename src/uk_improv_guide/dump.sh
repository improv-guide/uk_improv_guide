#!/usr/bin/env bash
python manage.py dumpdata uk_improv_guide --format=yaml > ./test_data/uk_improv_guide.yaml
