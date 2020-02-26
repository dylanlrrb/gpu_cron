#!/bin/bash

cd ~/gpu_cron
source	~/gpu_cron/bin/activate
git pull
pip3 install -r requirements.txt
python3 run.py
