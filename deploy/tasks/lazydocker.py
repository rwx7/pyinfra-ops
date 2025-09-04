from pyinfra import host
from pyinfra.operations import files, server
from shutil import which

version="0.23.3"
# The URL to download from
url = f"https://github.com/jesseduffield/lazydocker/releases/download/v{version}/lazydocker_{version}_Linux_x86_64.tar.gz"
# Where to store the downloaded file
dest_dir = "/opt/archives"
archive = f"lazydocker_{version}.tar.gz"

files.directory(
    path=dest_dir,
    present=True,
    recursive=True,
)

download = files.download(
    name=f"Download lazydocker {version}",
    src=url,
    dest=f"{dest_dir}/{archive}",
    #sha256sum=host.data.tool_sha256,
)

if which("lazydocker") is None or download.changed:
    server.shell(
      name="Unpack lazydocker and move content to destination",
      commands=[
        f"""
        cd {dest_dir} &&
            # archive does not have a top level directory, create one to keep dir tidy
            mkdir -p lazydocker_{version} &&
            cd lazydocker_{version} &&
            tar -xf ../{archive} &&
            chmod +x lazydocker &&
            cp lazydocker /usr/local/bin
        """,
      ]
    )
