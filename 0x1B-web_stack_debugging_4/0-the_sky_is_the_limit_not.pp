# Fix worker_connections in Nginx
exec { 'fix-worker-connections':
  command => 'sed -i "s/worker_connections.*/worker_connections 1024;/g" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
}

# extendss request limit to nginx
exec { 'fix-request-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  require => [Exec['fix-worker-connections'], Exec['fix-request-limit']],  # Ensure fix commands run first
}
