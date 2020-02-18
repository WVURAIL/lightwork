#!/bin/bash

export myrouter=`netstat -nr | awk '$1 == "0.0.0.0"{print$2}'`

if [ -e "$myrouter" ""]
then
   export myrouter=`netstat -nr | awk '$1 == "default"{print$2}'`
fi

echo $myrouter


