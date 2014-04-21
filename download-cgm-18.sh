
dt=$(date +%Y%m%d_%H%M%S)
sudo ./bin/mm-send-comm.py --init --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak ReadGlucoseHistory --page 16 --save | tee analysis/pg-16-$dt-ReadGlucoseHistory.markdown

