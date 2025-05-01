#!/bin/bash

# Aktifkan virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt

# Buat direktori uploads jika belum ada
mkdir -p uploads
chmod 755 uploads

# Set permissions
chmod 755 passenger_wsgi.py
chmod 755 app.py
chmod 644 .htaccess
chmod 600 .env

# Restart Python application
touch passenger_wsgi.py

echo "Deployment completed successfully!" 