# HoneyRecruiting Cyber

An experimental lab exploring technical profile assessment through guided conversations, rule-based bots and keyword-based analysis.

<p align="center">
  <img src="https://img.shields.io/badge/HR_TECH-HONEY_RECRUITING_CYBER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="HoneyRecruiting Cyber"/>
  <img src="https://img.shields.io/badge/PYTHON-FLASK-101010?style=for-the-badge&logo=python&logoColor=00FF41" alt="Python and Flask"/>
</p>

<p align="center">
  <a href="https://tzayadet.github.io/HoneyRecruitingCyber/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/HoneyRecruitingCyber"><strong>SOURCE CODE</strong></a>
</p>

[![Static deployment](https://github.com/tzayadet/HoneyRecruitingCyber/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/HoneyRecruitingCyber/actions/workflows/static.yml)

> GitHub Pages publishes a static project overview. The Flask application requires a Python backend and database; it does not run on Pages.

## What it does

- Conversational interface for exploring technical profiles.
- Rule-based bots and heuristic responses.
- Keyword-based classification and indicative scoring.
- Session-linked conversation history.
- Flask-SQLAlchemy persistence.
- Dashboard protected by HTTP Basic authentication.

## Run locally

**Requirements:** Python 3.11 or later.

```bash
python -m venv .venv
```

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
python -m pip install .
python main.py
```

**Linux / macOS**
```bash
source .venv/bin/activate
python -m pip install .
python main.py
```

The development server starts at `http://127.0.0.1:5000`. PostgreSQL is intended for shared deployments; SQLite can be used for development.

## Configuration

Set deployment secrets through environment variables, not source files.

| Variable | Purpose |
|---|---|
| `SESSION_SECRET` | Persistent session-signing secret |
| `DATABASE_URL` | SQLAlchemy database URL |
| `COOKIE_SECURE` | Enables Secure cookies under HTTPS |
| `TRUSTED_PROXY_COUNT` | Number of trusted reverse proxies |
| `DASHBOARD_USERNAME` | Dashboard username |
| `DASHBOARD_PASSWORD` | Dashboard password |

Use Gunicorn behind an HTTPS reverse proxy for shared deployments. Do not use Flask's development server in production.

## Project structure

| Component | Purpose |
|---|---|
| `app.py` | Flask application factory and configuration |
| `main.py` | Development entry point |
| `routes.py` | Routes and API |
| `models.py` | SQLAlchemy models |
| `bots.py` | Heuristic responses |
| `keywords.py` | Keyword analysis and scoring |
| `templates/`, `static/` | Web interface |

## Scope and limitations

This is a research prototype, not a production ATS or validated assessment system. Scoring is based on keyword matches and does not objectively measure competence. The bots use rules and heuristics, not a generative AI model.

Do not use its scores as an automated hiring decision. Do not enter real CVs or candidate personal data into a public demo. A shared deployment requires access controls, retention policies, privacy review and security testing.

## Deployment

The `.github/workflows/static.yml` workflow publishes the static project overview to GitHub Pages. The Flask backend and database require a separate hosting environment.

## License

MIT. See [LICENSE](LICENSE).
