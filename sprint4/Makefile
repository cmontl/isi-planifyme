# Makefile para PlanifyMe

DOCKER_COMPOSE=docker-compose -f docker/docker-compose.yml

up:
	$(DOCKER_COMPOSE) up --build

upd:
	$(DOCKER_COMPOSE) up --build -d

down:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

logs:
	$(DOCKER_COMPOSE) logs -f

restart:
	$(MAKE) down
	$(MAKE) up

build:
	$(DOCKER_COMPOSE) build --no-cache

ps:
	$(DOCKER_COMPOSE) ps

clean:
	docker system prune -a -f
