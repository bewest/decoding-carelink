

dt=$(date +%Y%m%d_%H%M%S)
sudo ./bin/mm-send-comm.py --init --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak WriteGlucoseHistoryTimestamp --save | tee analysis/write-$dt-WriteGlucoseHistoryTimestamp.markdown
#sudo ./bin/mm-send-comm.py --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak WriteGlucoseHistoryTimestamp --save | tee analysis/write-$dt-WriteGlucoseHistoryTimestamp.markdown

