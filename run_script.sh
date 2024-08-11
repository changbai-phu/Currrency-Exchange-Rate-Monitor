#!/bin/bash

# Path to the Python virtual environment
VENV_PATH="/Users/peggyhu/Downloads/vscode/CurrencyMonitor/venv"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Path to the Python script
PYTHON_SCRIPT="/Users/peggyhu/Downloads/vscode/CurrencyMonitor/CERM_daily_report.py"

# Run the Python script
python "$PYTHON_SCRIPT"

# Deactivate the virtual environment (optional, as it is done automatically when the script ends)
deactivate
