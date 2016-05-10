#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-23 22:27:43 -0500 (Sat, 23 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab02/run.bash $
#$Revision: 86567 $
if (( $# != 2 ))
then
    echo "Usage: run.bash <filenameSourceCode> <filenameOutput>"
    exit 1
fi
source=$(echo $1 | cut -d "." -f 1 )
rm -f $source
gcc $1 -o $source
if (( $?!=0 ))
then
	echo "error: $1 could not be compiled!"
	exit 1
fi
if [[ -e $2 ]]
then
    printf "$2 exists. Would you like to delete it? "
    read resp
    if [[ $resp = "n" ]]
    then
	printf "Enter a new filename: "
	read filename
	set -- "${@:1:1}" "$filename" "${@:2}"
    else
	rm $2
    fi
fi
for (( c=1;c<=32;c=c*2 ))
do
	for (( w=1;w<=16;w=w*2 ))
	do
		string=$($source $c $w a)
		pname=$(echo $string | cut -d ":" -f 2)
		cpi=$(echo $string | cut -d ":" -f 8)
		extime=$(echo $string | cut -d ":" -f 10)
		echo "$pname:$c:$w:$cpi:$extime" >> $2
		string=$($source $c $w i)	
		pname=$(echo $string | cut -d ":" -f 2)
		cpi=$(echo $string | cut -d ":" -f 8)
		extime=$(echo $string | cut -d ":" -f 10)
		echo "$pname:$c:$w:$cpi:$extime" >> $2
	done
done
exit 0
