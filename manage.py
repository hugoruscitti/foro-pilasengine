#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../src'))
sys.path.insert(0, os.path.join(HERE, '../requirements'))
sys.path.insert(0, os.path.join(HERE, '../../LBForum'))
sys.path.insert(0, os.path.join(HERE, '../../django-onlineuser'))
sys.path.insert(0, os.path.join(HERE, '../../django-simple-avatar'))
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
    settings_file = getattr(settings, 'SETTINGS', '')
    if settings_file:
        exec("import %s as settings" % settings_file)
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
