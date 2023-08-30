"""
WSGI config for passcode_revealer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure Ap Service
# If so, then load the settings from production.py
settings_module = 'passcode_revealer.azure_deployment' if 'WEBSITE_HOSTNAME' \
                                in os.environ else 'passcode_revealer.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passcode_revealer.settings')

application = get_wsgi_application()
