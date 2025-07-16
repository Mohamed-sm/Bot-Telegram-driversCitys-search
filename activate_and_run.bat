@echo off
REM Activation script for Windows
echo 🔧 Activating virtual environment...

REM Check if we're in the correct directory
if not exist "main.py" (
    echo ❌ Error: main.py not found. Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Try different virtual environment locations
if exist "venv\Scripts\activate.bat" (
    echo 📁 Using venv environment...
    call venv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    echo 📁 Using .venv environment...
    call .venv\Scripts\activate.bat
) else (
    echo ❌ Error: No virtual environment found. Please run 'python setup.py' first.
    pause
    exit /b 1
)

echo ✅ Virtual environment activated
echo 🚀 Launching bot...
python main.py
pause
