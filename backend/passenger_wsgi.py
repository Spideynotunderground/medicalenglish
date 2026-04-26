"""
WSGI config for Python hosting (PythonAnywhere, etc.)
"""
import os
import sys

# Add your project directory to the sys.path
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Load .env file
from dotenv import load_dotenv
load_dotenv(os.path.join(project_home, '.env'))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
