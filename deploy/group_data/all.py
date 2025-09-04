import os

with open(os.path.expanduser("~/.ssh/id_ed25519.pub"), "r") as file:
    authorized_keys = file.read()

ssh_user = "root"

# set SSH password if using password authentication
# ssh_password = "password"

# set server SSH port
sshd_port = 22

# create privileged users
users = [
    # {"name": "whale", "groups": ["docker"]},
    {"name": "hydrogen", "groups": ["sudo"]},
    {"name": "helium", "groups": ["sudo"]},
    {"name": "lithium", "groups": ["sudo"]},
]

# volume to store files that should be backed up
data_volume = "/datavol"
