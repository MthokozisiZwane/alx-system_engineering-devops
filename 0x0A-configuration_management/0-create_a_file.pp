# Puppet manifest to create a file in /tmp

# Defines the file resource
file { '/tmp/school':
  ensure  => file,       # Ensures that it is a file
  mode    => '0744',     # Sets file permissions to 0744
  owner   => 'www-data', # Sets the file owner to www-data
  group   => 'www-data', # Sets the file group to www-data
  content => 'I love Puppet', # Sest the content of the file
}

