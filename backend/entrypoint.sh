#!/bin/sh
set -e

echo "Initializing database..."
python -m app.init_db

echo "Starting Flask app..."
python run.py