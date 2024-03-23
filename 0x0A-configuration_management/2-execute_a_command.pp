#Kills a process

exec { 'killmenow':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill killmenow',
}

