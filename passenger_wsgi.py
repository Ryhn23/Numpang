import os
import sys

# Get cPanel user
CPANEL_USER = os.path.basename(os.path.expanduser('~'))

# Detect Python version
PYTHON_VERSION = '.'.join(map(str, sys.version_info[:2]))

# Build interpreter path
INTERP = f"/home/{CPANEL_USER}/virtualenv/numpang/{PYTHON_VERSION}/bin/python"

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add current directory to path
cwd = os.getcwd()
sys.path.append(cwd)

# Set environment variables
os.environ['PYTHONPATH'] = cwd

# Import Flask application
from app import app as application 