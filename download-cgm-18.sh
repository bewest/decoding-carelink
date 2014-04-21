
sudo ./bin/mm-send-comm.py  --init --port /dev/ttyUSB0  --serial 584923  --prefix  ReadCurPageNumber --prefix ReadCurGlucosePageNumber  sleep 0 | tee current-cgm-page.markdown

sleep 5

sudo ./bin/mm-send-comm.py --prefix-path logs/cgm-page-18- --serial 584923 --port /dev/ttyUSB0 tweak ReadSensorHistoryData --page 18 --save | tee analysis/send-page18-ReadSensorHistory.markdown

