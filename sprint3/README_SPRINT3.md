
# 📄 Hoja Inicial del Proyecto

**Nombre del Proyecto:** PlanifyMe  
**Curso:** Integración de Sistemas de Información  
**Sprint:** 3  
**Autor:** Carlos Monteagudo  
**Tecnologías:** Flask, Python, Docker, API REST, Microservicios, Makefile  
**Fecha de entrega:** 30 de junio de 2025  
**Descripción breve:**  
PlanifyMe es una aplicación web de planificación personal donde el usuario puede gestionar sus tareas y visualizar información personalizada como el clima, películas recomendadas y eventos próximos, consumidos mediante microservicios desarrollados de forma independiente.

---

# ⚙️ Manual de Ejecución

## 1. Requisitos previos
Asegúrate de tener instalado:
- Python 3.10 o superior
- `pip` y `venv`
- Docker
- Make

---

## 2. Clonar el repositorio
```bash
git clone https://github.com/cmontl/isi-planifyme.git
cd isi-planifyme
```

---

## 3. Estructura del proyecto
```
isi-planifyme/
├── sprint1/                  # Documentación y primeros elementos del proyecto
├── sprint2/                  # Inicio del desarrollo de funcionalidades
├── sprint3/                  # Microservicios, APIs externas, integración
│   ├── app/                  # Aplicación principal Flask
│   ├── weather_service/      # Microservicio del clima
│   ├── movies_service/       # Microservicio de películas
│   ├── events_service/       # Microservicio de eventos
│   ├── tests/                # Pruebas de los servicios
│   ├── Makefile              # Script para automatizar arranque y test
│   ├── requirements.txt      # Dependencias del proyecto
│   ├── run.py                # Arranque principal
│   └── api_routes.py         # Rutas de integración de APIs externas
```

---

## 4. Configuración del entorno virtual
```bash
cd sprint3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 5. Ejecución de los microservicios
Cada microservicio puede ejecutarse manualmente así:

### Clima
```bash
python3 weather_service/app.py
```

### Películas
```bash
python3 movies_service/app.py
```

### Eventos
```bash
python3 events_service/app.py
```

---

## 6. Ejecución de la aplicación principal
Una vez estén los microservicios activos, en otro terminal:
```bash
python3 run.py
```

Accede desde tu navegador a:  
📍 `http://localhost:5000`

---

## 7. Uso del Makefile (opcional)
Para levantar todos los servicios juntos y ejecutar tests:
```bash
make run
make test
```

---

## 8. Pruebas
Puedes lanzar los tests automáticos con:
```bash
make test
# o manualmente
pytest tests/
```

---

## 9. Parar los servicios
Presiona `Ctrl + C` en cada terminal donde estén ejecutándose los servicios, o:
```bash
make stop
```
