# Manifest to install flask from pip3

Exec { 'pip3 install flask':
  require => ['python-installed']
  command => '/usr/bin/pip3 install flask==2.1.0' 
}

Exec { 'python-installed':
  command => '/usr/bin/which python3' 
}
