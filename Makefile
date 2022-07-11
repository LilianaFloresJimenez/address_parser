build:
	docker-compose build

test:
	docker-compose run --rm python bash -c "pytest ./tests/unit"

enter:
	docker-compose run --rm python /bin/bash