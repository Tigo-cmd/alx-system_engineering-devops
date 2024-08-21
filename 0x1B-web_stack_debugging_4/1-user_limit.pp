# Changes the OS configuration so that it is possible to login 
# with the holberton user and open a file without any error message.

exec { 'fix_user_limit'
    command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
    path => '/usr/local/bin/:/bin/'
}

# Increase file limit for holberton ser.
exec { 'increase_file':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}