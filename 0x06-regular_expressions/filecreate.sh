#!/bin/bash
echo "file >"
read file
touch $file
echo "#!/usr/bin/env ruby" > $file
echo "cnt >"
read cnt
echo $cnt >> $file
chmod 764 $file
bash dirgit.sh
gedit $file
