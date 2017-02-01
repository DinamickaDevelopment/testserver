README
======


# 1. Server configuration

## 1.1. Updates

    apt-get update -y
    apt-get dist-upgrade -y
    reboot

## 1.2. Security


ssh config:

    nano etc/ssh/sshd_config
    Port 41033                   <-- change ssh port
    PasswordAuthentication no    <-- Only pubkey authentification 
    
    server ssh restart

And try to connect from another console (don't close the first console before all is working fine!)
    
    ssh -p 41033 serverip

Firewall:

    sudo ufw status
    sudo ufw delault allow outgoing
    sudo ufw default deny incoming
    sudo ufw limit 41033/tcp
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp 
    ...
    sudo ufw status numbered
    sudo delete [number]    <-- and delete the rules number related to 22/tcp ssh port 
    sudo ufw status verbose
    sudo delete [number ]
    sudo ufw enable

And try to connect from another console (don't close the first console before all is working fine!)


## 1.3. Tools

Automatic upgrades to not miss any security updates of openssh:

    nano /etc/apt/apt.conf.d/50unattended-upgrades     <-- and uncommment the auto-update you want
    dpkg-reconfigure -fnoninteractive unattended-upgrades  <-- bug: update doesnt applied...
    (dpkg-reconfigure -plow unattended-upgrades)



# 3.  Installing without docker


1.  Setting up SSL cert

    git clone https://git.atm4coin.com/root/ezletsencrypt.git

Follow the README.


2.  Installing (dev environment)

Install dependencies

    pip install -r requirements.txt



3. Initial Setup

Modify server/_env/env.json to match your database settings, email settings etc (dev server uses sqlite, postgres in prod)

Create an admin user

    cd petroweb/
    ./manage.py migrate
    ./manage.py createsuperuser

Copy staticfiles

    ./manage.py collectstatic --noinput

(optional) Load fixtures:

    ./manage.py loaddata _fixtures/*



4. Running

In production server should be run with guncicorn + nginx but for dev (autoreload) do:

    ./manage.py runserver

By default django will listen to localhost:8000

http://localhost:8000/admin


5. Running with Vagrant (TODO: Vagrantfile; skip to section 3)

    vagrant up

Open a second terminal to access the console of the VM.

    vagrant ssh