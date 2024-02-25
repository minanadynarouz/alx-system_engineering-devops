# configure a config file in .ssh to deny password and get key from ~/.ssh/school

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>
    "${file('/etc/ssh/ssh_config')}Host 198250-web-01
        HostName 54.237.83.201
        IdentityFile ~/.ssh/school
        PasswordAuthentication no",
  mode    => '0744'
}
