#!/bin/sh

docker-compose down -v
docker-compose down --remove-orphans
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input --clear
docker-compose exec web python manage.py createsuperuser --noinput