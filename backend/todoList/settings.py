"""
Django settings for todoList project.

Configured for deployment with Render backend and Vercel frontend.
"""
import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = BASE_DIR.parent
FRONTEND_DIR = REPO_ROOT / 'frontend'

# --------------------
# Environment Variables
# --------------------
# Use environment variables for sensitive settings in production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    'localhost,127.0.0.1,.vercel.app,.onrender.com'
).split(',')

CSRF_TRUSTED_ORIGINS = ['https://*.vercel.app', 'https://*.onrender.com']

# --------------------
# Application Definition
# --------------------
INSTALLED_APPS = [
    'corsheaders',  # CORS support
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoList.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_DIR / 'templates'],  # Frontend templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoList.wsgi.application'

# --------------------
# Database
# --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For simplicity; change to Postgres in production
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------
# Password Validators
# --------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --------------------
# Internationalization
# --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------
# Static Files
# --------------------
STATIC_URL = '/static/'

# Development static files
STATICFILES_DIRS = [FRONTEND_DIR / 'static']

# Production static files (Render will collect here)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --------------------
# CORS Configuration
# --------------------
# Allow your Vercel frontend to access backend APIs
CORS_ALLOWED_ORIGINS = [
    "https://to-do-list-hqkw.vercel.app",
]

# Optional: temporarily allow all origins for testing
# CORS_ALLOW_ALL_ORIGINS = True

# --------------------
# Default Auto Field
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
