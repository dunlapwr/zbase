"""
Production settings for ZHub project.
Deployed on DigitalOcean App Platform.
"""
import os

import dj_database_url

from .base import *  # noqa: F401, F403

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Database — parsed from DATABASE_URL injected by DigitalOcean
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# Security settings for running behind DO's load balancer
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Trust the DO App Platform domain
CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if host
]
