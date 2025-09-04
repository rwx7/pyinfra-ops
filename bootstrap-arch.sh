#!/bin/bash

if [ ! -d .venv ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pyinfra
else
    source .venv/bin/activate
fi

pyinfra --sudo -y \
    --data desktop_user=$(whoami) \
    --data shared_dir=/home/shared \
    @local arch-bootstrap.py
