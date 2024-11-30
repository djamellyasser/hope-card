"""
WSGI config for hopecarde project.
It exposes the WSGI callable as a module-level variable named ``app``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopecarde.settings')

app = get_wsgi_application()
