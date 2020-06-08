# Disaster recovery procedures for various scenarios

### You forget your bitlbee password
NOTE: all steps require root access (sudo su -)

1. first line of your xml file in /var/lib/bitlbee contains an item for password hash
2. 'bitlbee -x hash newpassword' to hash a new one,
3. replacing it will invalidate all other account passwords (didn't really for me, but keep an eye out for)
