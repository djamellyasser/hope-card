import os
import sys
from pathlib import Path

# Add your project directory to the sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopecarde.settings')

# This is to ensure we have access to all Django apps
import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Vercel needs the variable to be named 'app'
app = application
