@echo off
setlocal enabledelayedexpansion
title FastFlag Bypass Tool - Python Launcher
color 0A

echo.
echo  ================================================================================
echo                        FastFlag Bypass Tool - Python Launcher                  
echo                                   Version 2.0                                  
echo  ================================================================================
echo.

REM Check for administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo.
    echo  [WARNING] Administrator privileges recommended for optimal functionality.
    echo  Some features may not work properly without admin rights.
    echo.
    echo  To run as administrator: Right-click this file and select "Run as administrator"
    echo.
    timeout /t 3 >nul
)

echo  [INFO] Checking Python installation...

REM Check if Python is installed and accessible
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found in PATH!
    echo.
    echo  Python 3.6+ is required to run this tool.
    echo  Opening python.org in your browser for download...
    echo.
    start "" "https://www.python.org/downloads/"
    echo  [INFO] After installing Python:
    echo         1. Make sure to check "Add Python to PATH" during installation
    echo         2. Restart this script
    echo.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo  [SUCCESS] Python !PYTHON_VERSION! found!

REM Check if we're already in a virtual environment
if defined VIRTUAL_ENV (
    echo  [INFO] Already in virtual environment: !VIRTUAL_ENV!
    goto check_requirements
)

REM Check if venv directory exists
if exist "venv" (
    echo  [INFO] Virtual environment found. Activating...
    call venv\Scripts\activate.bat
    if errorlevel 1 (
        echo  [ERROR] Failed to activate virtual environment.
        echo  [INFO] Recreating virtual environment...
        rmdir /s /q venv 2>nul
        goto create_venv
    )
    echo  [SUCCESS] Virtual environment activated!
) else (
    :create_venv
    echo  [INFO] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo  [ERROR] Failed to create virtual environment.
        echo  [TIP] Make sure you have the 'venv' module installed.
        echo        Try: python -m pip install --upgrade pip
        pause
        exit /b 1
    )
    echo  [SUCCESS] Virtual environment created!
    
    echo  [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
    if errorlevel 1 (
        echo  [ERROR] Failed to activate virtual environment.
        pause
        exit /b 1
    )
    echo  [SUCCESS] Virtual environment activated!
)

:check_requirements
REM Check if requirements.txt exists, if not create a minimal one
if not exist "requirements.txt" (
    echo  [INFO] Creating requirements.txt...
    echo # FastFlag Bypass Tool Requirements > requirements.txt
    echo # No external dependencies required - uses Python standard library >> requirements.txt
    echo # This file is here for future extensibility >> requirements.txt
    echo. >> requirements.txt
    echo # Optional: Uncomment if you want colored output on older Windows versions >> requirements.txt
    echo # colorama>=0.4.4 >> requirements.txt
)

REM Check if requirements are installed (for future use)
echo  [INFO] Checking/installing requirements...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo  [WARNING] Some requirements may not have installed properly.
    echo  [INFO] This is usually not a problem as the tool uses standard libraries.
) else (
    echo  [SUCCESS] Requirements satisfied!
)

REM Check if bypass.py exists
if not exist "bypass.py" (
    echo  [ERROR] bypass.py not found in current directory!
    echo  [INFO] Make sure you're running this from the FastFlagBypass directory.
    echo  [INFO] Current directory: %CD%
    pause
    exit /b 1
)

echo.
echo  [INFO] Launching FastFlag Bypass Tool...
echo  ================================================================================
echo.

REM Run the Python script
python bypass.py

REM Check exit code
if errorlevel 1 (
    echo.
    echo  ================================================================================
    echo  [ERROR] The tool exited with an error.
    echo  [TIP] If you see permission errors, try running as administrator.
    echo  [TIP] If you see import errors, check your Python installation.
    echo  ================================================================================
    echo.
    pause
) else (
    echo.
    echo  ================================================================================
    echo  [SUCCESS] Tool completed successfully!
    echo  ================================================================================
    echo.
    timeout /t 2 >nul
)

REM Deactivate virtual environment if we activated it
if defined VIRTUAL_ENV (
    if not defined LAUNCHER_ORIGINAL_VENV (
        echo  [INFO] Deactivating virtual environment...
        deactivate 2>nul
    )
)

exit /b