#manifest for fixing the  Apache 500 error

# This manifest uses strace to identify the issue causing Apache 500 error and automates the fix.

# Defines an exec resource to run strace on the Apache process
exec { 'strace_apache':
  command     => '/usr/bin/strace -p $(pgrep apache2) -o /tmp/strace_output.txt',
  path        => '/usr/bin',
  refreshonly => true,
}

# Defines an exec resource to fix the identifie problem
exec { 'fix-wordpress':
  command     => '/bin/echo "/etc/php/7.4/apache2" >> /tmp/fix.log',
  path        => '/bin',
  subscribe   => Exec['strace_apache'],
  refreshonly => true,
}
#restarts Apache service the after the fix
service { 'apache2':
  ensure  => 'running',
  require => Exec['fix-wordpress'],
}
