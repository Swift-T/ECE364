#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-15 21:20:09 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Prelab01/svncheck.bash $
#$Revision: 85157 $
Iptr="file_list"
if [[ ! -r $Iptr ]]
then
    echo "Cannot read $Iptr"
    exit 0
fi
while read filename || [[ -n $filename ]]
do
    STAT=$(svn status $filename | head -c 1)
    if [[ "$STAT" = "?" && -e $filename ]]
    then
        if [[ ! -x $filename ]]
        then
            read -p "$filename better be execuatable before commit, press y to make it execuatable!" resp < /dev/tty
            if [[ "$resp" = "y" ]]
            then
                chmod +x $filename
            fi
        fi
        svn add $filename
    elif [[ "$STAT" = "" && ! -x $filename && -e $filename ]]
    then
        svn propset svn:executable ON $filename
    elif [[ "$STAT" = "" && ! -e $filename ]]
    then
        echo "Error: File $filename appears to not exist here or in svn."
    fi
done < $Iptr
svn commit -m "Auto committing code"
exit 0
