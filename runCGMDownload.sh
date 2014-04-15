
sudo ./bin/mm-send-comm.py  --init --port /dev/ttyUSB0  --serial 584923  --prefix  ReadCurPageNumber --prefix ReadCurGlucosePageNumber  sleep 0

sleep 3
<<<<<<< HEAD
for ((i=20; i<=40; i++ ))
do
	sleep 5
=======
for ((i=1; i<40; i++ ))
do
	sleep 3
>>>>>>> 6a884cff54ebd2eff5ea802055e7af0281b44421
	sudo ./bin/mm-send-comm.py --prefix-path logs/cgm-page-$i- --serial 584923 --port /dev/ttyUSB0 tweak ReadSensorHistoryData --page $i --save | tee analysis/send-page$i-ReadSensorHistory.markdown
done
