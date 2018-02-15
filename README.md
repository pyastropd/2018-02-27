
# Web interfaces for python applications
Davide Ricci

## Install node and npm if you need it.

### Method 1 (curl, if you plan to use the latest node and npm version)

From:
http://yoember.com/nodejs/the-best-way-to-install-node-js/

(see also https://github.com/creationix/nvm)

On Linux (other OS are treated in previous links):

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash

nvm list
nvm ls-remote
nvm install 7.10.0
nvm use 7.10.0
nvm alias default 7.10.0
node -v
npm install -g npm
npm -v
```

On Mac, add the following line in `.bash_profile`:
        
```bash
source ~/.nvm/nvm.sh
```
### Method 2 (repository, probably not the node and nvm latest version)

```bash
apt-get -y install node npm
```

# Install Apache and PHP

```bash
apt-get -y install apache2
apt-get -y install php7.0 libapache2-mod-php7.0

a2enmod userdir
systemctl restart apache2
```

# Clone this repository

Clone this repository:

```bash
mkdir ~/public_html
cd ~/public_html
git clone https://github.com/pyastropd/2018-02-27.git
```

Enter in the `2018-02-27/2-medium` directory and then:

```bash
npm -f install 
```

Navigate with your favorite browser in http://localhost:~/your_username/


