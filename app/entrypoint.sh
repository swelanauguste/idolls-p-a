#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput
# python manage.py add_banners
# python manage.py add_services ./static/docs/services.csv
# python manage.py add_socials ./static/docs/socials.csv
# python manage.py add_values ./static/docs/values.csv
# python manage.py add_why_us ./static/docs/why_us.csv

exec "$@"