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
