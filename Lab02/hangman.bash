#! /bin/bash
#
#$Author: ee364f12 $
#$Date: 2016-01-27 11:54:36 -0500 (Wed, 27 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f12/Lab02/hangman.bash $
#$Revision: 87106 $
	arr[0]="banana"
	arr[1]="parsimonious"
	arr[2]="sesquipedalian"
	arr1[0]="......"
	arr1[1]="............"
	arr1[2]=".............."
	rand=$[ $RANDOM % 3 ]
	#echo ${arr[$rand]}
	chose=${arr[$rand]}
	chose1=${arr1[$rand]}
	echo "Your word is ${#arr[$rand]} letters long."
	length=${#arr[$rand]}
	while [ $chose != $chose1 ]
	do
		printf "Word is: "
		for ((i=0;i<length;i++))
		do
			printf "${chose1:$i:1}"
		done
		printf "\n"
		read -p " Make a guess: " resp
		match=0
		for ((i=0;i<length;i++))
		do
			if [ $resp = ${chose:$i:1} ]
			then
				(( tmp=$i+1 )) 
				chose1=$(echo $chose1 | sed s/./$resp/$tmp)
				match=1
			fi
		done
		if (( $match == 0 ))
		then
			echo " Sorry, try again."
		fi
	done
	echo "Congratulations! You have guessed the word: $chose"	
exit 0
