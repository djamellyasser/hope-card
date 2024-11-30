from django.core.wsgi import get_wsgi_application
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopecarde.settings')

app = get_wsgi_application()
