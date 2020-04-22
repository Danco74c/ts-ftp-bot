#!/bin/bash
  
FOLDER=$1
USER=$2
PASSWORD=$3
ENCRYPTED=$(openssl passwd $PASSWORD)

if [ `sudo /bin/egrep  -i "^${USER}:" /etc/passwd` ]; then
        echo "User $USER exists in /etc/passwd" >> /home/FTPscript/user.txt
else
        echo "User $FOLDER now added to /etc/passwd" >> /home/FTPscript/user.txt
	
        sudo mkdir -p /home/FTPserver/$FOLDER
        sudo useradd -d /home/FTPserver/$FOLDER/ -m $USER -p $ENCRYPTED
        sudo chown -R $USER:$USER /home/FTPserver/$FOLDER
        sudo chmod 755 /home/FTPserver/$FOLDER
        echo -e "${PASSWORD}\n${PASSWORD}" | passwd $USER
fi
