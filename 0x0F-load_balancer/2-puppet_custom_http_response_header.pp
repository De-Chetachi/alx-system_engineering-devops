#using puppet automate the task of creating a custom HTTP header response

package { 'nginx':
  ensure => installed,
}

exec { 'hostname':
  command => '/usr/bin/hostname',
  logoutput => true,
}

file_line { 'x-server-by':
  path   =>'/etc/nginx/sites-available/default',
  ensure => 'present',
  after  => "listen [::]:80 default_server ipv6only=on;",
  line   => 'X-Server-By $(hostname)',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
