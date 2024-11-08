<div align="center">
  <h1>Setup Pi-Hole Ad-Blocker</h1>
  <h4>The Open-Source Network-Wide Ad-Blocker</h4>
</div>

[Pi-hole](https://pi-hole.net/) is a network-wide ad-blocker for linux.
[Github Repository](https://github.com/pi-hole/pi-hole)

### Methods of Installation
#### Automated Install
This is the faster installation path. Use the following command:
```sh
curl -sSL https://install.pi-hole.net | bash
```

#### Docker Install
Make sure you have docker on your system.

For Pi's/System you can run the following:
```sh
curl -sSL https://get.docker.com | sh
```

The Pi-Hole quick start guide can be found [here](https://github.com/pi-hole/docker-pi-hole/?tab=readme-ov-file#running-dhcp-from-docker-pi-hole).

Now you can follow [this guide](https://github.com/pi-hole/docker-pi-hole/#running-pi-hole-docker) to install Pi-Hole on Docker.

There is setup for running DHCP from Docker Pi-Hole, refer [here](https://github.com/pi-hole/docker-pi-hole/?tab=readme-ov-file#running-dhcp-from-docker-pi-hole).

There is a VPN [recommendation and setup](https://docs.pi-hole.net/guides/vpn/openvpn/overview/) with the Pi-Hole to use it anywhere.

#### Manual Install

##### Method 1: Clone the Pi-hole repo and run
Run the following 3 commands:
```sh
git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

##### Method 2: Manually download the installer and run
Run the following 2 commands:
```sh
wget -O basic-install.sh https://install.pi-hole.net
sudo bash basic-install.sh
```
