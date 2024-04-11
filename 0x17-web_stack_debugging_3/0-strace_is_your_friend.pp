#!/usr/bin/env puppet
# fix internal error
exec { 'web stack debuging':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}
