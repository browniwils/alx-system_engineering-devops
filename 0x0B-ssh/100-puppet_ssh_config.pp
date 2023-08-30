# config ssh client with puppet

file { '/etc/ssh/ssh_config':
	ensure => present,
	content =>
		"${file('/etc/ssh/ssh_config')}Host 225917-web-01
			HostName 34.203.33.204
			ServerAliveInterval 120
			IdentityFile ~/.ssh/school
			PasswordAuthentication no",
	owner	=> 'browniwils'
	group	=> 'browniwils'
	mode	=> '0744'

