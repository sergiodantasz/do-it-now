#!/bin/bash

npm --version

echo "Creating a virtual environment..."
python3.9 -m venv venv
source venv/bin/activate

echo "Installing the latest version of pip..."
python -m pip install --upgrade pip

echo "Installing the packages..."
python -m pip install -r requirements.txt

echo "Applying migrations..."
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear
