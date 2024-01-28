install:
	python3 -m pip install -r requirements.txt

run:
	export FLASK_APP=app.py && \
	python3 -m flask run --debug --port=8000 --host=0.0.0.0

docker-build:
	docker build -t simple-graphql:latest -f Dockerfile .

docker-build-prod:
	docker build -t simple-graphql:latest -f Dockerfile.prod .

docker-run:
	docker run --rm -p 8000:8000 -d --name simple-graphql simple-graphql

docker-stop:
	docker stop simple-graphql

docker-exec:
	docker exec -it simple-graphql bash
