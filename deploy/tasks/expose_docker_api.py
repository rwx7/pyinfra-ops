from pyinfra.operations import files, systemd

docker_service_d = "/etc/systemd/system/docker.service.d"

files.directory(name=f"Ensure {docker_service_d} exists", path=docker_service_d)

files.put(
    name=f"Write override.conf to {docker_service_d}",
    src="files/docker_remote.conf",
    dest=f"{docker_service_d}/override.conf",
)

systemd.service(
    name="Reload docker service",
    service="docker.socket",
    running=True,
    restarted=True,
    reloaded=True,
    enabled=True,
    daemon_reload=True,
)
