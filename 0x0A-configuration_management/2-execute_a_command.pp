# Puppet manifest to execute a command to kill a process

# Defines the exec resource to kill the 'killmenow' process
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  returns => [0, 1], # Allows exit codes 0 and 1
}

