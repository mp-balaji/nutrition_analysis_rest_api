#!/bin/bash

echo "Activating Virtual Environment..."
source venv/bin/activate

# Sleep to ensure the cloud proxy is running before running migration script
sleep 5

./migrate.sh

echo "Starting Application..."
flask run --host=0.0.0.0
