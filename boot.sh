#!/bin/sh
python wsgi.py
# gunicorn -c gunicorn_config.py wsgi:app