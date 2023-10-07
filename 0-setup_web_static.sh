#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get -y install nginx

web_static_dir="/data/web_static"
test_release_dir="$web_static_dir/releases/test"
current_dir="$web_static_dir/current"

sudo mkdir -p "$web_static_dir" "$test_release_dir" "$current_dir" "$web_static_dir/shared"
sudo echo "Test Page" > "$test_release_dir/index.html"
sudo ln -sf "$test_release_dir" "$current_dir"

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
