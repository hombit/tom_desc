"""
Django settings for your TOM project.

Originally generated by 'django-admin startproject' using Django 2.1.1.
Generated by ./manage.py tom_setup on Aug. 9, 2021, 11:06 p.m.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import logging.config
import os
import tempfile


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&amp;)$)o2h&amp;d%7x=817w&amp;#9yr@c33v4t*1u@ihcn=u$=c1zvz5%cf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'django_extensions',
    'guardian',
    'tom_common',
    'django_comments',
    'bootstrap4',
    'crispy_forms',
    'rest_framework',
    'django_filters',
    'django_gravatar',
    'tom_targets',
    'tom_alerts',
    'tom_catalogs',
    'tom_observations',
    'tom_dataproducts',
    'stream.apps.StreamConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tom_common.middleware.Raise403Middleware',
    'tom_common.middleware.ExternalServiceMiddleware',
    'tom_common.middleware.AuthStrategyMiddleware',
]

ROOT_URLCONF = 'tom_desc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'tom_desc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': os.getenv('DB_ENGINE', 'django.contrib.gis.db.backends.postgis'),
        # 'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'tom_desc'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASS', ''),
        'HOST': os.getenv('DB_HOST', 'tom-desc-postgres'),
        # 'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d H:m:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'data')
MEDIA_URL = '/data/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}

# Hopskotch Consumer Configuration

HOPSKOTCH_SERVER = os.getenv('HOPSKOTCH_SERVER', 'dev.hop.scimma.org')
HOPSKOTCH_PORT = os.getenv('HOPSKOTCH_PORT', '9092')
HOPSKOTCH_CONSUMER_POLLING_TIMEOUT = 10

HOPSKOTCH_CONSUMER_CONFIGURATION = {
    'bootstrap.servers': f'{HOPSKOTCH_SERVER}:{HOPSKOTCH_PORT}',
    'group.id': os.getenv('HOPSKOTCH_GROUP', 'skip-test'),
    'auto.offset.reset': 'latest',
    'security.protocol': 'sasl_ssl',
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': os.getenv('HOPSKOTCH_USER',''),
    'sasl.password': os.getenv('HOPSKOTCH_PASSWORD', ''),

    # system dependency: ssl.ca.location may need to be set
    # this does not seem to be necessary on Ubuntu. However,
    # for example on centos7: 'ssl.ca.location': '/etc/ssl/certs/ca-bundle.crt',
}

HOPSKOTCH_TOPICS = [
    'gcn',
    'gcn-circular',
    'sys-heartbeat',
#    'lvc.gcn-test',
#    'lvc.gcn-circular-test',
#    'lvc.lvc-counterpart',
#    'TOMToolkit.test'
]

HOPSKOTCH_PARSERS = {
    'gcn': ['tom_desc.parsers.gcn_lvc_notice_plaintext_parser.GCNLVCNoticeParser'],
    'gcn-circular': ['tom_desc.parsers.gcn_circular_parser.GCNCircularParser'],
#    'lvc.gcn-test': ['tom_desc.parsers.gcn_lvc_notice_plaintext_parser.GCNLVCNoticeParser'],
#    'lvc.gcn-circular-test': ['tom_desc.parsers.gcn_circular_parser.GCNCircularParser'],
#    'lvc.lvc-counterpart': ['tom_desc.parsers.gcn_lvc_counterpart_notice_parser.GCNLVCCounterpartNoticeParser'],
    # 'tomtoolkit-test': ['tom_desc.parsers.tomtoolkit_parser.TOMToolkitParser'],
    'default': ['tom_desc.parsers.base_parser.DefaultParser']
}


# Caching
# https://docs.djangoproject.com/en/dev/topics/cache/#filesystem-caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': tempfile.gettempdir()
    }
}

# TOM Specific configuration
TARGET_TYPE = 'SIDEREAL'

FACILITIES = {
    'LCO': {
        'portal_url': 'https://observe.lco.global',
        'api_key': '',
    },
    'GEM': {
        'portal_url': {
            'GS': 'https://139.229.34.15:8443',
            'GN': 'https://128.171.88.221:8443',
        },
        'api_key': {
            'GS': '',
            'GN': '',
        },
        'user_email': '',
        'programs': {
            'GS-YYYYS-T-NNN': {
                'MM': 'Std: Some descriptive text',
                'NN': 'Rap: Some descriptive text'
            },
            'GN-YYYYS-T-NNN': {
                'QQ': 'Std: Some descriptive text',
                'PP': 'Rap: Some descriptive text',
            },
        },
    },
}

# Define the valid data product types for your TOM. Be careful when removing items, as previously valid types will no
# longer be valid, and may cause issues unless the offending records are modified.
DATA_PRODUCT_TYPES = {
    'photometry': ('photometry', 'Photometry'),
    'fits_file': ('fits_file', 'FITS File'),
    'spectroscopy': ('spectroscopy', 'Spectroscopy'),
    'image_file': ('image_file', 'Image File')
}

DATA_PROCESSORS = {
    'photometry': 'tom_dataproducts.processors.photometry_processor.PhotometryProcessor',
    'spectroscopy': 'tom_dataproducts.processors.spectroscopy_processor.SpectroscopyProcessor',
}

TOM_FACILITY_CLASSES = [
    'tom_observations.facilities.lco.LCOFacility',
    'tom_observations.facilities.gemini.GEMFacility',
    'tom_observations.facilities.soar.SOARFacility',
    'tom_observations.facilities.lt.LTFacility'
]

TOM_ALERT_CLASSES = [
    'tom_alerts.brokers.alerce.ALeRCEBroker',
    'tom_antares.antares.ANTARESBroker',
    'tom_alerts.brokers.gaia.GaiaBroker',
    'tom_alerts.brokers.lasair.LasairBroker',
    'tom_alerts.brokers.mars.MARSBroker',
    'tom_alerts.brokers.scimma.SCIMMABroker',
    'tom_alerts.brokers.scout.ScoutBroker',
    'tom_alerts.brokers.tns.TNSBroker',
    'tom_fink.fink.FinkBroker',
]

BROKERS = {
    'TNS': {
        'api_key': ''
    }
}

TOM_HARVESTER_CLASSES = [
    'tom_catalogs.harvesters.simbad.SimbadHarvester',
    'tom_catalogs.harvesters.ned.NEDHarvester',
    'tom_catalogs.harvesters.jplhorizons.JPLHorizonsHarvester',
    'tom_catalogs.harvesters.tns.TNSHarvester',
]

HARVESTERS = {
    'TNS': {
        'api_key': ''
    }
}

# Define extra target fields here. Types can be any of "number", "string", "boolean" or "datetime"
# See https://tomtoolkit.github.io/docs/target_fields for documentation on this feature
# For example:
# EXTRA_FIELDS = [
#     {'name': 'redshift', 'type': 'number'},
#     {'name': 'discoverer', 'type': 'string'}
#     {'name': 'eligible', 'type': 'boolean'},
#     {'name': 'dicovery_date', 'type': 'datetime'}
# ]
EXTRA_FIELDS = []

# Authentication strategy can either be LOCKED (required login for all views)
# or READ_ONLY (read only access to views)
AUTH_STRATEGY = 'READ_ONLY'

# Row-level data permissions restrict users from viewing certain objects unless they are a member of the group to which
# the object belongs. Setting this value to True will allow all `ObservationRecord`, `DataProduct`, and `ReducedDatum`
# objects to be seen by everyone. Setting it to False will allow users to specify which groups can access
# `ObservationRecord`, `DataProduct`, and `ReducedDatum` objects.
TARGET_PERMISSIONS_ONLY = True

# URLs that should be allowed access even with AUTH_STRATEGY = LOCKED
# for example: OPEN_URLS = ['/', '/about']
OPEN_URLS = []

HOOKS = {
    'target_post_save': 'tom_common.hooks.target_post_save',
    'observation_change_state': 'tom_common.hooks.observation_change_state',
    'data_product_post_upload': 'tom_dataproducts.hooks.data_product_post_upload',
    'data_product_post_save': 'tom_dataproducts.hooks.data_product_post_save',
    'multiple_data_products_post_save': 'tom_dataproducts.hooks.multiple_data_products_post_save',
}

AUTO_THUMBNAILS = False

THUMBNAIL_MAX_SIZE = (0, 0)

THUMBNAIL_DEFAULT_SIZE = (200, 200)

HINTS_ENABLED = True
HINT_LEVEL = 20

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

try:
    from local_settings import * # noqa
except ImportError:
    pass
