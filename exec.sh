#!/bin/bash

# Change directory to the script's directory
cd "$(dirname "$0")"

# Execute the task with the Taskfile in the same directory
task run
