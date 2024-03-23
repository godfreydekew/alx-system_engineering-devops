#Kills a process

exec { 'killmenow':
  path    => '#!/bin/bash',
  command => 'pkill -f killmenow',
}

