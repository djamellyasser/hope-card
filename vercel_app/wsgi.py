import os
import sys
from pathlib import Path

# Add your project directory to the sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopecarde.settings')

    from django.core.wsgi import get_wsgi_application
    
    # This is to ensure we have access to all Django apps
    import django
    django.setup()
    
    application = get_wsgi_application()
    
    # Vercel needs the variable to be named 'app'
    app = application

except Exception as e:
    print(f"Error in wsgi.py: {str(e)}")
    raise
