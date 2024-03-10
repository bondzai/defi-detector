#!/bin/bash

# Change directory to the script's directory
cd "$(dirname "$0")"

source env/bin/activate
python src/main.py
