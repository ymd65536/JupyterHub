#!/bin/bash
sudo systemctl stop jupyterhub.service
sudo systemctl start jupyterhub.service
sudo systemctl status jupyterhub.service
