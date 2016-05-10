#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-23 22:27:43 -0500 (Sat, 23 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab02/yards.bash $
#$Revision: 86567 $
if (( $# != 1 ))
then
    echo "Usage: yards.bash <filename>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error $1 is not readable"
    exit 2
fi
maxavg=0
while read line
do
	total=0
	var=0
	(( num=$(echo $line | wc -w) ))
	
	for ((i=2; i<=num; i++))
	do
		(( total=total+$(echo $line | cut -d" " -f $i) ))
	done
	(( avg=total/(num-1) ))
	for ((i=2; i<=num; i++))
	do
		(( var=var+($(echo $line | cut -d" " -f $i)-avg)*($(echo $line | cut -d" " -f $i)-avg) ))
	done
	(( var=var/(num-1) ))
	if (( avg>maxavg ))
	then
		maxavg=$avg	
	fi
	echo "$(echo $line | cut -d" " -f 1) schools averaged $avg yards receiving with a variance of $var" 
done < $1
echo "The largest average yardage was $maxavg"
exit 0
