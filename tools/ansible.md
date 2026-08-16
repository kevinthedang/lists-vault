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
