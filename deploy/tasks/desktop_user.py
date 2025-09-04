# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra import host
from pyinfra.operations import files, pacman, systemd, server

desktop_user = host.data.desktop_user

server.group(
    name="Create the community group",
    group="community",
    gid=10100,
)

server.user(
    name=f"Add user '{desktop_user}' to community group",
    user=desktop_user,
    groups=["community", "input"],
    append=True,
    present=True,
)

files.directory(
    name="Recursively set ownership for /home/community",
    path="/home/community",
    group="community",
    # Set the group ownership to 'community' and forces
    # new fiiles to inherit this group.
    mode="2775",
    recursive=True,
)