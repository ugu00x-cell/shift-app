@echo off
cd /d "%~dp0"

echo ==========================================
echo   Shift App - Setup and Start
echo ==========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed.
    echo.
    echo Please install Python from:
    echo   https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during install.
    echo.
    echo After installing Python, double-click this file again.
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Install required libraries
echo Installing required libraries...
echo (This may take a few minutes on first run)
echo.
pip install Flask==3.1.0 Flask-SQLAlchemy==3.1.1 Flask-WTF==1.2.2 ortools openpyxl==3.1.5 jpholiday >nul 2>&1
if errorlevel 1 (
    echo Retrying with --user flag...
    pip install --user Flask==3.1.0 Flask-SQLAlchemy==3.1.1 Flask-WTF==1.2.2 ortools openpyxl==3.1.5 jpholiday
)
echo.
echo [OK] Libraries installed
echo.

echo ==========================================
echo   Starting Shift App...
echo   Browser will open automatically.
echo.
echo   If not, open this URL in your browser:
echo     http://localhost:5050
echo.
echo   To stop: close this window.
echo ==========================================
echo.

python app.py

pause
