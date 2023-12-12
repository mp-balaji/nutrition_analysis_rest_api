#!/bin/bash

echo "Activating Virtual Environment..."
source venv/bin/activate

echo "Starting Application..."
flask run --host=0.0.0.0
