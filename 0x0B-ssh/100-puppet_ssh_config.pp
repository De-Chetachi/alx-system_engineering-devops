#a manifest that kills a process named killmenow.

exec { 'echo':
  command => '/usr/bin/echo "	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
