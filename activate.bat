@echo off
set ENV_DIR=venv
SET ACTIVE_SCRIPT="%~dp0%ENV_DIR%\Scripts\activate.bat"

if not exist "%~dp0%ENV_DIR%" (
  echo init virtual env...
  pushd "%~dp0"
  python -m virtualenv %ENV_DIR%
  echo ::=============BOT=ENV=VARS==================>> %ACTIVE_SCRIPT%
  echo SET BOT_TOKEN="PLEASE SET VALID VALUE">> %ACTIVE_SCRIPT%
  echo ::===========================================>> %ACTIVE_SCRIPT%
  call %ACTIVE_SCRIPT%
  echo upgrade pip...
  python -m pip install --upgrade pip
  echo install requirements
  pip install -r requirements.txt
  echo !!! please manually add env vars into %~dp0.venv\Scripts\activate.bat !!!
) else (
  call %ACTIVE_SCRIPT%
  pip install -r requirements.txt
)
start "VEnv" cmd