#!/usr/bin/env bash
python manage.py dumpdata --format=yaml > ./test_data/test_data.yaml
