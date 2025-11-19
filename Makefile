APP_NAME=flask-app
IMAGE=ghcr.io/$(USER)/$(APP_NAME):latest

run:
	python app.py

build:
	docker build -t $(APP_NAME) .

run-docker:
	docker run -p 5000:5000 $(APP_NAME)

push:
	docker push $(IMAGE)

clean:
	docker system prune -f
