#! /bin/bash
if (($# != 1))
then
    echo "Usage: scheduler.bash <input file>"
    exit 1
fi

if [[ ! -e $1 | ! -r $1]]
then
    echo "Error: $1 doesn't exist."
    exit 2
fi

if [[ -e "schedule.out"]]
then
	echo "schedule.out already exist"
	exit 3
fi
echo "	07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00" > schedule.out
while read line || [[ -n $line ]]
do
	
done < $1

echo "The maximum number of people are available at " 
exit 0
