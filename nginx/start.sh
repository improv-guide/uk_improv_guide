#!/usr/bin/env bash

export data_path=/etc/letsencrypt
export domains=improv.guide
export cert_dir="$data_path/live/$domains"
export key_dir="$cert_dir/$domains"

echo "Certificate dir: $cert_dir"
echo "Key Dir: $key_dir"

if [ ! -e "$data_path/options-ssl-nginx.conf" ] || [ ! -e "$data_path/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  mkdir -p "$data_path/conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf > "$data_path/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem > "$data_path/ssl-dhparams.pem"
  echo
fi

if [ ! -e "$data_path/options-ssl-nginx.conf" ] || [ ! -e "$data_path/ssl-dhparams.pem" ]; then
    echo "Fetching options-ssl-nginx.con & ssl-dhparams.pem"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf > "$data_path/options-ssl-nginx.conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem > "$data_path/ssl-dhparams.pem"
fi


if [ ! -e "$key_dir/privkey.pem" ] || [ ! -e "$key_dir/fullchain.pem" ]; then
      echo "### Creating dummy certificate for $domains ..."

      echo "Making directory $key_dir"
      mkdir -p $key_dir
      openssl req -x509 -nodes -newkey rsa:2048 -days 1\
        -keyout "$key_dir/privkey.pem" \
        -out "$key_dir/fullchain.pem" \
        -subj '/CN=localhost'
    echo
fi

if [ ! -d "$cert_dir" ]; then
    echo "Starting without SSL"
    export NGINX_CONFIG=/etc/nginx/no_ssl.conf
else
    echo "Starting with SSL."
    export NGINX_CONFIG=/etc/nginx/ssl.conf
fi

echo "Booting Nginx"
nginx -c $NGINX_CONFIG -g 'daemon off;'