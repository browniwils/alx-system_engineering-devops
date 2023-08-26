# The kill a process called 'killmenow'
# kill the process only if it exist
# If its not exists, puppet should exit
# with a 0 return code

exec {'kill `killmenow` process':
command => '/usr/bin/pkill -9 -f killmenow',
onlyif  => '/usr/bin/pgrep -f killmenow'
}

