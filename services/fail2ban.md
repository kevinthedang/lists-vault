<div align="center">
  <p><a href="https://github.com/fail2ban/fail2ban"><img alt="pi-hole" src="../media/services/fail2ban.png" width="200px"/></a></p>
  <h1>Setup Fail2ban Framework</h1>
  <h4>The Open-Source Intrusion Prevention Software</h4>
</div>

[Fail2ban](https://github.com/fail2ban/fail2ban) is a framework that scans and monitors log files like `var/log/auth.log` to ban IP addresses conducting too many failed login attempts by updating the system's firewall to reject new connections from the IP it banned.

### Table of Contents
[Installation](#how-to-install)
[Customizing Fail2ban Client](#customizing-fail2ban-client)

## How to Install
1. Run the following commands to update and install the fail2ban client.
```sh
sudo apt update
sudo apt install fail2ban -y
```

2. Ensure that the service will run on startup.
```sh
sudo systemctl enable fail2ban
```

3. Check the status of the service.
```sh
sudo systemctl status fail2ban
```

4. If it is not loaded, start the service.
```sh
sudo systemctl start fail2ban
```

5. It should look like this if it's all ready to go!
```sh
$ sudo systemctl status fail2ban
● fail2ban.service - Fail2Ban Service
     Loaded: loaded (/usr/lib/systemd/system/fail2ban.service; enabled; preset: enabled)
     Active: active (running) since Sun 2024-11-24 10:54:47 PST; 6 days ago
       Docs: man:fail2ban(1)
   Main PID: 7580 (fail2ban-server)
      Tasks: 5 (limit: 38328)
     Memory: 18.9M (peak: 19.9M)
        CPU: 5min 16.434s
     CGroup: /system.slice/fail2ban.service
             └─7580 /usr/bin/python3 /usr/bin/fail2ban-server -xf start

Nov 24 10:54:47 <HOSTNAME_HERE> systemd[1]: Started fail2ban.service - Fail2Ban Service.
Nov 24 10:54:47 <HOSTNAME_HERE> fail2ban-server[7580]: 2024-11-24 10:54:47,700 fail2ban.configreader   [7580]: WARNING WARNING 'allowipv6' not defined in 'Definition'. Using default one: 'auto'>
Nov 24 10:54:47 <HOSTNAME_HERE> fail2ban-server[7580]: Server ready
```

6. You can check for any banned IP's on sshd.
```sh
sudo fail2ban-client status sshd
```

Example below:
```sh
$ sudo fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed: 0
|  |- Total failed:     0
|  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
`- Actions
   |- Currently banned: 0
   |- Total banned:     0
   `- Banned IP list:
```

7. If there is an IP address that you want to unban, run the following:
```sh
sudo fail2ban-client unban <IP_ADDRESS>
```

## Customizing Fail2ban Client
For now, you can just follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-20-04#step-2-configuring-fail2ban) from DigitalOcean.

If the guide above becomes outdate or unavailable. Please create an issue to replace it/create instructions for it.
