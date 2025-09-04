"""
Set up a VM with docker and expose the docker remote API.
It is intended for local development.
"""

from pyinfra import local


roles = [
    # exposes docker remote API on port 2375 without TLS
    "tasks/expose_docker_api.py",
    "tasks/show_ip_on_console_login.py",
]

for role in roles:
    local.include(role)
