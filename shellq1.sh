#!/bin/bash
FILE=$1
if [ -e $FILE ]; then #To check if the file  exists or not use -f if it is a regular file
    if [ -s $FILE ]; then  #To check if the file is empty.
        echo "0"   #The file exists and is not empty
    else
        echo "1"   #The file exists and is empty
    fi
else
    echo "2" #If the file doesn't exist
fi