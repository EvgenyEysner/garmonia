import os

# https://django-environ.readthedocs.io/en/latest/getting-started.html#installation
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
environ.Env.read_env()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["schoenheitsecke-oldenburg.de", "localhost", "0.0.0.0", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_db_logger",
    "account",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
AUTH_USER_MODEL = "account.user"

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env.bool("DJANGO_SECURE_HSTS_SECONDS")
if SECURE_HSTS_SECONDS > 0:
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Security middleware settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = SESSION_COOKIE_SECURE
# Use X-Forwarded-Proto Header to determine SSL status (useful for API docs)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Csrf middleware settings
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE

# Referrer-Policy middleware
REFERRER_POLICY = "same-origin"
URL_PROTOCOL = "https://" if SESSION_COOKIE_SECURE else "http://"

# Cross-site request forgery
CSRF_USE_SESSIONS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "de-DE"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email server configuration
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = True

RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # Указываем, куда будем сохранять
        # кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

# Logging
DB_LOGGER_ENTRY_LIFETIME = 30
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "db_handler": {
            "level": "DEBUG",
            "class": "django_db_logger.db_log_handler.DatabaseLogHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "system": {
            "level": "INFO",
            "handlers": ["console", "db_handler"],
            "propagate": True,
        },
        "async": {
            "level": "INFO",
            "handlers": ["console", "db_handler"],
            "propagate": True,
        },
        "django_scrubber": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True,
        },
    },
}

QUERYCOUNT = {
    "IGNORE_REQUEST_PATTERNS": [r".*jsi18n.*"],
    "IGNORE_SQL_PATTERNS": [],
    "THRESHOLDS": {
        "MEDIUM": 50,
        "HIGH": 200,
        "MIN_TIME_TO_LOG": 0,
        "MIN_QUERY_COUNT_TO_LOG": 0,
    },
    "DISPLAY_DUPLICATES": None,
    "RESPONSE_HEADER": "X-DjangoQueryCount-Count",
}
