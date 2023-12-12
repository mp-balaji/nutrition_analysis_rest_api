#!/bin/bash

if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 is not installed. Please install Python 3.11 and try again."
    exit 1
fi

echo "Creating Python virtual environment using Python 3.11..."
python3.11 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing required packages from requirements.txt..."
pip install -r requirements.txt

echo "Setup completed successfully."
