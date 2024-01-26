#extends request limit to nginx
exec { 'fix--for-nginx':
  command => 'sed -i "s/2000/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restarts Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix--for-nginx'],  # Ensures fix--for-nginx runs first
}
