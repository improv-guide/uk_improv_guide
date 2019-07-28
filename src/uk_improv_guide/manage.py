#!/usr/local/bin/python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

from django.core.management import execute_from_command_line

log = logging.getLogger(__name__)


def start():
    log.info("Starting application.")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uk_improv_guide.settings")
    execute_from_command_line(sys.argv)


def main():
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    start()

if __name__ == "__main__":
    main()

