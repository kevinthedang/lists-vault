<div align="center">
  <p><a href="https://networkupstools.org/"><img alt="nut" src="../media/tools/nut.svg" width="200px"/></a></p>
  <h1>Network UPS Tools</h1>
  <h4>Monitor, Control, and Coordinate Your UPS</h4>
</div>

[Network UPS Tools](https://networkupstools.org/) or NUT is an open source system to control your UPS hardware across you network. It is how we can make sure that our servers, NAS's, and more shut down safely during a power outage.

Guide references the following:
* [pi-nut](https://github.com/geerlingguy/pi-nut)
* [Jeff Geerlings pi-nut blog](https://www.jeffgeerling.com/blog/2025/nut-on-my-pi-so-my-servers-dont-die/)

> [!NOTE]
> Network UPS Tools does not require much power so having a dedicated efficient computer (like a Raspberry Pi) helps!

### Configure NUT

1. Install NUT on your system

```sh
sudo apt install -y nut
```

This installs `nut-client`, `nut-server`, and other UPS tools for later.

> [!NOTE]
> Be sure to plug the USB cable provided with your UPS into the USB port on the UPS and on the system you are using.

2. Run `nut-scanner`

```sh
sudo nut-scanner -U
```

For example:
```sh
Scanning USB bus.
[nutdev1]
	driver = "nutdrv_qx"
	port = "auto"
	vendorid = "0665"
	productid = "5161"
	product = "UPS"
	bus = "001"
```

Take those values and put them into your UPS configuration (This assume you have only 1 UPS plugged in).

3. Edit NUT's `ups.conf` file to add the configuration

```sh
[home-office]
    driver = nutdrv_qx
    product = UPS
    desc = "Home Office CyberPower Rack UPS"
    port = auto
    vendorid = 0665
    productid = 5161
    bus = 001
```

The name of the UPS should be ASCII characters with no spaces or special characters besides `-`.

> [!NOTE]
> If you cannot connect to your UPS, or the scanner cannot find it, read through the NUT documentation on UPS drivers to see if you are missing something. You do not have to use USB for connection, it is just the most common for a modern UPS.

### Setup NUT Server
We need to make the computer that handles the UPS the "NUT Server"

1. Edit the `upsd.conf` file to add the `LISTEN` directive:

```sh
sudo nano /etc/nut/upsd.conf
```

Add:

```sh
LISTEN 0.0.0.0 3493
```

2. Save and Close

3. Add NUT users who will manage the UPS locally or through the network. Edit `upsd.users`.

```sh
sudo nano /etc/nut/upsd.users
```

Add something like:

```sh
[admin]
    password = ADMIN_PASSWORD_HERE
    actions = set
    actions = fsd
    instcmds = all
    upsmon primary

[observer]
    password = OBSERVER_PASSWORD_HERE
    upsmon secondary
```

> [!NOTE]
> `admin` will have access to do anything like sending a shutdown command (`fsd`) to all connected systems. Recommended to not use that account for all clients.  
> The `observer` is what you would use on all NUT clients to connect back and monitor the main UPS.

4. Configure the UPS monitor on the NUT server computer by editing `upsmon.conf`

```sh
sudo nano /etc/nut/upsmon.conf
```

Something like:

```sh
# Make sure you use your actual admin password...
MONITOR server-room-rack@localhost 1 admin ADMIN_PASSWORD_HERE primary

# You might also want to configure FINALDELAY and set it to a period long enough
# for your servers to all shut down, prior to the primary node shutting down and
# triggering the UPS to switch off its load, e.g. for 3 minutes:
FINALDELAY 180
```

5. Save and Close then edit the `nut.conf` changing the `MODE` from `none` to `netserver`

```sh
sudo nano /etc/nut/nut.conf
```

To:

```sh
MODE=netserver
```

6. Restart your NUT system and make sure it is enabled on boot:

```sh
sudo systemctl restart nut-server
sudo systemctl enable nut-server
sudo systemctl restart nut-monitor
sudo systemctl enable nut-monitor
```

### Verify NUT Works

1. Check using `upsc [ups-name-here]`

```sh
upsc home-office
Init SSL without certificate database
battery.charge: 24
battery.energysave: no
battery.packs: 1
battery.protection: yes
battery.runtime: 0
battery.voltage: 50.60
battery.voltage.nominal: 48.0
device.model: LILVX2K0
device.type: ups
driver.name: nutdrv_qx
...
```

### Fancy Web UI

If you would like a nice web UI to monitor this stuff here are some ideas:

* [Home Assistant](https://www.home-assistant.io/integrations/nut/)
* [NUT Web GUI](https://github.com/SuperioOne/nut_webgui)

#### Home Assistant
Some yaml for the card:

```yaml
type: vertical-stack
title: Server Room Rack UPS
cards:
  - type: history-graph
    entities:
      - name: Status
        entity: sensor.server_room_rack_status
    hours_to_show: 4
  - type: gauge
    entity: sensor.server_room_rack_battery_charge
    name: Battery Charge
    severity:
      green: 50
      yellow: 20
      red: 0
```

#### NUT Web GUI
Can run a docker container for it:

```sh
docker run \
  -e UPSD_ADDR=10.0.2.10 \
  -e UPSD_USER=observer \
  -e UPSD_PASS=PASSWORD_HERE \
  -p 9000:9000 \
  ghcr.io/superioone/nut_webgui:latest
```

Access locally via `http://localhost:9000/ups/<ups-name-here>`

### Setup NUT on Clients
The NUT server is supposed to shutdown last after sending a `fsd` notice to all clients, but the other systems need `nut-client` to get this.

On each device connected to the UPS that needs to be shutdown cleanly, do the following to connect the clients:

1. Install `nut-client` using `sudo apt install nut-client`

2. Verify connection to server: `upsc home-office@IP_ADDRESS` (IP_ADDRESS is the ip address of the NUT server)

3. Configure NUT's UPS monitor for the client:

```sh
sudo nano /etc/nut/upsmon.conf
```

Add a `MONITOR` line:

```sh
MONITOR home-office@IP_ADDRESS 1 observer PASSWORD secondary
```

`IP_ADDRESS` is the UP of the NUT server and `PASSWORD` is the observer password.

4. Edit `/etc/nut/nut.conf` and set `MODE=client`

5. Restart and enable `nut-client` 

```sh
sudo systemctl restart nut-client
sudo systemctl enable nut-client
```

Now, each server where you have `nut-client` should track the primary NUT server and should shutdown from the `fsd` notice.

### Monitoring NUT server and clients
For more verbose logs, set the `NUT_DEBUG_LEVEL` environment variable when restarting the NUT services. By default, it logs important notifications like the UPS going from `online` to `battery`.

```sh
# On server
journalctl -f -u nut-server

# On client
journalctl -f -u nut-monitor
```

### Managing the Connected UPS
On the NUT server, you can use `upscmd` to manage the connected UPS, usin the `admin` user.

For example:

```sh
# List commands supported on this UPS
upscmd -l server-room-rack

# Run a quick battery test (requires password)
upscmd -u admin server-room-rack test.battery.start.quick
```

### Testing NUT

> [!NOTE]
> Testing can result in data loss. Make sure you are not doing anything critical on your systems while you are testing your setup.

#### Nut Debug / Test Mode
Follow this -> [Nut Debug / Test Mode](https://dan.langille.org/2020/09/10/nut-testing-the-shutdown-mechanism/) guide to test your NUT setup.

#### Live Test of NUT without unplugging UPS
You can run the following to trigger a `fsd` event on the NUT server:

```sh
upsmon -c fsd
```

That will immediately emulate the condition of the UPS status `OB LB` (On Battery / Low Battery), which tells all connected systems to run their shutdown command.

#### Live end-to-end test with UPS on battery
Unplug your UPS. Monitor stats with `upsc` and validate the various parameters are correct for your UPS:

```sh
upsc home-office
battery.charge: 32
...
battery.voltage: 51.30
...
ups.load: 11
...
ups.status: OL
```

Eventually the UPS will enter a status of `OL LB` or `ALARM OB`, and NUT should trigger shutdowns on all connected NUT clients.

### Conclusion

That's it for now!

There are many other cases that can be covered by the NUT documentation like calling `fsd` sooner for high power systems.
