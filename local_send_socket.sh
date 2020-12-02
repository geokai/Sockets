#!/bin/sh


port=$1
payload=$2





if [ ! -z $2 ] && [ -f $2 ]
then
    ncat --send-only localhost $1 < $2
else
    printf "Usage: ./send_socket.sh <fileToSend>\n\n"
fi
