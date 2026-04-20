from .common import *
import os
import dj_database_url


DEBUG = os.environ.get("DEBUG", "True") == "True"

# if DEBUG:
#     MIDDLEWARE += 'silk.middleware.SilkyMiddleware',

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-dev-only-key")

if os.environ.get("RENDER"):
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


