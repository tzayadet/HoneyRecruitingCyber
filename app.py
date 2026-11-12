"""Flask application configuration and shared SQLAlchemy extension."""
from __future__ import annotations

import logging
import os
import secrets

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

secret = os.environ.get("SESSION_SECRET")
if not secret:
    secret = secrets.token_urlsafe(48)
    logging.warning(
        "SESSION_SECRET is not configured; using an ephemeral key. "
        "Set SESSION_SECRET in production to keep sessions stable across restarts."
    )

database_url = os.environ.get("DATABASE_URL", "sqlite:///honeypot.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config.update(
    SECRET_KEY=secret,
    SQLALCHEMY_DATABASE_URI=database_url,
    SQLALCHEMY_ENGINE_OPTIONS={"pool_recycle": 300, "pool_pre_ping": True},
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    MAX_CONTENT_LENGTH=16 * 1024,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "true").lower()
    in {"1", "true", "yes"},
)

# Trust forwarded client/protocol headers only when the deployment explicitly
# declares the exact number of trusted reverse proxies.
proxy_count = int(os.environ.get("TRUSTED_PROXY_COUNT", "0"))
if proxy_count > 0:
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=proxy_count,
        x_proto=proxy_count,
        x_host=0,
        x_port=0,
        x_prefix=0,
    )

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# routes.py imports app and db from this module, so initialize the shared
# objects first and register models/routes only after they are available.
with app.app_context():
    import models  # noqa: F401

    db.create_all()

import routes  # noqa: F401,E402
