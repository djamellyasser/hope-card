"""
WSGI config for hopecarde project.
It exposes the WSGI callable as a module-level variable named ``app``.
"""
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopecarde.settings')

try:
    app = get_wsgi_application()
except Exception as e:
    print(f"Error loading WSGI application: {e}")
    raise
