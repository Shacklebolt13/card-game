LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "debug_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "error": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "logs/django.log",
            "formatter": "verbose",
        },
        "debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "logs/django.log",
            "formatter": "verbose",
        },
        "db": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "logs/db.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console","error"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["db"],
            "level": "DEBUG",
            "propagate": False,
        },
        "src": {
            "handlers": ["debug_console","error", "debug"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}