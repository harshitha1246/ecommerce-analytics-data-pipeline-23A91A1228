#!/bin/bash

# E-Commerce Data Pipeline Setup Script
# This script initializes the project environment and dependencies

set -e  # Exit on error

echo "========================================"
echo "E-Commerce Data Pipeline Setup"
echo "========================================"
echo ""

# Check Python version
echo "[1/7] Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $python_version"
echo ""

# Create virtual environment
echo "[2/7] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "[3/7] Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "[4/7] Upgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✓ pip upgraded"
echo ""

# Install dependencies
echo "[5/7] Installing Python dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create required directories
echo "[6/7] Creating project directories..."
mkdir -p data/raw
mkdir -p data/staging
mkdir -p data/processed
mkdir -p logs
mkdir -p dashboards/screenshots
echo "✓ Directories created"
echo ""

# Setup environment file
echo "[7/7] Setting up environment configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ Created .env file from template"
    echo "  NOTE: Please update .env with your database credentials"
else
    echo "✓ .env file already exists"
fi
echo ""

echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Update .env file with your database configuration"
echo "2. Run: docker-compose up -d"
echo "3. Run: python scripts/pipeline_orchestrator.py"
echo ""
echo "Virtual environment is active. To deactivate, run: deactivate"
echo ""
