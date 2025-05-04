import os
import sys

VENV_PATH = "/home/u5389241/virtualenv/public_html/numpang/3.7/bin/python"
if sys.executable != VENV_PATH:
    os.execl(VENV_PATH, VENV_PATH, *sys.argv)

sys.path.append(os.getcwd())

from app import app as application

# For debugging
import logging
logging.basicConfig(filename='passenger.log', level=logging.DEBUG)
try:
    logging.debug('Starting application...')
    application.debug = False
except Exception as e:
    logging.error(f'Error starting application: {str(e)}') 