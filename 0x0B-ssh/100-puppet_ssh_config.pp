# 100-puppet_ssh_config.pp

# Ensuring the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => present,
}

# Set up the SSH client configuration
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
}

