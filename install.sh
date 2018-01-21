#!/bin/bash
easy_install pip
pip install --upgrade pip
pip install --upgrade setuptools
#sudo pip install virtualenv
#virtualenv ./virtualenv
pip install --upgrade pip
pip install setuptools --upgrade
pip install boto==2.48.0
pip install logger==1.4

pip install request==0.0.22
pip install awsauth==0.3.3
yum install mysql-devel gcc python-devel -y
pip install MySQL-python