# Here you define the hosts for the staging environment
from pyinfra import operations

docker_servers = ["192.168.159.129"]

backup_servers = [("selfhosted", {"users": [{"name": "backup", "groups": []}]})]
