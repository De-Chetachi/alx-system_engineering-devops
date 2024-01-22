#!/usr/bin/env bash
#
sudo apt-get -y update
sudo apt install -y certbot
certbot certonly --standalone -d www.chedevops.tech

