#!/bin/bash

echo "================================================"
echo "Installing Backend Dependencies..."
echo "================================================"

cd "$(dirname "$0")"

# Install required packages
pip3 install Flask flask-cors reportlab

echo ""
echo "================================================"
echo "Starting Enhanced Backend Server..."
echo "================================================"
echo ""

# Start the enhanced backend
python3 app_enhanced.py
