from pyinfra.operations import server

server.script_template(
    name="Ensure soft git server is installed and running",
    src="templates/install-git-server.sh.j2",
)
