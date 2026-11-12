# HoneyRecruiting Cyber Assessment Lab

**Repository:** HoneyRecruitingCyber

Prototipo de laboratorio para explorar evaluación técnica de conocimientos de ciberseguridad mediante una interfaz conversacional, bots basados en reglas, detección de términos y puntuación orientativa.

**Página pública del proyecto:** https://tzayadet.github.io/HoneyRecruitingCyber/  
Esta página de GitHub Pages es una ficha de presentación estática. La aplicación Flask requiere ejecución de backend independiente y no funciona dentro de GitHub Pages.

## Qué incluye

- Aplicación web Flask con sesiones anónimas.
- Persistencia mediante Flask-SQLAlchemy.
- Bots con respuestas heurísticas.
- Clasificación orientativa basada en palabras clave.
- Historial de conversación por sesión.
- Dashboard analítico protegido mediante autenticación HTTP Basic.

## Requisitos

- Python 3.11+
- PostgreSQL en despliegue compartido, o SQLite para desarrollo local.

## Instalación local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install .
python main.py
```

La aplicación se inicia en `http://127.0.0.1:5000`.

## Configuración

Define estas variables antes de un despliegue:

- `SESSION_SECRET`: secreto aleatorio persistente para firmar sesiones.
- `DATABASE_URL`: URL de conexión SQLAlchemy.
- `COOKIE_SECURE=true`: activa cookies Secure cuando se sirve mediante HTTPS.
- `TRUSTED_PROXY_COUNT`: número de proxies inversos de confianza, si procede.
- `DASHBOARD_USERNAME` y `DASHBOARD_PASSWORD`: credenciales del dashboard. Sin ambas variables, las rutas de analítica permanecen deshabilitadas.

No uses el servidor de desarrollo en producción. Utiliza Gunicorn detrás de un proxy HTTPS y configura explícitamente los proxies de confianza.

## GitHub Pages y backend

GitHub Pages solo publica la página estática de presentación del proyecto. No ejecuta Flask, Python ni PostgreSQL. Para utilizar el chat necesitas desplegar el backend en un servicio compatible con Python y configurar la base de datos.

En un despliegue HTTPS configura `SESSION_SECRET` con un valor aleatorio persistente y conserva `COOKIE_SECURE=true`. Para desarrollo local por HTTP puedes establecer `COOKIE_SECURE=false`. Si utilizas un proxy inverso, configura `TRUSTED_PROXY_COUNT` únicamente con el número real de proxies de confianza. El servidor de desarrollo `python main.py` no debe utilizarse en producción; el comando de despliegue utiliza Gunicorn.

## Alcance y limitaciones

- La puntuación se basa en coincidencias de palabras clave; no es una evaluación objetiva de competencia ni una decisión automatizada de contratación.
- Las respuestas de los bots son heurísticas y no utilizan un modelo de IA.
- La aplicación crea las tablas al iniciar mediante `create_all`; para un uso prolongado conviene incorporar migraciones versionadas.
- El dashboard contiene información agregada y actividad de usuarios; mantenlo protegido y aplica retención de datos y controles de privacidad adecuados.
- No introduzcas datos personales reales en una demo pública.

## Estructura

- `app.py`: creación y configuración de Flask.
- `main.py`: entrada para desarrollo local.
- `routes.py`: vistas y API.
- `models.py`: modelos SQLAlchemy.
- `bots.py`: bots heurísticos.
- `keywords.py`: análisis de términos y puntuación.
- `templates/` y `static/`: interfaz web.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
