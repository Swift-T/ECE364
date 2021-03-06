#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-27 11:18:50 -0500 (Wed, 27 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Lab02/printUsageStats.bash $
#$Revision: 87085 $
if (($# != 1))
then
    echo "Usage: sorting.bash <input file>"
    exit 1
fi

if [[ ! -e $1 ]]
then
    echo "Error: $1 doesn't exist."
    exit 2
fi
time=$(head -n 1 $1 | cut -d " " -f 3)
echo "Parsing file \"$1\". Timestamp: $time"
echo "Your choices are:"
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N highest mem usages"
echo "4) Top 3 longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"
echo
read -p "Please enter your choice: " choice
while (( $choice != 6 ))
do
if (( $choice == 1))
then
    echo "Total number of active user IDs: $(head -n 1 $1 | cut -d "," -f 3 | cut -d " " -f 2)"
fi
if (( $choice == 2))
then
    read -p "Enter a value for N: " num
    (( temp=num+7 ))
    cpu11=$(head -n $temp $1 | tail -n $num | cut -d " " -f 9)
    user=$(head -n $temp $1 | tail -n $num | cut -d " " -f 2)
    for (( i=1;i<=num;i++ ))
    do
	echo "User $(echo $user | cut -d " " -f $i) is utilizing CPU resoures at $(echo $cpu11 | cut -d " " -f $i)%"
    done
fi
if (( $choice == 3))
then
    read -p "Enter a value for N: " num
    user=$(tail -n +8 $1 | sort -k10,10 -r -t" " | head -n $num | cut -d " " -f 2)
    mem=$(tail -n +8 $1 | sort -k10,10 -r -t" " | head -n $num | cut -d " " -f 10)
    for (( i=1;i<=num;i++ ))
    do
	echo "User $(echo $user | cut -d " " -f $i) is utilizing mem resoures at $(echo $mem | cut -d " " -f $i)%"
    done	   
fi
if (( $choice == 4))
then
    pid=$(tail -n +8 $1 | sort -k11,11 -nr -t" " | head -n 3 | cut -d " " -f 1)
    com=$(tail -n +8 $1 | sort -k11,11 -nr -t" " | head -n 3 | cut -d " " -f 12)
    for (( i=1;i<=3;i++ ))
    do
	echo "PID: $(echo $pid | cut -d " " -f $i), cmd: $(echo $com | cut -d " " -f $i)"
    done
fi
if (( $choice ==5))
then
    read -p "Please enter a valid uqsername: " user
    cat $1 | grep $user > /dev/null
    if (( $? != 0 ))
    then
	echo "NO match found"
    fi
    com=$(cat $1 | grep $user | cut -d " " -f 12)
    cpus=$(cat $1 | grep $user | cut -d " " -f 9)
    num=$(echo $com | wc -w)
    for (( i=1;i<=num;i++ ))
    do
		echo "$(echo $cpus | cut -d " " -f $i) $(echo $com | cut -d " " -f $i)"
    done
fi
if (( $choice == 6))
then
    exit 0
fi
echo
read -p "Please enter your choice: " choice
done
exit 0
