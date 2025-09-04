# Run with pyinfra @local arch-bootstrap.py -y
from pyinfra.operations import files, pacman, systemd, server

# 7zip is used for `7z b` benchmarking
pacman.packages(
    name="Ensure qbittorrent-nox",
    packages=["qbittorrent-nox"],
)


server.group(
    name="Create the downloader group",
    group="downloader",
    gid=11000,
)

server.user(
    name="Add user downloader to downloader group",
    user="downloader",
    groups=["downloader"],
    append=True,
    present=True,
    uid=11000,
)
