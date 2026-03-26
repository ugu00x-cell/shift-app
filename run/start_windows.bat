@echo off
cd /d "%~dp0.."

echo ==========================================
echo   Starting Shift App...
echo   Browser will open automatically.
echo.
echo   If not, open: http://localhost:5050
echo.
echo   To stop: close this window.
echo ==========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found.
    echo Please run setup_and_start.bat first.
    pause
    exit /b 1
)

python app.py

pause
