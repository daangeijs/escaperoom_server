# Variables
DOCKER_IMAGE_NAME=escaperoom
DJANGO_MANAGE=python escaperoom/manage.py
DOCKER_VOLUME_NAME=escaperoom_data


.PHONY: migrations superuser runserver populate_menus setup_volume

build:
	@echo "Building Docker image..."
	@docker build -t $(DOCKER_IMAGE_NAME) .

migrations:
	docker exec $(DOCKER_IMAGE_NAME) $(DJANGO_MANAGE) migrate

superuser:
	docker exec -it $(DOCKER_IMAGE_NAME) $(DJANGO_MANAGE) createsuperuser

setup_volume:
	@echo "Creating persistent Docker volume..."
	@docker volume create $(DOCKER_VOLUME_NAME)

populate_menus:
	docker exec -it $(DOCKER_IMAGE_NAME) $(DJANGO_MANAGE) autopopulate_main_menus

setup: build setup_volume runserver migrations superuser
	@echo "Setup complete!"
	docker stop $(DOCKER_IMAGE_NAME)

runserver: 
	@echo "Starting server with persistent volume..."
	docker run -p 8000:8000 -d --rm --name $(DOCKER_IMAGE_NAME) -v $(DOCKER_VOLUME_NAME):/app $(DOCKER_IMAGE_NAME)
	@echo "Server running on http://localhost:8000"