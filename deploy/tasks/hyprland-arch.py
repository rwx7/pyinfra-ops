# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra.operations import files, pacman, systemd, server

pacman.packages(
    name="Ensure hyprland pakages",
    packages=[
        "hyprland",
        "hyprpaper",
        "hyprpolkitagent",
        "rofi-wayland",
        "waybar",
        "mako",
        "foot",
        "swww",
        "uwsm",
        "libnewt",
        # plugins
        "cmake",
        "meson",
        "cpio",
        "gcc",
    ],
)

#
# ninja
# gcc
# cmake
# meson
# libxcb
# xcb-proto
# xcb-util
# xcb-util-keysyms
# libxfixes
# libx11
# libxcomposite
# libxrender
# libxcursor
# pixman
# wayland-protocols
# cairo
# pango
# libxkbcommon
# xcb-util-wm
# xorg-xwayland
# libinput
# libliftoff
# libdisplay-info
# cpio
# tomlplusplus
# hyprlang-git
# hyprcursor-git
# hyprwayland-scanner-git xcb-util-errors hyprutils-git glaze hyprgraphics-git aquamarine-git re2 hyprland-qtutils
#