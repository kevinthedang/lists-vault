<div align="center">
  <p><a href="https://github.com/ansible/ansible"><img alt="ansible" src="../media/tools/ansible.png" width="200px"/></a></p>
  <h1>Ansible</h1>
  <h4>Open Source Automation System</h4>
</div>

Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain.

* [Ansible Docs](https://docs.ansible.com/)
* [Ansible Repository](https://github.com/ansible/ansible)
* [Ansible for DevOps](https://github.com/geerlingguy/ansible-for-devops) by [Jeff Geerling](https://github.com/geerlingguy)

> [!NOTE]
> This installation guide will reference Ansible for DevOps  
> This guide will also go through the linux installation

> [!NOTE]
> Ansible's only real dependency is Python. Get that installed first.

### Installing Ansible

1. Easiest way is to use `apt` for ubuntu/debian.

```sh
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
```

> [!NOTE]
> If you receive a `sudo: add-apt-repository: command not found`, you are probable missing the `software-properties-common` package. Install it with:  
> ```sh  
> sudo apt-get install software-properties-common  
> ```

2. Ansible should now be isntall. Make sure it is working properly by entering:

```sh
ansible --version
```

You should see something like this:

```sh
$ ansible --version
ansible [core 2.14.6]
    ...
    python version = 3.10.11
    jinja version = 3.1.2
    libyaml = True
```

### Basic Inventory
Ansible uses an inventory file (list of servers) to communicate with the servers.

1. Create a host file

```sh
mkdir test-project
cd test-project
touch hosts.ini
```

2. Go into the `hosts.ini` file (vim, nano, whatever) and put the following:

```
[example]
www.example.com
```

where `example` is the group of servers you are managing and `www.example.com` is the domain name (or IP address) of a server in that group. If not using port 22 for SSH on a server, you need to add it to ther address, like `www.example.com:2222` since Ansible with default to port 22 and will not get this from the ssh config file.

For example in your home network:

```
[pi-cluster]
192.168.0.20
192.168.0.21
192.168.0.22
192.168.0.23
```

### First Ad-Hoc Ansible Command
Ansible is installed and we have an inventory file. Let's run a command to see if everything works!

1. Enter the following command (something safe for now):

```sh
ansible -i hosts.ini example -m ping -u [username]
```

`[username]` us the user you would use to log into the server. If everything works you should see a message that shows `www.example.com | SUCCESS >>`, then the result of the ping. If it does not work, run it again with `-vvvv` at the end to see a verbose output. Possible issue is that the SSH keys are not properly configured. if you can ssh with `ssh username@www.example.com` then it should work!

> [!NOTE]
> Ansible assumes passworless (key-based) login for SSH. You can use passwords using `--ask-pass` but this is not recommended.

2. Let's run a more useful command

```sh
ansible -i hosts.ini example -a "free -h" -u [username]
```

This example will just show memory usage that is human readable for all servers in this `example` group. Commands like these are great for servers that are behaving out of the "normal" way.

### Summary
That is the basics for now. We got:

1. Ansible installed
2. Basic inventory to tell it about your servers
3. Ran a couple commands through Ansible.