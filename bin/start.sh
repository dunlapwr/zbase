#!/usr/bin/env bash

echo "Running database migrations..."
if python manage.py migrate --noinput; then
    echo "Migrations complete."
else
    echo "WARNING: Migrations failed (exit code $?). Starting gunicorn anyway..."
fi

echo "Starting gunicorn..."
exec gunicorn zhub.wsgi:application --bind "0.0.0.0:${PORT:-8080}" --workers 2 --access-logfile - --error-logfile -
