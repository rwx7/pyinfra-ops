import os

from pyinfra.operations import server, files
from pyinfra import local

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# if 'db_servers' in host.groups:
#     local.include('tasks/database.py')

roles = [
    "tasks/install_docker.py",
    "tasks/create_user.py",
    "tasks/install_essential_packages.py",
]

for role in roles:
    local.include(role)
