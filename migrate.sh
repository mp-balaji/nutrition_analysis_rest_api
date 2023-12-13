#!/bin/bash

echo "Activating virtual environment..."
if source venv/bin/activate; then
    echo "Virtual environment activated."
else
    echo "Failed to activate virtual environment. Make sure 'venv' exists."
    exit 1
fi

export FLASK_APP=app.py
echo "FLASK_APP set to $FLASK_APP."

echo "Creating new scripts folder if necessary..."
flask db init

echo "Generating new migration files if necessary..."
flask db migrate

echo "Applying database migrations..."
flask db upgrade

echo "Database migration completed successfully."
