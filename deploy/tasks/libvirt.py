# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra import host
from pyinfra.operations import files, pacman, systemd, server

desktop_user = host.data.desktop_user

pacman.packages(
    name="Ensure libvirt pakages",
    packages=[
        "qemu-full",
        "virt-manager",
        "virt-viewer",
        "dnsmasq",
        "bridge-utils",
        "libguestfs",
        "ebtables",
        "vde2",
        "openbsd-netcat",
    ],
)

files.line(
    name="Set unix socket group",
    path="/etc/libvirt/libvirtd.conf",
    line="#unix_sock_group",
    replace='unix_sock_group="libvirt"',
)

files.line(
    name="Set unix socket rw perms",
    path="/etc/libvirt/libvirtd.conf",
    line="#unix_sock_rw_perms",
    replace='unix_sock_rw_perms="0770"',
)

server.user(
    name=f"Add user '{desktop_user}' to libvirt group",
    user=desktop_user,
    groups=["libvirt"],
    append=True,
    present=True,
)

systemd.service(
    name="Ensure libvirtd service is enabled and running",
    service="libvirtd.service",
    running=True,
    restarted=True,
    enabled=True,
)
