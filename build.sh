#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd project

python manage.py collectstatic --no-input

python manage.py migrate

python -m gunicorn project.asgi:application -k uvicorn.workers.UvicornWorker
