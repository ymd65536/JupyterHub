#!/bin/bash

# pwd => 
sudo mkdir ../../opt/jupyterhub
sudo mkdir ../jupyter/notebooks
sudo /usr/local/bin/jupyterhub -f ../../opt/jupyterhub/jupyterhub_config.py --generate-config

sudo vi ../../opt/jupyterhub/jupyterhub_config.py
