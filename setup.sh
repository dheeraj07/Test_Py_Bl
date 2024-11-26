#!/bin/bash

# Update and install dependencies
sudo apt-get update && sudo apt-get install -y python3 python3-pip unzip

# Install project dependencies (if applicable)
pip3 install -r requirements.txt
