# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra.operations import files, pacman, systemd, server

# 7zip is used for `7z b` benchmarking
pacman.packages(
    name="Ensure essential terminal packages",
    packages=["neovim", "zsh", "htop", "7zip", "tmux", "os-prober"],
)

# pacman.packages(
#     name="Ensure desktop services",
#     packages=[
#         "keyd",
#     ],
# )

# pacman.packages(
#    name="Ensure Gnome extensions browser connector",
#    packages=[
#        "gnome-browser-connector",
#    ],
# )

# pacman.packages(
#     name="Ensure sway packages",
#     packages=["sway", "foot", "fuzzel"],
# )

# pacman.packages(
#     name="Ensure hyprland packages",
#     packages=["hyprland", "swww", "waybar", "foot", "rofi-wayland", "uwsm", "mako"],
# )


# {{{ Fix unsynced time ater install. Related to timezones.

timesyncd_conf = "/etc/systemd/timesyncd.conf.d/local.conf"

files.directory(
    path="/etc/systemd/timesyncd.conf.d",
    present=True,
)

files.template(src="deploy/templates/timesync.conf", dest=timesyncd_conf, mode="644")

systemd.service(
    service="systemd-timesyncd.service",
    restarted=True,
    enabled=True,
)

# }}}


files.line(
    name="Slightly increase faillock attempts",
    path="/etc/security/failelock.conf",
    line=r"# deny =",
    replace="deny = 6",
)


files.line(
    name="Update GRUB config",
    path="/etc/default/grub",
    line=r"#GRUB_DISABLE_OS_PROBER=false",
    replace="GRUB_DISABLE_OS_PROBER=false",
)

server.shell(
        name="Update GRUB entries",
        commands=["grub-mkconfig -o /boot/grub/grub.cfg"],
)

