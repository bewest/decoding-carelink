#!/bin/bash

echo ""
SOCAT=$(which socat)
# BLOCK_SIZE="-b 64"
BLOCK_SIZE=""
ADDR1="TCP-CONNECT:bewest.io:8080,reuseaddr"
ADDR2="pty,link=./carelink.ttyUSB0,b9600,raw"
# ADDR2="FILE:carelink.ttyUSB0,b9600,raw"
# $ socat pty,link=$HOME/dev/vmodem0,waitslave tcp:modem-server:54321
SOCAT_ARGS="${BLOCK_SIZE} ${ADDR1} ${ADDR2}"

# from http://www.rfc1149.net/blog/2011/12/01/accessing-serial-ports-the-easy-way/
# I launch socat as
# % socat TCP-LISTEN:4161,fork,reuseaddr FILE:/dev/ttyUSB0,b57600,raw and what
# I immediately get is a TCP server listening onto port 4161 and ready to relay
# any incoming connection to the /dev/ttyUSB0 serial port with a 57600 baud
# rate. And not only do I have no more concern about accessing the serial port
# properly, but also I can access a port located on a remote computer as easily
# by launching socat there instead of locally.



echo "$SOCAT $SOCAT_ARGS"
$SOCAT $SOCAT_ARGS

#####
# EOF
