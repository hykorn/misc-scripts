#!/bin/bash
# diff $1 against $2 if filename are the same

source lsfile.sh

for i in `lsfile $1`
do
  for j in `lsfile $2`
  do
    S1="$i"
    S2="$j"
    echo $S1
#    if [ $S1=$S2 ]
#    then
#      echo "match $S1 == $S2"
#    fi
      
  done
done
