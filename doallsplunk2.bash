#!/bin/bash

# Check 3 arguments are given #
if [ $# -lt 3 ]
then
    echo "Usage : $0 option pattern [virtual or physical or splunk]"
    exit
fi

# Check the given file is exist #
#if [ ! -f $3 ]
#then
#        echo "Filename given \"$3\" doesn't exist"
#        exit
#fi

if [ $3 = virtual ]
then
    echo "Virtual servers"
elif [ $3 = physical ]
then
    echo "Physical servers"
elif [ $3 = splunk ]
then
    echo "All splunk servers"
else 
    echo "You need to specify which servers"
    exit
fi


splunk=( 10.10.5.30 10.10.5.31 10.10.5.32 10.10.5.36 10.10.5.33 10.10.5.34 10.10.20.25 10.10.20.26 10.10.20.27 10.10.20.28 10.10.20.29 )
virtual=( 10.10.5.30 10.10.5.31 10.10.5.32 10.10.5.36 10.10.5.33 10.10.5.34 )
physical=( 10.10.20.25 10.10.20.26 10.10.20.27 10.10.20.28 10.10.20.29 )

case "$1" in

# uname -a from all the matched lines
-u) if [ $3 = virtual ]
    then
        for i in ${virtual[@]}; do
            echo $i
            ssh vstanfield@$i uname -mrs;
            ssh vstanfield@$i df -h;
            ssh vstanfield@$i free -h;
        done
    elif [ $3 = physical ]
    then
        for i in ${physical[@]}; do
            echo $i
            ssh vstanfield@$i uname -mrs;
            ssh vstanfield@$i df -h;
            ssh vstanfield@$i free -h;
        done
    elif [ $3 = splunk ]
    then
        for i in ${splunk[@]}; do
            echo $i
            ssh vstanfield@$i uname -mrs;
            ssh vstanfield@$i df -h;
            ssh vstanfield@$i free -h;
        done
    else
        echo "Got here"
    fi
    ;;
*) echo "Invalid option"
   ;;
esac

