import os
import django
from django.conf import settings

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monty_hall.settings')

def pytest_configure():
    if not settings.configured:
        django.setup()