# simplyriley

Personal Site
<br><br>
# Building our Development Environment
This guide will assume that this dev enviornment is being ran on Ubuntu. It is possible to create a virtualbox VM that can run this project on Windows/Mac, but the following commands are specifically targeted to Ubuntu users.
<br><br>

## 1: Create a new folder to hold our musicbudd project, preferably at ~/workspace/musicbudd
```
mkdir ~/workspace/musicbudd
```
<br>

## 2. Install git
```
sudo apt update
sudo apt install git
```
- Once Git has been installed, we'll need to set a username & email to attach to any commits
```
git config --global user.name "<first_name> <last_name>"

git config --global user.email "<email_addresss>"
```
<br>

## 3. Generate a local ssh-key on your machine so that you can push/pull to/from Github
```
sudo apt install -y openssh-client.git
mkdir -p ~/.ssh/github
chmod 700 ~/.ssh ~/.ssh/github
ssh-keygen -t rsa -b 4096 -C 'your@email.com' -f ~/.ssh/github/id_rsa -q -N ''
cat ~/.ssh/github/id_rsa.pub
```
<br>

## 4. Add the new ssh key to your Github account
- In Github, click on your profile in the top-right corner and go to settings
- Then go to "SSH and GPG keys"
- Click "New SSH key" button
- Take the output from the ```cat ~/.ssh/github/id_rsa.pub``` command and paste it into Github, give it a name, and hit "Add SSH key".
<br><br>

## 5. Add some finishing touches to your ssh key on your local machine
```
touch ~/.ssh/config
chmod 600 ~/.ssh/config
```
- Open ```~/.ssh/config``` with your editor of choice, and add the following
```
Host github.com
    IdentityFile ~/.ssh/github/id_rsa
```
- Now in your terminal run ```ssh -T git@github.com```, you should get a message saying that you can establish a connection successfully.
<br><br>

## 6. Clone the project from the repository
- From the Github repository page (this one), click the green "Code" button and copy the SSH URL, and run the below command from inside the ```~/workspace/musicbudd``` directory.
```
git clone <ssh_url>
```
<br>

## 7. Download VSCode
- The authors would recommend turning on settingsSync inside VSCode, so that your personalization settings & extensions are shared between workstations.
- Here are some extensions that the authors have found useful while working on this project.
```
- Python by microsoft
        - Bookmarks by Alessandro Fragnani
        - Bracket Pair Colorizer by Coenraads
        - Docker by Microsoft
        - Git Blame by Wade Anderson
        - GitLens by GitKraken
        - GitHub by knisterpeter
        - HTML CSS Support by Ecmel
        - Markdown All in One by Yu Zhang
        - TODO Highlight by Wayou Liu
        - Visual Studio IntelliCode by Microsoft
        - vscode-icons by vscode icons team
        - vscode-proto3 by zxh404
        - YAML by Redhat
        - Intellisense for CSS class names by Zignd
        - HTML Preview by Thomas Haakon Townsend
        - ES7 React/Redux/Graphql support by dsznajder
```
<br>

## 8. Download & Install VirtualBox for hosting VMs @ ```https://www.virtualbox.org/wiki/Downloads```
- If you get a "kernel modules must be signed" error when attempting to open Virtualbox, refer to this StackOverflow solution @ ```https://stackoverflow.com/questions/61248315/sign-virtual-box-modules-vboxdrv-vboxnetflt-vboxnetadp-vboxpci-centos-8```
<br><br>

## 9. Download & Install Vagrant for managing VirtualBox VMs @ ```https://www.vagrantup.com/downloads```
- Now from inside our ```~/workspace/musicbudd``` directory, if there is no Vagrantfile
```
vagrant init ubuntu/xenial64
vagrant box add ubuntu/xenial64
vagrant up
```
- If the Vagrantfile already exists (it should), just run
```
vagrant up
```
- If this works successfully, you can open up VirtualBox and you should see a new & running VM.
<br><br>

## 10.  SSH into the VM via Vagrant with ```vagrant ssh``` from the ```~/workspace/musicbudd``` directory, and then ```cd /vagrant``` into the shared volume.
- the ```/vagrant``` folder is a shared volume between the VM and the host machine, so from it we can access our Github project. All work in the VM should be done from the ```/vagrant``` directory.
- When you first ssh into the vagrantbox, you'll probably see a message prompting you to upgrade to the newest release with command ```do-release-upgrade```, it's probably worth doing this until you're on the latest Ubuntu LTS release.
<br><br>

## 11.  From inside the VM, Download & Install Docker
```
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```
- Ensure that Docker was installed properly with the ```docker -v``` command
<br><br>

## 12. Download & Install docker-compose
- docker-compose is a useful tool for building/running multiple docker containers at once, and networking between them.
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
- Test that docker-compose installed correctly with the ```docker-compose -v``` command
<br><br>

## 13. Install PyEnv
- PyEnv is a useful tool for managing multiple Python versions & installations without interfering with the system default (which Ubuntu does not like you messing with)
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash
```
- Update your ```~/.bashrc``` file with the following lines
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH=~/.pyenv/shims:$PATH
```
- Restart your terminal instance w/ the new path variables using the ```source ~/.bashrc``` command
- Using pyenv, download the latest python version and set it to be used globally
```
pyenv install --list | grep " 3\.[678]"
pyenv install -v <version_name>
pyenv global <version_name>
```
- Validate that the correct python <version_name> is being used via the ```python --version``` command
<br><br>

## 14. Download & Install Python pip
- pip is a Python package manager, for download 3rd party libraries and frameworks
```
sudo apt install python3-pip
python -m pip install --upgrade pip
```
- Validate that pip was installed correctly with ```pip --version```
<br><br>

## 15. Download & Install Django
- Django is a robust web framework written in Python. We will be using it to manage our web server.
```
python -m pip install Django

sudo apt-get install python-django
```
- Validate that Django was installed correctly with ```python -m django --version```
<br><br>

## 16. Download & Install Node.js
- Node.js powers the React view framework, which is required for this project to build/run.
- npm is a Node.js package manager for downloading and installing various libraries/frameworks such as React
```
sudo apt install nodejs
sudo apt install npm
```
- Validate that these two installed correctly with ```node -v``` & ```npm -v```
- Ensure that Node.js is as up-to-date as possible
```
npm cache clean -f

npm install -g n

sudo n stable
```
- Next download & install npx, a tool for executing Node.js packages
```
sudo npm i -g npx
```
<br><br>

## 17. Start the development server
```
python manage.py runserver 0.0.0.0:8000
```
- We've already set up the port-forwarding for the VM inside the Vagrantfile, so this command should make the server visible on your local machine @ http://0.0.0.0:8000/