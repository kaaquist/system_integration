#!/bin/bash
FILES=`pwd`"/img/diagrams/*/*"

for f in $FILES
do
  if [ ${f: -3} != ".sh" ]
  filename="${f##*/}"
  basename=${filename%.*}
  #echo $filename
  then
		#echo "Processing $f file..."
  		# take action on each file. $f store current file name
  		echo "------------------------- FILE: " $filename
  		echo "------------------------- FOUND: "
  		echo "- : `ack /$basename ./tex/ -c -l`"
  fi
done