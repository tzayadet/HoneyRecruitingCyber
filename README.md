<p align="center">
  <img src="https://img.shields.io/badge/CYBERSECURITY-HONEYRECRUITING-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="HoneyRecruiting Cyber"/>
  <img src="https://img.shields.io/badge/FLASK-PYTHON-101010?style=for-the-badge&logo=flask&logoColor=00FF41" alt="Flask"/>
</p>

# HoneyRecruiting Cyber

Laboratorio experimental que explora la evaluación técnica de perfiles de ciberseguridad mediante conversaciones guiadas, bots heurísticos y análisis orientativo de términos técnicos.

<p align="center">
  <a href="https://tzayadet.github.io/HoneyRecruitingCyber/"><strong>PROJECT SHOWCASE ↗</strong></a> ·
  <a href="https://github.com/tzayadet/HoneyRecruitingCyber"><strong>SOURCE CODE</strong></a>
</p>

[![GitHub Pages](https://github.com/tzayadet/HoneyRecruitingCyber/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/HoneyRecruitingCyber/actions/workflows/static.yml)

> Pages publica una ficha estática del proyecto. La aplicación Flask requiere un backend Python y una base de datos; no se ejecuta en GitHub Pages.

## What it does

- Interfaz conversacional para explorar perfiles técnicos.
- Bots basados en reglas y respuestas heurísticas.
- Clasificación orientativa mediante palabras clave.
- Historial de conversación asociado a sesiones.
- Persistencia con Flask-SQLAlchemy.
- Dashboard analítico con autenticación HTTP Basic.

## Run locally

**Requirements:** Python 3.11+.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install .
python main.py
```

La aplicación de desarrollo se inicia en `http://127.0.0.1:5000`. Para despliegues compartidos se contempla PostgreSQL; SQLite puede utilizarse en desarrollo.

## Configuration

Configura las variables de entorno antes de desplegar:

| Variable | Purpose |
|---|---|
| `SESSION_SECRET` | Secreto persistente para firmar sesiones |
| `DATABASE_URL` | Cadena de conexión SQLAlchemy |
| `COOKIE_SECURE` | Activa cookies Secure bajo HTTPS |
| `TRUSTED_PROXY_COUNT` | Número real de proxies inversos de confianza |
| `DASHBOARD_USERNAME` | Usuario del dashboard |
| `DASHBOARD_PASSWORD` | Contraseña del dashboard |

Utiliza Gunicorn detrás de un proxy HTTPS en despliegues reales. No utilices el servidor de desarrollo de Flask en producción.

## Project layout

| Component | Purpose |
|---|---|
| `app.py` | Creación y configuración de Flask |
| `main.py` | Entrada de desarrollo |
| `routes.py` | Rutas y API |
| `models.py` | Modelos SQLAlchemy |
| `bots.py` | Respuestas heurísticas |
| `keywords.py` | Análisis de términos y puntuación |
| `templates/` · `static/` | Interfaz web |

## Scope & limitations

Es un prototipo de investigación, no un ATS ni una herramienta de selección lista para producción. La puntuación se basa en coincidencias de palabras clave y no mide de forma objetiva la competencia. Los bots no utilizan un modelo de IA.

No debe utilizarse como criterio automático de contratación. No introduzcas CV ni datos personales reales en una demo pública. El dashboard debe mantenerse protegido y los datos locales deben someterse a controles de acceso, retención y privacidad.

## Deployment

El workflow `.github/workflows/static.yml` publica la ficha estática del proyecto en GitHub Pages. El backend Flask y la base de datos necesitan un servicio compatible independiente.

## License

MIT. See [LICENSE](LICENSE).
