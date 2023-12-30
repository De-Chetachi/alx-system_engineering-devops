#using puppet automate the task of creating a custom HTTP header response

package { 'nginx':
  ensure => installed,
}

file_line { 'red':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/var/www/html/custom_404.html':
  content => 'Ceci n'est pas une page',
}

exec { 'hostname':
  command => '/usr/bin/hostname',
  logoutput => true,
}

file_line { 'x-server-by':
  path =>'/etc/nginx/sites-available/default',
  ensure => present,
  after => "listen [::]:80 default_server ipv6only=on;",
  line => 'X-Server-By $(hostname)'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
