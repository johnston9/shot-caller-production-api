release: python manage.py makemigrations && python manage.py migrate
web: gunicorn shot-caller-production-api.wsgi
