#!/bin/bash
easy_install pip
pip install --upgrade pip
pip install --upgrade setuptools
sudo pip install virtualenv
virtualenv ./virtualenv
./virtualenv/bin/pip install --upgrade pip
./virtualenv/bin/pip install setuptools --upgrade
