<div align="center">
  <p><a href="https://pi-hole.net/"><img alt="pi-hole" src="../media/services/pihole-logo.svg" width="100px"/></a></p>
  <h1>Jellyfin Media System</h1>
  <h4>The Open-Source Media Server Software</h4>
</div>

[Jellyfin](https://jellyfin.org/) is an Free Software Media System. You can also download it from the url provided.
[GitHub Repository](https://github.com/jellyfin/jellyfin)

### Installation
> [!NOTE]
> For users that are not using Debian/Ubuntu, it is recommended to use containers instead of directly installing it. A guide is provided [here](https://jellyfin.org/docs/general/installation/container/).

The following guide will be shown through Ubuntu Server Noble:
1. Curl the shell script that installs Jellyfin
```sh
$ curl https://repo.jellyfin.org/install-debuntu.sh | sudo bash
```

> [!WARNING]
> You should always verify these scripts are not harmful for your system. You can do this with sha256sum to make sure the file is correct and not tampered. You should also read through it!

Install the service will use the `8096` port for accessing the service. Allow this on ufw.
```sh
$ sudo ufw allow 8096
$ sudo ufw reload
```

2. Access the web interface
You can navigate to the following address:
```
http://<ip_address_of_server>:8096
```

3. Follow the steps to setup an Admin account and setup a folder for you media.