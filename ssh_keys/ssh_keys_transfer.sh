#!/bin/bash

for server in $(awk 'NR > 2 {print $1}' /etc/hosts)
do
cat ~/.ssh/id_rsa.pub | ssh root@$server "mkdir -p .ssh; cat >> .ssh/authorized_keys; chmod 700 .ssh; chmod 640 .ssh/authorized_keys"
done
