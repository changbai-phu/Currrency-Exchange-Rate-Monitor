#!/bin/bash

# Path to the Python virtual environment - input your own path below
VENV_PATH="/Users/Downloads/vscode/CurrencyMonitor/venv"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Path to the Python script - input your own path below
PYTHON_SCRIPT="/Users/Downloads/vscode/CurrencyMonitor/CERM_daily_report.py"

# Run the Python script
python "$PYTHON_SCRIPT"

# Deactivate the virtual environment (optional, as it is done automatically when the script ends)
deactivate
