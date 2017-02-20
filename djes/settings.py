# coding: utf-8

"""
Django settings for djes project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y9qw%2b^c7-$*@6rmfy)&fsiep=svk(o@8di!wzf528eno^t+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Core django dependencies
    'django.contrib.staticfiles',

    # External dependencies
    'bootstrap3',
    'simple_elasticsearch',

    # Project dependencies
    'djesapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'djes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'node_modules'),
    os.path.join(BASE_DIR, 'static'),
]


# Django simple elasticsearch settings
ELASTICSEARCH_TYPE_CLASSES = [
    'djes.models.Article',
]

ELASTICSEARCH_DEFAULT_INDEX_SETTINGS = {
    "settings": {
        "analysis": {
            "tokenizer": {
                "whitespace": {"type": "whitespace"}
            },
            "filter": {
                "french_elision": {
                    "type": "elision",
                    "articles": ["l", "m", "t", "qu", "n", "s", "j", "d"]
                },
                "french_stop": {
                    "type": "stop",
                    "stopwords": ["ès", "vers", "a", "à", "afin", "ai", "ainsi", "après", "attendu",
                                  "au", "aujourd", "auquel", "aussi", "autre", "autres", "aux",
                                  "auxquelles", "auxquels", "avait", "avant", "avoir", "c", "ça",
                                  "car", "ce", "ceci", "cela", "celle", "celles", "celui",
                                  "cependant", "certain", "certaine", "certaines", "certains", "ces",
                                  "cet", "cette", "ceux", "chez", "ci", "combien", "comme", "comment",
                                  "concernant", "contre", "d", "dans", "de", "debout", "dedans",
                                  "dehors", "delà", "depuis", "derrière", "des", "dès", "désormais",
                                  "desquelles", "desquels", "dessous", "dessus", "devant", "devers",
                                  "devra", "divers", "diverse", "diverses", "doit", "donc", "dont",
                                  "du", "duquel", "durant", "elle", "elles", "en", "entre", "environ",
                                  "est", "et", "etc", "été", "etre", "être", "eu", "eux", "excepté",
                                  "hélas", "hormis", "hors", "hui", "il", "ils", "j", "je", "jusqu",
                                  "jusque", "l", "la", "là", "laquelle", "le", "lequel", "les",
                                  "lesquelles", "lesquels", "leur", "leurs", "lorsque", "lui", "ma",
                                  "mais", "malgré", "me", "même", "mêmes", "merci", "mes", "mien",
                                  "mienne", "miennes", "miens", "moi", "moins", "mon", "moyennant",
                                  "n", "ne", "néanmoins", "ni", "non", "nos", "notre", "nôtre",
                                  "nôtres", "nous", "ô", "on", "ont", "ou", "où", "outre", "par",
                                  "parmi", "partant", "pas", "passé", "pendant", "plein", "plus",
                                  "plusieurs", "pour", "pourquoi", "près", "proche", "puisque", "qu",
                                  "quand", "que", "quel", "quelle", "quelles", "quels", "qui", "quoi",
                                  "quoique", "revoici", "revoilà", "s", "sa", "sauf", "se", "selon",
                                  "seront", "ses", "si", "sien", "sienne", "siennes", "siens", "sinon",
                                  "soi", "soit", "son", "sont", "sous", "suivant", "sur", "ta", "te",
                                  "tes", "tien", "tienne", "tiennes", "tiens", "toi", "ton", "tous",
                                  "tout", "toute", "toutes", "tu", "un", "une", "va", "voici", "voilà",
                                  "vos", "votre", "vôtre", "vôtres", "vous", "vu", "y"]
                }
            },
            "analyzer": {
                "custom_french_analyzer": {
                    "tokenizer": "letter",
                    "filter": ["asciifolding", "lowercase", "french_stop", "french_stem", "french_elision"]
                },
                "address": {
                    "type": "custom",
                    "tokenizer": "whitespace",
                    "filter": ["trim", "lowercase"]
                }
            }
        }
    }
}
