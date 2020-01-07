#!/bin/sh

if [ ! -z $1 ] && [ -f $1 ]
then
    ncat --send-only localhost 5001 < $1
else
    printf "Usage: ./send_socket.sh <fileToSend>\n\n"
fi
