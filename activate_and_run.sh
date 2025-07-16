#!/bin/bash
# Activation script for Unix/Linux/macOS
echo "🔧 Activating virtual environment..."

# Check if we're in the correct directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Please run this script from the project root directory."
    exit 1
fi

# Try different virtual environment locations
if [ -d "venv" ] && [ -f "venv/bin/activate" ]; then
    echo "📁 Using venv environment..."
    source venv/bin/activate
elif [ -d ".venv" ] && [ -f ".venv/bin/activate" ]; then
    echo "📁 Using .venv environment..."
    source .venv/bin/activate
else
    echo "❌ Error: No virtual environment found. Please run 'python setup.py' first."
    exit 1
fi

echo "✅ Virtual environment activated"
echo "🚀 Launching bot..."
python main.py
