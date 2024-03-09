#!/bin/bash

# Determine the Chrome version
CHROME_VERSION=$(google-chrome --version | grep -oE "[0-9]+")

# Download the compatible ChromeDriver version
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}

# Extract the downloaded zip file
unzip /tmp/chromedriver.zip -d /tmp/

# Remove the existing ChromeDriver from PATH
sudo rm /usr/local/bin/chromedriver

# Move the newly downloaded ChromeDriver to the PATH
sudo mv /tmp/chromedriver /usr/local/bin/

# Set appropriate permissions
sudo chmod +x /usr/local/bin/chromedriver

echo "ChromeDriver version for Chrome $CHROME_VERSION has been updated successfully."
