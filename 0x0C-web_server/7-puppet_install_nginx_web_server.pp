# using puppet to install nginx

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/site-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/MthokozisiZwane permanent;',
}

file { '/var/www/html/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => package['nginx'],
}
