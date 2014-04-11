
for ((i=1; i<10; i++ ))
do
	sleep 5
	sudo ./bin/mm-send-comm.py --init --serial 584923 --port /dev/ttyUSB0 tweak ReadSensorHistoryData --page $i --save | tee analysis/send-page$i-ReadSensorHistory.markdown
done
