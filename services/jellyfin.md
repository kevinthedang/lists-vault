<div align="center">
  <p><a href="https://pi-hole.net/"><img alt="pi-hole" src="../media/services/jellyfin.png" width="100px"/></a></p>
  <h1>Jellyfin</h1>
  <h4>The Free Software Media System</h4>
</div>

* [Jellyfin](https://jellyfin.org/) is an Free Software Media System. You can also download it from the url provided.
* [Jellyfin Installation](https://jellyfin.org/docs/general/installation/)
* [GitHub Repository](https://github.com/jellyfin/jellyfin)

### Installation
> [!NOTE]
> For users that are not using Debian/Ubuntu, it is recommended to use containers instead of directly installing it. A guide is provided [here](https://jellyfin.org/docs/general/installation/container/).

The following guide will be shown through Ubuntu (and Ubuntu derivatives):
1. Curl the shell script and verify it is the correct script.
```sh
curl -s https://repo.jellyfin.org/install-debuntu.sh -O
```

> [!WARNING]
> You should always verify these scripts are not harmful for your system. You can do this with sha256sum to make sure the file is correct and not tampered. You should also read through it!  
> You can do this by running `less install-debuntu.sh`

2. Verify shell script
```sh
curl -s https://repo.jellyfin.org/install-debuntu.sh.sha256sum -O && \
sha256sum -c install-debuntu.sh.sha256sum
```

> [!NOTE]
> Expected output should be `install-debuntu.sh: OK` from the sha256sum.

3. Execute shell install script
```sh
sudo bash install-debuntu.sh
```

4. Verify Jellyfin Service

The Jellyfin script already checks but it's good to verify!

```sh
sudo systemctl status jellyfin
```

5. It will provide an ip address and port to check it out!

Example: `http://192.168.0.120:8096`

6. Follow the steps to setup an Admin account and setup a folder for you media.