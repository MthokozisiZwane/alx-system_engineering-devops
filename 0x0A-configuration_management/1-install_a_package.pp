# Puppet manifest to install Flask package

# Defines the package resource for python3-pip
package { 'python3-pip':
  ensure => installed,
}

# Defines the package resource for Flask with version constraint
package { 'Flask':
  ensure   => '2.1.0',        # Ensures that Flask is installed with version 2.1.0
  provider => 'pip3',         # Uses pip3 as the package provider
  require  => Package['python3-pip'], # Require python3-pip to be installed first
  before   => Exec['install_flask_fix'], # Ensures the fix command runs after Flask is installed
}

# Defines an exec resource to fix Flask's dependencies
exec { 'install_flask_fix':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path    => '/usr/bin',
  require => Package['Flask'],
  onlyif  => '/usr/local/bin/flask --version 2>&1 | grep -q "ImportError"',
}

