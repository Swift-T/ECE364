#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-20 11:15:28 -0500 (Wed, 20 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Lab01/getFinalScores.bash $
#$Revision: 86337 $
if (( $# != 1 ))
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
fi
if [[ ! -e $1 ]]
then
    echo "Error reading input file: $1"
    exit 2
fi
filename=$( echo $1 | cut -d "." -f 1)
filename=$( echo "./"$filename".out" )
if [[ -e $filename ]]
then
    echo "Output file $filename already exists."
    exit 3
fi
touch $filename
while read line || [[ -n $line ]]
do
    name=$( echo $line | cut -d "," -f 1)
    ass=$( echo $line | cut -d "," -f 2)
    mid1=$( echo $line | cut -d "," -f 3)
    mid2=$( echo $line | cut -d "," -f 4)
    pro=$( echo $line | cut -d "," -f 5)
    (( final=(15*$ass)/100+(30*$mid1)/100+(30*$mid2)/100+(25*$pro)/100 ))
    echo $name","$final >> $filename
done < $1
exit 0
