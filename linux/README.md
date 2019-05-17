## Linux Cheat Sheet
> https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/

### this will show all user
> cat /etc/passwd

### add user, will create a user
> adduser jdocker

### add group, will create a group
> groupadd docker

### user to a 'sudo' group
> usermod -aG sudo jdocker

> usermod -aG docker jdocker

### list user of a group
> lid -g docker

### Delete the john account.
> userdel john
