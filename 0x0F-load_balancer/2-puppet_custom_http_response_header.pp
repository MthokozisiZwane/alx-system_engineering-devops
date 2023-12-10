# 2-puppet_custom_http_response_header.pp

# Installing Nginx package if not already installed
package { 'nginx':
  ensure => installed,
}

# Defining the custom HTTP header configuration
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "add_header X-Served-By $hostname;\n",
}

# Creates symbolic link to enable the custom header configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
}

# Restarting Nginx to apply changes
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
