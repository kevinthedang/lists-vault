<div align="center">
  <p><a href="https://www.docker.com/"><img alt="java" src="../media/tools/docker.png" width="200px"/></a></p>
  <h1>Docker</h1>
  <h4>Package and Run Application in Lightweight Containers</h4>
</div>

Docker provides tools for working with AI across your development workflow. Each tool serves a different purpose.

### Install Docker Engine
You can follow the official [Docker Install](https://docs.docker.com/engine/install/) walkthrough.

1. For the most part, you can follow the walkthrough above. Make sure you follow the correct guide.

> [!NOTE]
> For example, Linux Mint Cinnamon would be Ubuntu because it is a Ubuntu derivative. Not officially supported but may work.

> [!NOTE]
> The following installation guide will follow Ubuntu. Other installation walkthroughs can be made with different markdown files in the future if needed.

> [!WARNING]
> Please consider the following security implications and firewall incompatibilties provided by Docker.
> * If you use ufw or firewalld to manage firewall settings, be aware that when you expose container ports using Docker, these ports bypass your firewall rules. For more information, refer to [Docker and ufw](https://docs.docker.com/engine/network/packet-filtering-firewalls/#docker-and-ufw).
> * Docker is only compatible with iptables-nft and iptables-legacy. Firewall rules created with nft are not supported on a system with Docker installed. Make sure that any firewall rulesets you use are created with iptables or ip6tables, and that you add them to the DOCKER-USER chain, see [Packet filtering and firewalls](https://docs.docker.com/engine/network/packet-filtering-firewalls/).

2. Uninstall Old Docker

```sh
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc docker-buildx podman-docker containerd runc | cut -f1)
```

It's okay if it reports that none are installed.

> [!NOTE]
> Images, containers, volumes, and networks stored in `/var/lib/docker/` aren't automatically removed when you uninstall Docker. If you want to start with a clean installation, and prefer to clean up any existing data, read the [uninstall Docker Engine](https://docs.docker.com/engine/install/ubuntu/#uninstall-docker-engine) section.

3. Install using Docker's `apt` repository

#### Setup Docker `apt` Repository

```sh
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Then:

```sh
# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

Finally:

```sh
sudo apt update
```

#### Install Docker Packages

```sh
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

4. Verify Docker Installation

```sh
sudo systemctl status docker
```

If it is not online:

```sh
sudo systemctl start docker
```

Run the following to test it out!

```sh
sudo docker run hello-world
```

5. Run Docker as non-root User

If the group `docker` does not exist:

```sh
sudo groupadd docker
```

Add your user to the group:

```sh
sudo usermod -aG docker $USER
```

Now logout and log in. Or do the following:

```sh
newgrp docker
```

> [!NOTE]
> If this is in a VM (Virtual Machine), it is recommended to restart the VM.

Run:

```sh
docker run hello-world
```

> [!NOTE]
> **From the Docker Guide**: If you initially ran Docker CLI commands using sudo before adding your user to the docker group, you may see the following error:
>
> ```sh
> WARNING: Error loading config file: /home/user/.docker/config.json -
> stat /home/user/.docker/config.json: permission denied
> ```
> This error indicates that the permission settings for the ~/.docker/ directory are incorrect, due to having used the sudo command earlier.
>
> To fix this problem, either remove the ~/.docker/ directory (it's recreated automatically, but any custom settings are lost), or change its ownership and permissions using the following commands:
>
> ```sh
> sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
> sudo chmod g+rwx "$HOME/.docker" -R
> ```

6. Enable Docker on Startup

Run:

```sh
sudo systemctl enable docker.serivce
sudo systemctl enable containerd.service
```

To disable on startup:

```sh
sudo systemctl disable docker.serivce
sudo systemctl disable containerd.service
```

That's it for now! You should have docker working on your system!