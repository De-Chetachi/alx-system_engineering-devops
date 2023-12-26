#!/usr/bin/env bash
#configure port forwarding

sudo su
ufw route allow 8080
echo "net/ipv4/ip_forward=1" >> /etc/ufw/sysctl.conf
sysctl -p
echo "*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT" >> /etc/ufw/before.rules
sudo systemctl restart ufw
