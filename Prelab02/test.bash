#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
while read line
do
    echo $line
done <  "${1:-/dev/stdin}"
exit 0
