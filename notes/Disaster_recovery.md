# Disaster recovery procedures for various scenarios

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## You forget your bitlbee password

=======
### You forget your bitlbee password
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
### You forget your bitlbee password
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
### You forget your bitlbee password
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
NOTE: all steps require root access (sudo su -)

1. first line of your xml file in /var/lib/bitlbee contains an item for password hash
2. 'bitlbee -x hash newpassword' to hash a new one,
3. replacing it will invalidate all other account passwords (didn't really for me, but keep an eye out for)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

## all of the changes i've made to my 20.04 VM

created /etc/apt/apt.conf.d/99massivechungus
wrote apt::Install-Suggests "true";

added
Defaults        pwfeedback
to /etc/sudoers
adds the fancy dots to passwords

installed tmux: tmux

added
tmux new-session -A -s Sage
to .bashrc
to enable automatic connection to tmux on login

install Weechat: weechat

wee-slack: <https://github.com/wee-slack/wee-slack>

mkdir -p ~/.weechat/python/autoload
cd ~/.weechat/python
curl -O https://raw.githubusercontent.com/wee-slack/wee-slack/master/wee_slack.py
ln -s ../wee_slack.py autoload

sudo apt install weechat-python python3-websocket

OPTIONAL: Install MySQL: mysql-server

sudo apt-get install mysql-server
sudo mysql_secure_installation
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
=======
>>>>>>> 9efeefb094b6ffe518cf8af3e532bc5b4a505d51
