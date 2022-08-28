release: python manage.py makemigrations && python manage.py migrate
web: gunicorn shot_caller_production_api.wsgi
