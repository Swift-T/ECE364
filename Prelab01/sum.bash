#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-15 21:30:20 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab01/sum.bash $
#$Revision: 85162 $
sum=0
for num in $@
do
    let sum=$sum+$num 
done
echo $sum
exit 0
