# Install Flask version 2.1.0 using pip3

package { 'python3-pip':
    ensure => 'installed'
}

exec { 'flask':
    command => '/usr/bin/pip3 install flask==2.1.0'
}

