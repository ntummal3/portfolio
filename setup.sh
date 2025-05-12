#!/bin/bash

# Update system
sudo apt update
sudo apt upgrade -y

# Install required packages
sudo apt install -y python3-pip python3-venv nginx

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Setup Nginx
sudo cp nginx_config /etc/nginx/sites-available/portfolio
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# Setup systemd service
sudo cp portfolio.service /etc/systemd/system/
sudo systemctl start portfolio
sudo systemctl enable portfolio

# Setup firewall
sudo ufw allow 'Nginx Full'
sudo ufw allow ssh
sudo ufw --force enable 