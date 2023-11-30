#!/usr/bin/env bash
# using puppet to make changes to configuration file

file { 'ect/ssh/ssh_config':
	ensure => present,
content =>"
	
	#ssh client confuguration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	"
}
