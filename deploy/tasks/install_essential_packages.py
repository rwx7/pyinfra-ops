from pyinfra.operations import apt, pacman, files


# apt.packages(
#     name="Install essential packages.",
#     packages=["openssh-server", "net-tools", "sudo", "curl", "git"],
# )

pacman.packages(
        name = "Install essential packages",
        packages = ["nvim"]
)

pacman.packages(
        name = "Install user desktop packages",
        packages = ["zsh"]
)

files.template(
    name="Restrict SSH login to public keys.",
    src="templates/sshd_config_keys_only.j2",
    dest="/etc/ssh/sshd_config",
)