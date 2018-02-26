
web:python manage.py runserver
web: gunicorn --pythonpath gamestore gamestore.wsgi --log-file -
heroku ps:scale web=1
