#!/bin/bash

# create JupyterHub Env

sudo useradd jupyter
sudo usermod -G wheel jupyter
passwd jupyter

python3 -V
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install jupyterhub jupyterlab notebook

sudo yum -y update
sudo yum -y install gcc-c++
sudo yum -y install git
git clone https://github.com/creationix/nvm.git ~/.nvm

source ~/.nvm/nvm.sh

vi .bash_profile

nvm ls-remote | grep "(Latest LTS*"
nvm install 14.19.3
nvm use v14.19.3
node -v
npm install -g configurable-http-proxy
