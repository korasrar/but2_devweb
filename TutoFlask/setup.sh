#!/bin/bash

echo "Running setup_run.sh script..."

virtualenv -p python3 venv

source venv/bin/activate  

pip install -r requirements.txt

flask loaddb monApp/data/data.yml

echo "Generate a default user (default/password)"

flask newuser default password