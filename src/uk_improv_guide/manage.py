#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
from django.core.management import execute_from_command_line

log = logging.getLogger(__name__)

def main():
    log.info("Starting application.")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uk_improv_guide.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    main()
