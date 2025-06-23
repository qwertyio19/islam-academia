import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

def get_list(env_name):
    val = os.environ.get(env_name, "")
    return [x.strip() for x in val.split(",") if x.strip()]

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key") 

PRODUCTION = os.environ.get("PRODUCTION", "False") == "True"
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = get_list("ALLOWED_HOSTS") or ['*'] 

LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    ('en', _('English')),
    ('tr', _('Turkish')),
    ('ar', _('Arabic')),
]

LANGUAGE_CODE = "ru"
TIME_ZONE = "Asia/Bishkek"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru', 'ky', 'tr', 'ar', 'en')
TRANSLATABLE_MODEL_MODULES = ['app.base.models']

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

THEME_APPS = [
    "jazzmin",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MY_APPS = [
    "app.students",
    "app.AboutAcademy",
    "app.activity",
    "app.mainpage",
    "app.gellary",
    "app.management",
    "app.ology",
    "app.education",
    "app.applicants",
    "app.search",
]

LIBRARY_APPS = [
    'modeltranslation',
    "rest_framework",
    "corsheaders",
    'drf_yasg',
    'ckeditor',
    'django_ckeditor_5',
    'django_filters',
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *MY_APPS,
    *LIBRARY_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

CORS_ALLOWED_ORIGINS = get_list("CORS_ALLOWED_ORIGINS")  #
CORS_ALLOW_ALL_ORIGINS = os.environ.get("CORS_ALLOW_ALL_ORIGINS", "False") == "True"

CSRF_TRUSTED_ORIGINS = get_list("CSRF_TRUSTED_ORIGINS")  


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'Frontend', 'dist')],
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

WSGI_APPLICATION = "core.wsgi.application"

STATIC_URL = '/back_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'back_static')

MEDIA_URL = "back_media/"
MEDIA_ROOT = BASE_DIR / "back_media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from core.settings.jazzmin import JAZZMIN_SETTINGS
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 300,
        'width': 800,
    },
}
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'en',
        },
    },
}

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
