web: python manage.py migrate --noinput && gunicorn zhub.wsgi:application --bind 0.0.0.0:$PORT --workers 2
release: python manage.py migrate --noinput
