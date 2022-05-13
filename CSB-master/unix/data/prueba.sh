#1/usr/bin/bash
tail -n +2 $1 | cut -d ";"  -f 2 | sort | uniq -c >> $2


