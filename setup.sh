#!/bin/bash

# Setup script for Expense Tracker

echo "Setting up Expense Tracker..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create data directory
echo "Creating data directory..."
mkdir -p data

echo "Setup complete!"
echo ""
echo "To run the application:"
echo "  source venv/bin/activate"
echo "  python run.py"
echo ""
echo "Then open http://localhost:8999 in your browser"
echo "Default login: user / password123"
