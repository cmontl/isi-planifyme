# Makefile para Sprint 3 - PlanifyMe

.PHONY: all run services tests stop

PYTHON=python3

all: run

run: services
	@echo "▶️ Ejecutando servidor principal (frontend)..."
	$(PYTHON) run.py

services:
	@echo "🔄 Lanzando microservicios en segundo plano..."
	$(PYTHON) weather_service/app.py & echo $$! > weather.pid
	$(PYTHON) movies_service/app.py & echo $$! > movies.pid
	$(PYTHON) events_service/app.py & echo $$! > events.pid
	sleep 2
	@echo "✅ Microservicios activos."

tests:
	@echo "🧪 Ejecutando tests..."
	$(PYTHON) -m unittest discover -s tests -p "*.py"

stop:
	@echo "🛑 Deteniendo microservicios..."
	-@kill `cat weather.pid` 2>/dev/null || true
	-@kill `cat movies.pid` 2>/dev/null || true
	-@kill `cat events.pid` 2>/dev/null || true
	@rm -f weather.pid movies.pid events.pid
	@echo "✅ Microservicios detenidos."
