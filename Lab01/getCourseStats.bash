#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-20 11:18:42 -0500 (Wed, 20 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Lab01/getCourseStats.bash $
#$Revision: 86343 $
if (( $# != 1 ))
then
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1
fi
if [[ $1 != "ece364" && $1 != "ece337" && $1 != "ece468" ]]
then
    echo "Error: course $1 is not a valid option"
    exit 5
fi
num=$( echo $( ls gradebooks/$1_section*.txt | wc -w ) )
count=1
stnum=0
tot=0
max=0
avg=0
while (( $count <= $num ))
do
    ./getFinalScores.bash gradebooks/$1_section$count.txt
#./getFinalScores.bash gradebooks/$1_section1.txt
    if (( $? != 0 ))
    then 
        echo "Error while running getFinalScores.bash"
        exit 3
    fi
    while read line || [[ -n $line ]]
    do
        (( stnum=stnum+1 ))
        g=$( echo $line | cut -d "," -f 2)
        (( tot=tot+g ))
        if (( g > max ))
        then
            max=$g;
            name=$( echo $line | cut -d "," -f 1)
        fi
    done < ./gradebooks/$1_section$count.out
    (( count=count+1 ))
done
(( avg=tot/stnum ))
echo "Total students: $stnum"
echo "Average score: $avg"
echo "$name had the highest score of $max"
echo
exit 0
