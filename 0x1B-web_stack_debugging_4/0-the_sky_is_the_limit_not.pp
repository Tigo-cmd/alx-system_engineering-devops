# fix nginx request limit

exec  { 'fix--for-nginx':
    command => 'sudo sed -i "s/15/10000/g" /etc/default/nginx && sudo service nginx restart',
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
    provider => 'shell',
}

# Reload nginx additional functionality uncomment to render active

# -> exec { 'nginx-Reload':
#  command => 'nginx restart',
#  path    => '/etc/init.d/'
#}
