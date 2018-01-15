#!/bin/bash
easy_install pip
pip install --upgrade pip
pip install --upgrade setuptools
sudo pip install virtualenv
virtualenv ./virtualenv
./virtualenv/bin/pip install --upgrade pip
./virtualenv/bin/pip install setuptools --upgrade
./virtualenv/bin/pip install request==0.0.22
./virtualenv/bin/pip install awsauth==0.3.3
