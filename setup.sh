#!/bin/bash

# Update the package list
sudo apt-get update

# Install Python 3 and pip if not already installed
sudo apt-get install -y python3 python3-pip

# Install the required Python packages system-wide, overriding restrictions
pip install --break-system-packages -r requirements.txt
