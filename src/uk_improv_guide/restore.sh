#!/usr/bin/env bash
python manage.py loaddata --exclude=auth.Permission --format=yaml ./test_data/test_data.yaml