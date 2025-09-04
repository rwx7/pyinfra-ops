# NOTES

## soft-serve git server

```sh
docker volume create \
    --opt type=none \
    --opt o=bind \
    --opt device=/mnt/wd14tb_2/docker_volumes/soft_serve_vol \
    soft_serve_vol

docker run \
     --name=soft-serve \
     --volume soft_serve_vol:/soft-serve \
     --publish 23231:23231 \
     --publish 23232:23232 \
     --publish 23233:23233 \
     --publish 9418:9418 \
     --restart unless-stopped \
     -e "SOFT_SERVE_INITIAL_ADMIN_KEYS=ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFS3kvpOvsyy2HIgT3f01UsDo1f4voGJbUc3qHrvCi1N root@DESKTOP-9OMG88H" \
     -e "SOFT_SERVE_SSH_KEY_PATH=ssh://owngit" \
     -e "SOFT_SERVE_NAME=mgutz git server" \
     --detach \
     charmcli/soft-serve:latest

# copy over config.yaml by using a temporary container

# docker run --rm -v $PWD:/source -v soft_serve_vol:/dest -w /source alpine cp soft_serve.yaml /dest/config.yaml

# copy configuration file

docker cp config.yaml soft-serve:/soft-serve/config.yaml
```

## kopia

Doesn't work well with sftp and passphrase protected private keys.
Restic seems to work better for sftp.

```sh
kopia repository create sftp \
    --path=backups \
    --host=192.168.159.141 \
    --username=backup \
    --keyfile=$HOME/.ssh/id_ed25519 \
    --known-hosts=$HOME/.ssh/known_hosts
```

## minio (S3)

```sh
docker volume create minio_vol


# NOTE: password must be more than 8 chars
docker run \
    -d \
    -p 9000:9000 \
    -p 9001:9001 \
    --name minio \
    -e "MINIO_ROOT_USER=admin" \
    -e "MINIO_ROOT_PASSWORD=supersecret" \
    -v minio_vol:/data \
    --restart=unless-stopped \
    quay.io/minio/minio server /data --console-address ":9001"

# install
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  -o /usr/local/bin/mc
chmod +x /usr/local/bin/mc
```

## TODO

Grafana Loki for logs
