#!/bin/bash
echo "file >"
read file
touch $file
echo "#!/bin/bash" > $file
echo "content >"
read cnt
echo $cnt >> $file
chmod 764 $file
