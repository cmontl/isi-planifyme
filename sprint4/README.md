
# 🗓️ PlanifyMe

**PlanifyMe** es una aplicación web construida con **Flask**, que permite a los usuarios organizar tareas y consultar información útil como el clima, películas y eventos. Utiliza arquitectura de microservicios y está dockerizada para facilitar su despliegue.

---

## 🚀 Características principales

- ✅ Registro e inicio de sesión de usuarios
- ✅ Gestión de tareas personales (CRUD)
- ✅ Microservicio de Clima (Weather API)
- ✅ Microservicio de Películas
- ✅ Microservicio de Eventos
- ✅ Base de datos MySQL inicializada automáticamente
- ✅ Docker + Makefile para ejecutar todo fácilmente

---

## 🧱 Estructura de carpetas

```
sprint4/
│
├── app/                    # Aplicación principal Flask (interfaz)
│   ├── templates/
│   ├── static/
│   ├── routes.py
│   ├── run.py
│   ├── config.py
│   └── ...
│
├── movies_service/         # Microservicio películas (Flask)
│   └── app.py
│
├── weather_service/        # Microservicio clima (Flask)
│   └── app.py
│
├── events_service/         # Microservicio eventos (Flask)
│   └── app.py
│
├── docker/                 # Configuración Docker
│   ├── docker-compose.yml
│   └── db/
│       └── init.sql        # Script para crear la base de datos y tablas
│
├── Makefile                # Comandos útiles para desarrollo
└── README.md
```

---

## 🐳 Cómo ejecutar el proyecto

1. 📦 Asegúrate de tener `Docker` y `Docker Compose` instalados.
2. 📁 Entra en la carpeta `sprint4/`.
3. ▶️ Ejecuta:

```bash
make up
```

> Esto construye y lanza la app, base de datos y los microservicios, todo en primer plano.

Opcional:

- `make upd`: Ejecuta en segundo plano.
- `make logs`: Muestra los logs en tiempo real.
- `make down`: Detiene y elimina contenedores.
- `make restart`: Reinicia todo desde cero.
- `make clean`: Borra imágenes y caché de Docker.

---

## 🌐 Acceso a la aplicación

Una vez esté corriendo, accede a:

```
http://localhost:5000
```

---

## 📦 Requisitos

- Python 3.11
- Docker & Docker Compose
- Make

---

## 🛠️ Tecnologías usadas

- Flask
- MySQL
- Docker
- Bootstrap (en frontend)
- Microservicios REST (para clima, eventos, películas)

---

## 📌 Notas

- La base de datos se inicializa automáticamente gracias al script `init.sql`.
- Los microservicios están configurados para comunicarse vía nombre de servicio (`weather`, `movies`, `events`).
- Puedes modificar los microservicios en sus respectivas carpetas.

---

## 👨‍💻 Autor

Carlos Monteagudo · Proyecto académico para la asignatura **Integración de Sistemas de Información (ISI)**.
