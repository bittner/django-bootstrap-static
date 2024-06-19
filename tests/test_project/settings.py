"""Minimal Django settings for test project."""

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "bootstrap",
    "fontawesome",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

STATIC_URL = "static"
