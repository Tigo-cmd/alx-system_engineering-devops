#!/bin/bash
echo "file >"
read file
touch $file
echo "#!/usr/bin/env bash" > $file
echo "cnt >"
read cnt
echo $cnt >> $file
chmod 764 $file
gedit $file
git add $file
bash dirgit.sh
