# Install Flask version 2.1.0 using pip3

Package { 'pip3':
  ensure => installed,
}

exec { 'pip3 install':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Package['pip3']
}
