COMPOSE = docker compose

.PHONY: build up start stop down restart logs logs-backend logs-frontend shell-backend shell-frontend clean

## Build all images
build:
	$(COMPOSE) build

## Start all services (detached)
up:
	$(COMPOSE) up -d

## Alias for up
start: up

## Build and start
up-build:
	$(COMPOSE) up -d --build

## Stop running containers without removing them
stop:
	$(COMPOSE) stop

## Stop and remove containers and networks
down:
	$(COMPOSE) down

## Restart all services
restart:
	$(COMPOSE) restart

## Stream logs for all services
logs:
	$(COMPOSE) logs -f

## Stream logs for backend only
logs-backend:
	$(COMPOSE) logs -f backend

## Stream logs for frontend only
logs-frontend:
	$(COMPOSE) logs -f frontend

## Open a shell in the backend container
shell-backend:
	$(COMPOSE) exec backend bash

## Open a shell in the frontend container
shell-frontend:
	$(COMPOSE) exec frontend bash

## Stop and remove containers, networks, volumes
clean:
	$(COMPOSE) down -v --remove-orphans
