
web:python gamestore/manage.py collectstatic --noinput; gunicorn --pythonpath gamestore gamestore.wsgi --log-file -
heroku ps:scale web=1
