#!/bin/bash

mkdir /home/mike/scripts/dir_for_app && cd /home/mike/scripts/dir_for_app

sudo apt -y install python3 python3-pip python3-venv curl

wget https://www.dropbox.com/s/ija7ax3sj6ysb0p/blocknote-master.tar.gz
tar -xvf blocknote-master.tar.gz
cd blocknote-master
curl https://raw.githubusercontent.com/Shach1/trpp_pr2/master/requirements.txt -o requirements.txt

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
