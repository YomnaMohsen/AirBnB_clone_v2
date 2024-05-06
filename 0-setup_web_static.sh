#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/  /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sh -c 'echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;
         location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
        location /hbnb_static/ {
            alias /data/web_static/current/;
        }    
                               
    }"  > /etc/nginx/sites-enabled/default'                                                                             23,20-27      21%
sudo service nginx restart