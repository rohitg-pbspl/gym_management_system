# Siddartha Logistics Test Server Documentation

## Server Details
1. **Server Name or IP address:** 15.206.250.223
2. **User Name:** ubuntu
3. **Password:** SSH key attached .pem

## Server Creation Process
#### Open the Terminal and follow the commands.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b style="font-size:10">For Login to the Server</b>
1. ssh -i Promantia_testserver_01.pem ubuntu@15.206.250.223 

    #### Update and Upgrade Packages
1. sudo apt-get update -y
2. sudo apt-get upgrade -y
    #### Install Required Packages
1. sudo apt-get install -y libmysqlclient-dev
2. sudo apt-get install libffi-dev libssl-dev
3. sudo apt-get install -y build-essential
4. sudo apt-get install -y git
5. sudo apt-get install -y ruby-active-model-serializers
    #### Install Python : Python 3.10
1.  sudo apt install software-properties-common -y
2.  sudo add-apt-repository ppa:deadsnakes/ppa
3.  sudo apt install python3.10 python3.10-dev python3.10-distutils
    #### Install Python Virtual Environment
1.  sudo apt-get install python3.10-venv
    #### Install Software Properties Common
1.  sudo apt-get install software-properties-common
    #### Install Redis Server
1.  sudo apt-get install redis-server
    #### Install other packages
1.  sudo apt-get install xvfb libfontconfig wkhtmltopdf
2.  sudo apt-get install libmysqlclient-dev
    #### Install MariaDB
1.  sudo apt-get install apt-transport-https curl
2.  sudo curl -o /etc/apt/trusted.gpg.d/mariadb_release_signing_key.asc 'https://mariadb.org/mariadb_release_signing_key.asc'
3.  sudo sh -c "echo 'deb https://mirrors.aliyun.com/mariadb/repo/10.3/ubuntu bionic main' >>/etc/apt/sources.list"
4.  sudo apt-get update
5.  sudo apt-get install mariadb-server-10.3 (or)<br> sudo apt-get install mariadbserver-10.6 (for 21+ Ubuntu versions)<br>
<br>
**Note:** No Passwords will be asked to enter for 10.6+ version. Later we have to reset
it again.<br>
After mariadb installed, edit file my.cnf at /etc/mysql/my.cnf by using the following
cmd.<br>
<br>
23. sudo nano /etc/mysql/my.cnf <br>
<b>Paste below things in the my.cnf configuration file :</b><br>
    
    [mysqld] <br>
    innodb-file-format=barracuda <br>
    innodb-file-per-table=1<br>
    innodb-large-prefix=1<br>
    character-set-client-handshake = FALSE<br>
    character-set-server = utf8mb4<br>
    collation-server = utf8mb4_unicode_ci<br>
    <br>
--Press ctrl+o<br>
--Press Enter<br>
--Press ctrl+x<br>
    #### Restart the MariaDB service<br>
1.  sudo service mysql restart
    #### Install Curl
2.  sudo apt install curl<br>
    #### Install Node
3.  curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
4.  source ~/.profile
5.  nvm install 16.15.0
    #### Install NPM
6.  sudo apt-get install npm
    #### Install Yarn
7.  sudo npm install -g yarn<br>
or<br>
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list<br>
sudo apt-get update sudo apt-get install yarn -y
    #### Install Frappe
1. git clone https://github.com/frappe/bench bench-repo
2. sudo apt install python-pip
3. sudo apt install python3-pip
4. pip3 install -e bench-repo
5. source .profile
6. source .bashrc
    #### Initialize Frappe Bench
7. bench init frappe-bench --frappe-branch version-14 <br>
   <br>
<u>To check that frappe-bench folder is created or not but not having access permission</u>
1. ls 
2.  sudo chmod 777 -R {mention path of frappe-bench folder}/frappe-bench/<br>
Example: sudo chmod 777 -R /home/username/frappe-bench/<br>
Switch directories into the Frappe Bench directory

3. cd frappe-bench<br>
<u>Run these commands if you get any kind of python related error.</u><br>
mv env env-old<br>
virtualenv –python python3.10 env<br>
env/bin/pip install -U pip<br>
env/bin/pip install -e apps/frappe<br>

    #### To check the bench version
1. bench version<br>
   
    #### Reset the MYSQL password.

2. sudo mysql_secure_installation
3. sudo mysql -u root -p <br>
Enter the New password for MySQL mariadb.<br>
<b>Note:</b> MySQL password is needed in future, so please note down the password.<br>
    #### Create a New Site
1. bench new-site [site-name] (For Eg. bench new-site siddartha_logistics)<br>
While creating the site, enter the newly created MySQL password.<br>
    #### Install apps
1. bench get-app [App git-hub path]<br>
<b>Example:</b> bench get-app https://github.com/promantia-ltd/siddartha_logistics_erpnext_app.git<br>
bench --site [site-name] install-app [app-name]<br>
<b>Example:</b> bench --site siddartha_logistics install-app siddartha_logistics_erpnext_app<br>
    #### Starting the bench<br>
2. bench use [site-name]<br>
bench setup requirements<br>
bench build<br>
bench start<br>
bench --site [site-name] migrate<br>

Press Ctrl+C to stop the bench.
