#!/usr/bin/env bash
#using pappet to male changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,
content =>"
	#ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
