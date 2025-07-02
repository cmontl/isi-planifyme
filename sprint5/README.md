# PlanifyMe – Documentación Técnica Sprint 5

## 1. Introducción

PlanifyMe es una aplicación web desarrollada como parte del proyecto de la asignatura “Integración de Sistemas de Información”. Su propósito es permitir a los usuarios organizar sus tareas diarias en función de información contextual en tiempo real como el clima, eventos locales y películas en cartelera. Esta funcionalidad busca enriquecer la planificación personal con datos relevantes que faciliten la toma de decisiones.

Este documento constituye la memoria explicativa del Sprint 5, donde se presenta el sistema completo y se incluye una demo funcional del MVP (Producto Mínimo Viable).

---

## 2. Objetivo de la Aplicación

El objetivo principal de PlanifyMe es mejorar la gestión del tiempo del usuario mediante:

- ✅ Consulta del clima actual de la ciudad del usuario.
- ✅ Visualización de eventos próximos.
- ✅ Visualización de películas actuales.
- ✅ Gestión personalizada de tareas basadas en esa información.

Por ejemplo, si se espera lluvia y hay una película interesante, el sistema sugerirá actividades bajo techo.

---

## 3. Arquitectura del Sistema

La solución ha sido implementada como un sistema basado en microservicios utilizando Docker y Flask, con una base de datos MySQL. El sistema se compone de los siguientes servicios:

- **Main App** (`main_app`): Aplicación principal en Flask.
- **Weather Service** (`weather_service`): Microservicio que consume una API externa para consultar el clima.
- **Events Service** (`events_service`): Microservicio que consulta eventos.
- **Movies Service** (`movies_service`): Microservicio para consultar películas actuales.
- **Base de datos** (`mysql_db`): Contenedor con MySQL donde se almacenan usuarios y tareas.

La comunicación entre servicios se realiza mediante peticiones HTTP REST.

---

## 4. Funcionalidades

### 4.1 Registro e Inicio de Sesión

Los usuarios pueden registrarse y autenticarse. Los datos se almacenan en la base de datos y las credenciales son validadas antes de permitir el acceso a funcionalidades privadas.

### 4.2 Gestión de Tareas

Una vez autenticado, el usuario puede:

- Añadir nuevas tareas (planes).
- Ver todas sus tareas.
- Eliminar tareas.

### 4.3 Integración con APIs Externas

Los microservicios consumen las siguientes fuentes externas:

- **Clima**: Se consulta el clima en tiempo real para una ciudad especificada.
- **Películas**: Se obtiene una lista de películas en cartelera.
- **Eventos**: Se listan eventos que ocurren próximamente.

Estos datos son consumidos desde la interfaz y se utilizan para enriquecer la experiencia del usuario.

---

## 5. Tecnologías Utilizadas

- **Lenguaje**: Python 3.11
- **Framework Web**: Flask
- **Motor de Base de Datos**: MySQL 8.0
- **Contenedores**: Docker & Docker Compose
- **Sistema Operativo de desarrollo**: Ubuntu Linux

---

## 6. Estructura de Carpetas

```
sprint4/
├── app/                # Aplicación principal Flask
├── events_service/     # Servicio de eventos
├── movies_service/     # Servicio de películas
├── weather_service/    # Servicio del clima
├── docker/             # Archivos docker-compose y base de datos
├── Makefile            # Automatización de despliegue
└── README.md           # Documentación
```

---

## 7. Despliegue y Ejecución

Para ejecutar el sistema completo:

```bash
make up
```

Esto:
- Construye los contenedores.
- Inicia todos los servicios en background.
- Permite acceder a la aplicación principal en `http://localhost:5000`.

Para detener los servicios:

```bash
make down
```

---

## 8. Demo del MVP

La demo incluye:

- Registro/Login de usuario.
- Creación y visualización de tareas.
- Visualización del clima, eventos y películas.
- Flujo completo de interacción entre frontend y microservicios.

---

## 9. Conclusiones

PlanifyMe demuestra cómo un sistema de microservicios puede integrarse eficazmente para proporcionar al usuario información personalizada y útil. Este trabajo refleja el aprendizaje aplicado en áreas como despliegue en contenedores, consumo de APIs, y gestión de la información del usuario.

---

## 10. Autores

Carlos Montiel y equipo. Grado en Ingeniería Informática.
Universidad de Castilla-La Mancha.