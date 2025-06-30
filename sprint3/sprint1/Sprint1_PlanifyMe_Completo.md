
# 🚀 Sprint 1 - Proyecto ISI: **PlanifyMe**

## 1. Nombre del grupo y roles tecnológicos
- **Nombre del proyecto**: PlanifyMe
- **Equipo**:
  - Backend: Carlos
  - Testing: Carlos
  - Frontend (opcional o con herramientas de test): Carlos

---

## 2. Motivación
Las personas pierden tiempo cada semana decidiendo qué hacer durante el fin de semana. PlanifyMe sugiere planes personalizados (películas, eventos o actividades) según la ubicación y el clima.

---

## 3. Objetivos y Subobjetivos

### Objetivo principal
Sugerir automáticamente actividades de ocio personalizadas.

### Subobjetivos
- Registro y login de usuarios con JWT
- Consultar clima, eventos y películas mediante APIs externas
- Generar sugerencias de planes según contexto
- Guardar planes favoritos del usuario

---

## 4. Casos de uso
1. **Registro/Login del usuario**
2. **Obtener sugerencia de plan personalizado (según APIs externas)**
3. **Guardar planes favoritos**
4. **Consultar historial de sugerencias**

---

## 5. TAM & SAM

- **TAM (Total Available Market)**: Jóvenes de entre 16-35 años con acceso a internet en España (~8 millones)
- **SAM (Serviceable Available Market)**: Estudiantes universitarios que usan apps móviles/web (~2 millones)

---

## 6. Perfil del cliente (Persona)
- **Nombre**: Laura, 22 años
- **Situación**: Estudiante universitaria, vive en ciudad mediana
- **Problemas**: Tiene tiempo libre los fines de semana, pero no quiere perder tiempo planeando
- **Necesidad**: Quiere planes sencillos, rápidos, adaptados al clima y sin tener que buscar en muchas apps
- **Cómo nos conoce**: Recomendación en clase o por redes

---

## 7. Business Model Canvas

| Elemento                  | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **Segmentos de clientes** | Estudiantes universitarios de entre 18-30 años con acceso a smartphone.     |
| **Propuesta de valor**    | Ofrecer sugerencias personalizadas y automáticas de planes de ocio de fin de semana, según su ubicación, clima y gustos, todo desde un único lugar. |
| **Canales**               | Web App, Redes Sociales (Instagram, TikTok), Promociones en universidades. |
| **Relación con clientes** | Autoservicio digital, atención básica por email/redes, mejoras por feedback.|
| **Fuentes de ingresos**   | Inicialmente gratuito; versión premium con filtros personalizados y recordatorios. |
| **Recursos clave**        | Backend Flask, APIs externas, Docker, Kubernetes, GitHub Actions, base de datos SQLite/PostgreSQL. |
| **Actividades clave**     | Integración con APIs, desarrollo de microservicios, gestión de usuarios, despliegue continuo. |
| **Socios clave**          | APIs de terceros: OpenWeatherMap, TMDB, Ticketmaster. Plataformas de despliegue (DockerHub, GitHub). |
| **Estructura de costes**  | Coste de mantenimiento de servidores, dominios, API premium, desarrollo.     |

---

## 8. Customer Journey Map

| Fase           | Acción del usuario                        | Punto de contacto              | Emoción esperada          | Oportunidad de mejora                     |
|----------------|-------------------------------------------|---------------------------------|----------------------------|-------------------------------------------|
| **Descubrimiento** | Laura ve un anuncio de PlanifyMe en Instagram. | Publicidad en RRSS              | Curiosidad                  | Crear una campaña con llamadas a la acción claras. |
| **Consideración**  | Visita la web app y lee la descripción.        | Landing page                    | Interés                    | Mostrar ejemplos visuales atractivos de planes. |
| **Registro**       | Se registra con email y contraseña.           | Formulario de registro          | Expectativa                | Simplificar el registro, permitir login con Google. |
| **Exploración**    | Prueba la funcionalidad “sugerir plan”.       | Botón de sugerencia + interfaz  | Emoción / Sorpresa         | Mejorar recomendaciones con historial previo. |
| **Acción**         | Guarda un plan favorito.                      | Botón “guardar plan”            | Satisfacción               | Permitir compartir el plan por WhatsApp o email. |
| **Fidelización**   | Vuelve el siguiente fin de semana.            | Notificación o recordatorio     | Confianza / hábito         | Implementar recordatorios automáticos.         |

---

## 9. KPIs y OKRs

### KPIs
- Nº de usuarios registrados
- Nº de sugerencias generadas por día
- Tiempo medio por sesión

### OKRs
- Objetivo 1: Tener al menos 10 usuarios activos en la primera semana.
- Objetivo 2: Generar al menos 50 sugerencias durante los primeros 10 días.

---

## 10. Repositorio en GitHub
Repositorio creado: `https://github.com/tuusuario/isi-planifyme`  
Compartido con el profesor: **FelixVillanueva**
