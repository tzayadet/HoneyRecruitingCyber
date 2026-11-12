"""Flask application factory and configuration for HoneyRecruitingCyber."""
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


db = SQLAlchemy(model_class=Base)


def create_app() -> Flask:
    app = Flask(__name__)

    secret = os.environ.get("SESSION_SECRET")
    if not secret:
        secret = secrets.token_urlsafe(48)
        logging.warning(
            "SESSION_SECRET is not configured; using an ephemeral key. "
            "Sessions will be invalidated when the process restarts."
        )

    app.config.update(
        SECRET_KEY=secret,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            "DATABASE_URL", "sqlite:///honeypot.db"
        ),
        SQLALCHEMY_ENGINE_OPTIONS={"pool_recycle": 300, "pool_pre_ping": True},
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAX_CONTENT_LENGTH=16 * 1024,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "false").lower()
        in {"1", "true", "yes"},
    )

    # Trust forwarded headers only when the deployment explicitly declares
    # the number of trusted reverse proxies. Never trust X-Host from clients.
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

    db.init_app(app)

    with app.app_context():
        import models  # noqa: F401
        db.create_all()

    import routes  # noqa: F401

    return app


app = create_app()
