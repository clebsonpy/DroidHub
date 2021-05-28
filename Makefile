runserver:
	docker-compose up

bash:
	docker-compose run --rm backend bash

build:
	docker-compose build --no-cache

migrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate

createsuperuser:
	docker-compose run --rm backend python manage.py createsuperuser

build-prod:
	docker-compose -f docker-compose.prod.yml build --no-cache

runserver-prod:
	docker-compose -f docker-compose.prod.yml up

migrate-prod:
	docker-compose -f docker-compose.prod.yml run --rm backend python manage.py migrate