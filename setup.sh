#!/usr/bin/env bash

ACTIVATE="venv/bin/activate"

echo "Creating pythonic environment"

if [ ! -f $ACTIVATE ]; then
    echo "Creating venv for provisioning"
    python3 -m venv venv
fi

. $ACTIVATE
pip install --upgrade setuptools pip wheel
pip install -r requirements.txt

echo "Run source venv/bin/activate"
