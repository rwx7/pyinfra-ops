from pyinfra.operations import files, systemd

files.replace(
    name="Change /etc/issue to show IP4 address",
    path="/etc/issue",
    text="\\\\l",
    replace="\\\\l \\\\4",
)
