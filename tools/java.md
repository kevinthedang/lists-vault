<div align="center">
  <p><a href="https://www.java.com/en/"><img alt="java" src="../media/tools/java.png" width="150px"/></a></p>
  <h1>Java</h1>
  <h4>The Classic Class-Based, Object-Oriented Programming Language</h4>
</div>

[Java](https://www.java.com/en/) is a class-based, object-oriented programming language that was first released by Sun Microsystems in 1995 and later acquired by Oracle Corporation.
* [Azul Zulu JDK](https://www.azul.com/downloads/#zulu)
* [OpenJDK](https://openjdk.org/) and consider downloading from [here](https://adoptium.net/)
* [Oracle JDK](https://www.oracle.com/java/technologies/downloads/)

### Table of Contents
* [Installation](#installation)
    * [OpenJDK](#openjdk)
    * [Azul Zulu JDK](#azul-zulu-jdk)
* [Security](#securing-java-in-your-system)

### Installation
Installation will vary between systems.

#### OpenJDK
Good for general-purpose use and development.

1. Update Repository and search for what JDK you want:
```sh
sudo apt update
apt-cache search openjdk
```

You should see something like this:
```sh
openjdk-11-jdk - OpenJDK Development Kit (JDK)
openjdk-17-jdk - OpenJDK Development Kit (JDK)
openjdk-20-jdk - OpenJDK Development Kit (JDK)
```

2. Install OpenJDK
We'll install Java 17 for this example.
```sh
sudo apt install openjdk-17-jdk
```

> [!NOTE]
> If you only need the runtime to run the programs and not develop them run the following:
> ```sh
> sudo apt install openjdk-17-jre
> ```

3. Verify Installation
```sh
java -version
```

It should show something like this:
```sh
openjdk version "17.0.x" 2024-XX-XX
OpenJDK Runtime Environment (build 17.0.x+XX-Ubuntu-1)
OpenJDK 64-Bit Server VM (build 17.0.x+XX-Ubuntu-1, mixed mode)
```

4. Set **JAVA_HOME** for OpenJDK
Find the installation path:
```sh
sudo update-alternatives --list java
```

##### System-Wide
It'll be something like `/usr/lib/jvm/java-17-openjdk-amd64/bin/java`. Add it to `/etc/environment`.
```sh
sudo nano /etc/environment
```

Put the following in the file:
```sh
JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
```

##### User Only
```sh
nano ~/.bashrc # or .zshrc or whatever
```

Put the following in your profile file:
```sh
export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
```

Now verify if it set!
```sh
echo $JAVA_HOME
```

5. Update Path (Optional)
Run the following to add it to your path:
```sh
export PATH=$JAVA_HOME/bin:$PATH
```

Now consider looking at [security for java](#securing-java-in-your-system).


#### Azul Zulu JDK
Good for stability, performance, and lts for java applications.

1. We'll need to obtain Azul's GPG key and add it to our local repository.
```sh
sudo apt update
sudo apt install -y wget apt-transport-https
wget -qO - https://repos.azul.com/azul-repo.key | sudo apt-key add -
sudo apt-add-repository "deb https://repos.azul.com/zulu/deb stable main"
```

> [!IMPORTANT]  
> If you get the following:
> ```sh
> $ wget -qO - https://repos.azul.com/azul-repo.key | sudo apt-key add -
> Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
> OK
> ```
> You should probably use the updated method. Run the following in order:
> ```sh
> wget -qO /usr/share/keyrings/azul.asc https://repos.azul.com/azul-repo.key
> echo "deb [signed-by=/usr/share/keyrings/azul.asc] https://repos.azul.com/zulu/deb stable main" | sudo tee /etc/apt/sources.list.d/azul.list
> sudo apt update
> sudo apt install zulu17-jdk
> ```


2. Install Zulu JDK
Now install the version of Zulu you want. Refer to their [JDK versions](https://www.azul.com/downloads/?package=jdk#zulu).  
The following example will show for Zulu JDK 17.

```sh
sudo apt update
sudo apt install zulu17-jdk
```

3. Verify Zulu Installation:
```sh
java -version
```

It'll look like this:

```sh
$ java -version
openjdk version "17.0.x" 2024-XX-XX
OpenJDK Runtime Environment (Zulu 17.x.xx) (build 17.0.x+XX-LTS)
OpenJDK 64-Bit Server VM (Zulu 17.x.xx) (build 17.0.x+XX-LTS, mixed mode)
```

4. Set **JAVA_HOME** (Optional and recommended)
We need to find the installation path:
```sh
sudo update-alternatives --config java
```

It should show something like this:

```sh
$ sudo update-alternatives --config java
There is 1 choice for the alternative java (providing /usr/bin/java).

  Selection    Path                          Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/zulu17/bin/java   2175401   auto mode
  1            /usr/lib/jvm/zulu17/bin/java   2175401   manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

Add **JAVA_HOME** to the environment:
```sh
echo 'JAVA_HOME="/usr/lib/jvm/zulu17"' | sudo tee -a /etc/environment
```

Run the following to ensure it worked:
```sh
source /etc/environment
echo $JAVA_HOME
```

5. Update Path (Optional)
To make sure the Binaries are in your `PATH`, run the following:
```sh
export PATH=$JAVA_HOME/bin:$PATH
```
Add this to /etc/environment or your shell profile (`~/.bashrc` or `~/.zshrc` or whatever you use).

Now consider looking at [security for java](#securing-java-in-your-system).

### Securing Java in your System
All of the following is optional. It is recommened to do at least some of these.
These steps will utilize Azul Java JDK 17 from the [azul guide above](#azul-zulu-jdk).

1. Limit Execution to Authorized Applications/Users
Use permissions and file ownership to restrict who can execute Java. Ensure only specific applications or users that need Java can run it.
```sh
sudo chmod o-x /usr/lib/jvm/zulu17/bin/java
sudo chown root:root /usr/lib/jvm/zulu17/bin/java
```

2. Disable the Java Compilier (**javac**)
Remove execute permissions for javac:
```sh
sudo chmod o-x /usr/lib/jvm/zulu17/bin/javac
```

3. Secure Binaries using a **java** group
Create the new group:
```sh
sudo addgroup java
```

Change the group ownership of the java group:
```sh
sudo chgrp java /usr/lib/jvm/zulu17/bin/java
```

> [!NOTE]
> If you would like to set for all binaries, run the following:
> ```sh
> sudo chgrp java /usr/lib/jvm/zulu17/bin/*
> sudo chmod o-x /usr/lib/jvm/zulu17/bin/*
> ```


Remove execute permissions for others:
```sh
sudo chmod o-x /usr/lib/jvm/zulu17/bin/java
```

Verify permissions:
```sh
ls -l /usr/lib/jvm/zulu17/bin/
-rwxr-x--- 1 root java 12345 Dec  1 12:34 /usr/lib/jvm/zulu17/bin/java
```

Add your user to the **java** group:
```sh
sudo usermod -aG java <username>
```

> [!NOTE]
> Consider the following:
> * If you have other people on your server developing with java, they might need unrestricted access to tools like javac and javadoc. In this scenario, restrict only critical binaries (java, keytool, etc.).
> * Restrict all binaries except those explicitly required for the application you are running if you have a **production** server.
> * Lastly, some monitoring or management tools might need access to binaries like jps or jstat. Review application requirements before restricting these.

4. Use Docker
Run Java Applications in Isolated Environments
Use Docker or similar containerization tools:
* Create a Docker image with Java installed.
* Run the Java application in a container with restricted permissions.

5. Remove Unused Java Versions
List all of the Java versions you might have:
```sh
sudo update-alternatives --list java
```

Uninstall the ones you don't need anymore:
```sh
sudo apt remove <package_name>
```