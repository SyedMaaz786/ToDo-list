import os
import sys

from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Ensure backend directory is on path
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / 'backend'
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoList.settings')

application = get_wsgi_application()


