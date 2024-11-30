#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static

# Collect static files
python manage.py collectstatic --noinput

# Make the build.sh executable
chmod +x build.sh
