'''
Also, we will need a separate module to run Flask application with Gunicorn.

'''

from app import create_app
app = create_app()