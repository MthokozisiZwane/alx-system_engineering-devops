# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "add_header X-Served-By $hostname;\n",
}

# Create symbolic link to enable the custom header configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-availabledefault',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}
