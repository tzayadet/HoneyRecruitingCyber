# Honey Recruiting Cyber

Prototipo de evaluación técnica de conocimientos de ciberseguridad mediante una interfaz de chat, bots basados en reglas, detección de términos y puntuación orientativa.

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

## GitHub Pages

GitHub Pages solo publica la página estática de presentación del proyecto. No ejecuta Flask, Python ni PostgreSQL. Para utilizar el chat necesitas desplegar el backend en un servicio compatible con Python y configurar la base de datos.

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
