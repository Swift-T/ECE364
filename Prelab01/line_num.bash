#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-14 19:49:16 -0500 (Thu, 14 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab01/line_num.bash $
#$Revision: 85053 $
if (( $# != 1))
then
    echo "Usage: line_num.bash <filename>"
    exit 0
fi
if [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 0
fi
num=1
while read line || [[ -n "$line" ]]
do
    echo "$num:$line"
    (( num=num+1 ))
done < $1
exit 0
