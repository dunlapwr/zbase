#!/usr/bin/env bash
set -e

echo "Running database migrations..."
python manage.py migrate --noinput
echo "Migrations complete. Starting gunicorn..."
exec gunicorn zhub.wsgi:application --bind "0.0.0.0:${PORT:-8080}" --workers 2 --access-logfile - --error-logfile -
