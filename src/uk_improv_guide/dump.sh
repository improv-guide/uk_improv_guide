#!/usr/bin/env bash
python manage.py dumpdata --format=yaml --exclude=admin.logentry --exclude=reversion.revision --exclude=reversion.version --exclude=sessions.session --exclude=contenttypes.contenttype > ./test_data/test_data.yaml
