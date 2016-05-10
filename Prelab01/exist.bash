#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-13 17:05:42 -0500 (Wed, 13 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab01/exist.bash $
#$Revision: 84748 $
for filename in $@
do
    if [[ -r $filename ]]
    then
        echo "File $filename is readable!"
    elif [[ ! -e $filename ]]
    then
        touch $filename    
    fi
done
exit 0
