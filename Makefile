runserver:
	docker-compose up

bash:
	docker-compose run --rm backend bash

build:
	docker-compose build --no-cache