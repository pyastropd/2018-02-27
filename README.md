
# Web interfaces for python applications
Davide Ricci

example in http://rodan/~indy/git/2018-02-27/ from oapd

Graphical User Interfaces are great. If you plan to build one for your python code, there are several options, some of which will be probably discussed in further meetings. 

But what about making your code usable online for everybody? For example:

 - Exposure time calculator;
 - Ephemerides;
 - ...;

Keep in mind that everyone already has the best container for that: the web browser. 
Moreover, modern web standards allow very responsive solutions:

I give a little introduction about HTML5 and javascript, with little skeleton examples that you can reuse.

## Install npm and node if you do not have it.

`npm` (node package manager) is the analogous of `pip`, but for javascript packages.
`node` is javascript for server side programming. We do not use it, but it is required by `npm`

### Method 1 (using curl, if you plan to use the latest node and npm version)

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

### Method 2 (repository, probably not the latest npm and node version)

```bash
apt-get -y install node npm
```
# Clone this repository

Clone this repository in a directory called "~/public_html" (use this folder name):

```bash
mkdir ~/public_html
cd ~/public_html
git clone https://github.com/pyastropd/2018-02-27.git
```

Enter in the `2018-02-27/2-medium` directory and then:

```bash
npm -f install 
```

to install all dependecy packages for these examples.

# Install Apache and PHP

`apache` is a web server. `php` is a server-side scripting language. 

```bash
apt-get -y install apache2
apt-get -y install php7.0 libapache2-mod-php7.0
```

Now your laptop is a web server!

Following lines will enable your local user web directory that will be visible at http://localhost/~your_username

```bash
a2enmod userdir
systemctl restart apache2
```
Look at http://localhost/~your_username using your favorite browser!








