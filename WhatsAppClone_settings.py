# WhatsAppClone/settings.py

import os
from pathlib import Path

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add 'chat' to the list of installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',  # The chat app
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Templates location
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Point to the templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django default context processors
            ],
        },
    },
]
