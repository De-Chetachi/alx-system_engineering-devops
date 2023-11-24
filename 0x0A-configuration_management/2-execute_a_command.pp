#a manifest that kills a process named killmenow.

exec { 'kill_':
  command => '/usr/bin/pkill killmenow'
}
