#!/bin/bash
# http://www.dest-unreach.org/socat/doc/socat-ttyovertcp.txt
# EXAMPLE FOR REMOTE TTY (TTY OVER TCP) USING SOCAT
# 
# You have a host with some serial device like a modem or a bluetooth interface
# (modem server)
# You want to make use of this device on a different host. (client)
# 
# 1) on the modem server start a process that accepts network connections and
# links them with the serial device /dev/tty0:
# 
# $ socat tcp-l:54321,reuseaddr,fork file:/dev/tty0,nonblock,waitlock=/var/run/tty0.lock
# 
# 2) on the client start a process that creates a pseudo tty and links it with a
# tcp connection to the modem server:
# 
# $ socat pty,link=$HOME/dev/vmodem0,waitslave tcp:modem-server:54321
#  socat  FILE:/dev/ttyUSB0,nonblock,b9600,raw tcp:localhost:4161 

# 
echo ""
SOCAT=$(which socat)
# BLOCK_SIZE="-b 64"
BLOCK_SIZE=""
ADDR1="tcp-l:8080,reuseaddr,fork"
ADDR2="FILE:/dev/ttyUSB0,nonblock,b9600,raw"
# ADDR2="FILE:carelink.ttyUSB0,b9600,raw"
# $ socat pty,link=$HOME/dev/vmodem0,waitslave tcp:modem-server:54321
SOCAT_ARGS="-d -d ${BLOCK_SIZE} ${ADDR1} ${ADDR2}"

echo "$SOCAT $SOCAT_ARGS"
$SOCAT $SOCAT_ARGS &
sleep 2
ssh -f -N -R 0.0.0.0:8080:0.0.0.0:8080 bewest@bewest.io

#####
# EOF
