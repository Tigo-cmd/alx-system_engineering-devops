# Ensure that the necessary directory exists
file { '/etc/httpd/conf.d':
  ensure => directory,
}

# Ensure that the necessary configuration file exists
file { '/etc/httpd/conf.d/custom_config.conf':
  ensure  => file,
  content => template('apache/custom_config.conf.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => File['/etc/httpd/conf.d'],
}

# Ensure that Apache service is running
service { 'httpd':
  ensure  => running,
  enable  => true,
  require => File['/etc/httpd/conf.d/custom_config.conf'],
}

# Alternatively, if the issue was a permission problem
file { '/var/www/html':
  ensure  => directory,
  owner   => 'apache',
  group   => 'apache',
  mode    => '0755',
  recurse => true,
  require => Package['httpd'],
}

# If SELinux is causing the issue (common in CentOS/RHEL)
exec { 'restorecon apache content':
  command => '/sbin/restorecon -Rv /var/www/html',
  onlyif  => 'getenforce | grep -iq enforcing',
  require => File['/var/www/html'],
}

