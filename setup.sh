#!/bin/bash

# Update system
sudo yum update -y

# Install Python and development tools
sudo yum install python3 python3-pip python3-devel nginx git -y

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Setup Nginx
sudo cp nginx_config /etc/nginx/conf.d/portfolio.conf
sudo systemctl start nginx
sudo systemctl enable nginx

# Setup Gunicorn service
sudo cp portfolio.service /etc/systemd/system/
sudo systemctl start portfolio
sudo systemctl enable portfolio

# Setup firewall
sudo ufw allow 'Nginx Full'
sudo ufw allow ssh
sudo ufw --force enable 