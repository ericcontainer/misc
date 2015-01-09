#!/bin/bash
 
# References
# http://www.computerhope.com/unix/nc.htm#03
# https://github.com/daniloegea/netcat
# http://unix.stackexchange.com/questions/26715/how-can-i-communicate-with-a-unix-domain-socket-via-the-shell-on-debian-squeeze
# http://unix.stackexchange.com/questions/33924/write-inside-a-socket-open-by-another-process-in-linux/33982#33982
# http://www.linuxjournal.com/content/more-using-bashs-built-devtcp-file-tcpip
# http://www.dest-unreach.org/socat/
# http://stuff.mit.edu/afs/sipb/machine/penguin-lust/src/socat-1.7.1.2/EXAMPLES
# http://ubuntuforums.org/showthread.php?t=828870
 
# Socat version
echo -e "GET /images/json HTTP/1.1\r\n" | socat unix-connect:/var/run/docker.sock STDIO
 
# nc version (netcat-freebsd)
echo -e "GET /images/json HTTP/1.0\r\n" | nc -U /var/run/docker.sock
 
# bonus round: relay socket
socat -d -d TCP-L:8080,fork UNIX:/var/run/docker.sock
