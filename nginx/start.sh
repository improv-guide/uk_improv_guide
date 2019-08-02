#!/usr/bin/env bash

export data_path=/etc/letsencrypt
export domains=improv.guide
export path="/etc/letsencrypt/live/$domains"

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  mkdir -p "$data_path/conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem > "$data_path/conf/ssl-dhparams.pem"
  echo
fi


if [ ! -d $path ]; then
    echo "Making the directory $path"
    mkdir -p $path
    echo
fi;

if [ ! -e "$path/privkey.pem" ] || [ ! -e "$$path/fullchain.pem" ]; then
    echo "### Creating dummy certificate for $domains ..."
    export key_dir=$data_path/conf/live/$domains
    echo "Making directory $key_dir"
    mkdir -p $key_dir
      openssl req -x509 -nodes -newkey rsa:1024 -days 1\
        -keyout "$path/privkey.pem" \
        -out "$path/fullchain.pem" \
        -subj '/CN=localhost'
    echo
fi

if [ ! -e "$data_path/options-ssl-nginx.conf" ] || [ ! -e "$data_path/ssl-dhparams.pem" ]; then
    echo "Fetching options-ssl-nginx.con & ssl-dhparams.pem"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf > "$data_path/options-ssl-nginx.conf"
    curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem > "$data_path/ssl-dhparams.pem"
fi

nginx -g 'daemon off;'