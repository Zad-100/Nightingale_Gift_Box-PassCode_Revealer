"""
Settings module for Django Web App deployement using Azure App Service. If the
environment variable WEBSITE_HOSTNAME is defined, then we're running on Azure
App Service and should use the production settings. Otherwise, the environment
variable is not defined (we're running locally) and we should use the local
development settings, i.e., settings.py
"""

import os
# ## NO Quality Assurance (noqa) - Disable flake8 (warnings) for this line
from .settings import * # noqa
from .settings import BASE_DIR


### Configure the domain name using the environment variable
### that Azure automatically creates for us.

# Set secret key for the app during deployment
SECRET_KEY = os.getenv('SECRET_KEY')

# Allow Azure's host name to serve the website
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' \
                                                 in os.environ else []

# Make Azure's host as trusted origin for CSRF
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] \
                       if 'WEBSITE_HOSTNAME' in os.environ else []

# Set DEBUG to False for production/deployment
DEBUG = False

# Whitenoise configuration for collecting and serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Configure Postgres database based on connection string of the
# libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1]
                   for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}