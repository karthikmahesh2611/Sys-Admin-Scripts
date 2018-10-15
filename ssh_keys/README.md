The script will transfer the rsa public keys to all the servers added to your /ets/hosts file
The script has been configured to skip the first two lines in /etc/hosts which is basically localhost

Make sure you have created the rsa keys before hand on the server using below command

$ ssh-keygen -t rsa


