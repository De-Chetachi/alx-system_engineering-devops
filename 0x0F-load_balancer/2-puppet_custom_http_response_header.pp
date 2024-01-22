#using puppet automate the task of creating a custom HTTP header response

package { 'nginx':
  ensure => 'installed',
}

file_line { 'x-served-by':
  path   =>'/etc/nginx/sites-available/default',
  ensure => 'present',
  after  => "server_name _;",
  line   => '\tadd header X-Served-By $(hostname);',
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
