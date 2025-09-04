#!/bin/bash

set -exuo pipefail

apt update
apt upgrade -y

apt-get install -y openssh-server
