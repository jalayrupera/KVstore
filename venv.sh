#!/bin/bash
PWD=`pwd`
python3.11 -m venv venv
echo $PWD
activate_venv() {
    . $PWD/venv/bin/activate
}

activate_venv

pip install -r requirements.txt