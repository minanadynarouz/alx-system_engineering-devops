# Install an especific version of flask (2.1.0)
# Using Puppt to install flask from pip3
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
