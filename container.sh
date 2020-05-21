curl --unix-socket /var/run/docker.sock http://localhost/containers/json

curl --unix-socket /var/run/docker.sock http://localhost/containers/ab789404daa7/stats > res.txt