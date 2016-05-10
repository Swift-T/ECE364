#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-23 22:27:43 -0500 (Sat, 23 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab02/process_temps.bash $
#$Revision: 86567 $
if (( $# != 1 ))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "$1 is not a readable file."
    exit 2
fi
line1=0
while read line
do
	if (( $line1==0 ))
	then
		(( line1=line1+1 ))
		continue
	fi
	avg=0
	(( num=$(echo $line | wc -w) ))
	for ((i=2; i<=num; i++))
	do
		(( avg=avg+$(echo $line | cut -d " " -f $i) ))
	done
	(( avg=avg/(num-1) ))
	echo "Average temperature for time $(echo $line | cut -d " " -f 1) was $avg C." 
done < $1
exit 0
