"""
Open the file in your text editor. In a default Django project, each app 
folder has an __init__.py file which helps to mark it as a module. 
The file is empty by default, but you can add code to influence the import behavior.
"""
from .celery import app as celery_app

__all__ = ("celery_app",)