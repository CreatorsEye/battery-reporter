@echo off
title CEBT Installer for Windows
echo ========================================
echo    CEBT - Creators Eye Battery Tester
echo    Windows Installation
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python 3.6 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo After installing Python, run this installer again.
    echo.
    echo Or use the HTML GUI version instead:
    echo https://github.com/CreatorsEye/battery-reporter/tree/main/GUI/HTML
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed.
echo.

REM Create installation folder
set INSTALL_DIR=%USERPROFILE%\CEBT
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
echo [OK] Created folder: %INSTALL_DIR%
echo.

REM Copy cebt.py
copy /Y cebt.py "%INSTALL_DIR%\" >nul
echo [OK] Copied cebt.py
echo.

REM Create batch wrapper in system PATH
echo @echo off > "%WINDIR%\cebt.bat"
echo python "%INSTALL_DIR%\cebt.py" %%* >> "%WINDIR%\cebt.bat"
echo [OK] Created cebt command in system PATH
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo You can now use 'cebt' from any terminal:
echo.
echo   cebt /S     Start a new test
echo   cebt /R     Show last results
echo   cebt /C     Compare all tests
echo   cebt /L     Open last report in browser
echo   cebt /O     Set output folder
echo   cebt /H     Show help
echo.
echo Reports will be saved to:
echo   %USERPROFILE%\Documents\CEBT-Reports\
echo.
echo ========================================
pause
