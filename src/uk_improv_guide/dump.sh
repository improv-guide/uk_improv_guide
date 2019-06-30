#!/usr/bin/env bash
python manage.py dumpdata --natural-foreign --natural-primary --format=yaml > ./test_data/test_data.yaml
