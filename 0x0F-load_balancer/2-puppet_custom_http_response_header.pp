# web_configuration.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# The index page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Performing a redirection
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/MthokozisiZwane permanent;",
}

# Creating a custom error page
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

# Custom HTTP response header
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "add_header X-Served-By $hostname;",
}

# Test Nginx configuration
exec { 'nginx_config_test':
  command => 'nginx -t',
  require => File['/etc/nginx/sites-enabled/default'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['nginx_config_test'],
}
