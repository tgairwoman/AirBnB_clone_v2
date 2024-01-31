#!/usr/bin/env bash
# this script that sets up your web servers for the deployment of web_static.
if [ ! -x "$(command -v nginx)" ]; then
	apt-get -y update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
  sed -i '49a\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi
service nginx restart
