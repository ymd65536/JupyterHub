#!/bin/bash

# jupyterhub user add operations

username="${1}"

# some operation
sudo useradd -p $(perl -e 'print crypt("password", "\$6\$salt03")') -d /home/$username -G jupyter $username
sudo mkdir /home/$username/notebooks
sudo chmod 777 /home/$username/notebooks
