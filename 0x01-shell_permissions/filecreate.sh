#!/bin/bash
echo "file >"
read file
touch $file
echo "#!/bin/bash" > $file
echo "cnt >"
read cnt
echo $cnt >> $file
chmod 764 $file
bash dirgit.sh
