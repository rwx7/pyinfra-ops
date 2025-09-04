from pyinfra import host
from pyinfra.operations import files, server
from io import StringIO


def write_authorized_keys(user: str):
    ssh_dir = "/root/.ssh" if user == "root" else f"/home/{user}/.ssh"

    files.directory(
        name=f"Ensure {ssh_dir} exists", path=ssh_dir, mode="700", user=user, group=user
    )

    files.put(
        name=f"Write authorized_keys to {ssh_dir}",
        src=StringIO(host.data.authorized_keys),
        dest=f"{ssh_dir}/authorized_keys",
        mode="600",
        user=user,
        group=user,
    )


for user_info in host.data.users:
    user = user_info["name"]
    groups = user_info["groups"]
    server.user(
        name=f"Ensure {user} user exists",
        user=user,
        home=f"/home/{user}",
        groups=user_info["groups"],
        shell="/bin/bash",
    )

    write_authorized_keys(user)


write_authorized_keys("root")