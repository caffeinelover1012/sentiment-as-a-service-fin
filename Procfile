release: python manage.py migrate
web: gunicorn basicauth.wsgi:application --log-file - --log-level debug