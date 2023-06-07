# How to use KEDEMatcher

This document shows how to use only the most used commands.
Detailed information can be found [here](https://docs.kedehub.io/kedehub/kedehub-merge-identities.html)

## Provision a new company

### Configuration directory

KEDEMatcher uses [Confuse](https://confuse.readthedocs.io/en/latest/index.html) for managing its configuration.
In our case the application name is KedeGit.
Both KEDEMatcher and KedeGit share the same configuration files.
The configuration paths for different platforms are listed [here](https://confuse.readthedocs.io/en/latest/usage.html#search-paths). 
Users can also add an override configuration directory with an environment variable. 
The environment variable name for KEDEGit is KEDEGITDIR.

This guide shows how to use KEDEMatcher on Amazon EC2 

For EC2 the configuration directory is: 
```commandline
/home/ec2-user/.config/KedeGit
```
You need to create it before proceeding further.

````commandline
mkdir ~/.config/KedeGit
````

### Configure KEDEMatcher

#### Allowed and excluded file types
```commandline
cp docs/kede-config.json /home/ec2-user/.config/KedeGit

nano /home/ec2-user/.config/KedeGit/kede-config.json
```
Change the file if needed to match your architecture, technology and preferences.

#### Set configuration file 
```commandline

cp docs/empty_config.yaml /home/ec2-user/.config/KedeGit/config.yaml
```
Open <em>config.yaml</em> and add values for company name, user and token from your invitation email.
```commandline
nano /home/ec2-user/.config/KedeGit/config.yaml
```
```commandline
server:
    protocol: https
    host: api.kedehub.io
    port: 443

company:
    name:
    user:
    token:
```

### Instal virtualenv
```commandline
pip install virtualenv
```

### Install KEDEMatcher in virtual environment
```commandline
git clone https://github.com/kedehub/kedematcher.git

cd kedematcher

python3 -m venv env

source ~/kedematcher/env/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

pip3 install names-matcher

pip3 install numpy --upgrade

deactivate
```

```