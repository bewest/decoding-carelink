#!/bin/bash

for (( i = 0; i <= 18; i++ ))
do
	sleep 2
	dt=$(date +%Y%m%d_%H%M%S)
	sudo ./bin/mm-send-comm.py --prefix-path logs/$dt-pg-$i- --serial 584923 --port /dev/ttyUSB0 tweak ReadGlucoseHistory --page $i --save | tee analysis/cgm-$dt-pg-$i-ReadGlucoseHistory.markdown
	sudo ./bin/mm-send-comm.py --prefix-path logs/$dt-pg-$i- --serial 584923 --port /dev/ttyUSB0 tweak ReadISIGHistory --page $i --save | tee analysis/cgm-$dt-pg-$i-ReadISIGHistory.markdown
done


