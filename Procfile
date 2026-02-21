release: python manage.py migrate --noinput
web: gunicorn zhub.wsgi:application --bind "0.0.0.0:$PORT" --workers 2 --access-logfile - --error-logfile -
