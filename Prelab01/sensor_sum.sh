#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-14 20:22:07 -0500 (Thu, 14 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab01/sensor_sum.sh $
#$Revision: 85062 $
if (( $# != 1))
then
    echo "Usage: sensor_num.sh <filename>"
    exit 0
fi
if [[ ! -r $1 ]]
then
    echo "error: $1 is not a readable file!"
    exit 0
fi
while read line || [[ -n "$line" ]]
do
    line=$( echo $line | tr -s ' ' )
    printf "$( echo $line | head -c2 ) $(( $( echo $line | cut -d' ' -f2 )+$(echo $line | cut -d' ' -f3 )+$( echo $line | cut -d' ' -f4 ) ))\n"
done < $1
exit 0
