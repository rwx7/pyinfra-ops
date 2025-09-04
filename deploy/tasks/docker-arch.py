# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra import host
from pyinfra.operations import files, pacman, systemd, server

desktop_user = host.data.desktop_user
shared_dir = host.data.shared_dir

pacman.packages(
    name="Installed pacman docker packages",
    packages=[
        "docker",
        "docker-compose",
        "docker-buildx",
    ],
)

files.directory(
    name=f"Ensure {shared_dir}/docker",
    path=f"{shared_dir}/docker",
    present=True,
)

files.link(
    name=f"Link {shared_dir}/docker to /var/lib/docker",
    path="/var/lib/docker",
    target=f"{shared_dir}/docker",
    symbolic=True,
    force=True,
)

server.user(
    name=f"Add user '{desktop_user}' to docker group",
    user=desktop_user,
    groups=["docker"],
    append=True,
    present=True,
)

systemd.service(
    name="Ensure docker socket service is enabled and running",
    service="docker.socket",
    running=True,
    restarted=True,
    enabled=True,
)
