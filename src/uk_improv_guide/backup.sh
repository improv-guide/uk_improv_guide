#!/usr/bin/env bash
python manage.py dumpdata uk_improv_guide --format=yaml > .${BACKUP_DIR}/uk_improv_guide.yaml
