
# 📦 PlanifyMe – Sprint 2

Este sprint se centra en la conexión con APIs externas, diseño de base de datos, tests de integración y la definición de mockups visuales alineados con el customer journey.

---

## ✅ Funcionalidades implementadas

- ✔️ Pruebas de conexión y respuesta con 3 APIs externas (clima, eventos, películas).
- ✔️ Creación de base de datos `planifyme` con 3 tablas:
  - `users`: usuarios registrados.
  - `favorites`: eventos/películas/clima guardados por el usuario.
  - `tasks`: tareas personales creadas por el usuario.
- ✔️ Tests CRUD sobre las tablas para asegurar el correcto funcionamiento.
- ✔️ Mockups visuales que reflejan el recorrido del usuario (customer journey).

---

## 🧪 Tests incluidos

- `test_user_crud.py` – Añadir, editar y borrar usuarios.
- `test_favorites.py` – Añadir y eliminar favoritos.
- `test_tasks.py` – Añadir tarea, marcar como hecha y borrar.

---

## 📐 Mockups entregados

Mockups funcionales realizados con HTML/CSS para simular pantallas de la aplicación. Pueden abrirse en cualquier navegador.

### Pantallas incluidas:

1. **Login:** `mockup_login.html`
2. **Registro:** `mockup_register.html`
3. **Panel principal (dashboard):** `mockup_dashboard.html`
4. **Detalle de evento:** `mockup_event_detail.html`
5. **Crear tarea:** `mockup_task_create.html`
6. **Vista de favoritos:** `mockup_favorites_view.html`

---

## 📁 Estructura del sprint

```
sprint2/
├── README.md
├── tests/
│   ├── db_config.py
│   ├── test_user_crud.py
│   ├── test_favorites.py
│   └── test_tasks.py
├── apis/
│   ├── test_api_weather.py
│   ├── test_api_movies.py
│   └── test_api_events.py
├── mockups/
│   ├── mockup_login.html
│   ├── mockup_register.html
│   ├── mockup_dashboard.html
│   ├── mockup_event_detail.html
│   ├── mockup_task_create.html
│   └── mockup_favorites_view.html
└── requirements.txt
```

---

## 🚀 Próximo sprint (Sprint 3)

- Integración real de las APIs en la app Flask.
- Gestión real de usuarios y sesiones.
- Endpoints REST para tareas y favoritos.
