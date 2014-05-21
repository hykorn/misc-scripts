#!/bin/bash

#MYBASENAME=$(basename "$i")

function lsfile()
{
  cd $1
  for i in *.*
  do
    echo $(basename "$i") 
  done
}

#lsfile $1
