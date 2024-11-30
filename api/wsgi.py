"""
WSGI config for Vercel deployment
"""
import os
import sys
from pathlib import Path

# Add your project directory to the sys.path
path = str(Path(__file__).parent.parent)
if path not in sys.path:
    sys.path.append(path)

# Point to the project settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'hopecarde.settings'

# Get the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Vercel expects a variable named 'app'
app = application
