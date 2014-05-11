#!/bin/bash

page=$1
dt=$(date +%Y%m%d_%H%M%S)
if [[ "$2" == "init" ]]; then
  echo "downloading page $page and initializing ($2)"
  sudo ./bin/mm-send-comm.py --init --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak ReadGlucoseHistory --page $page --save | tee analysis/pg-$page-$dt-ReadGlucoseHistory.markdown
  sudo ./bin/mm-send-comm.py --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak ReadISIGHistory --page $page --save | tee analysis/pg-$page-$dt-ReadISIGHistory.markdown
else
  echo "downloading page $page and NOT initializing ($2)"
  sudo ./bin/mm-send-comm.py --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak ReadGlucoseHistory --page $page --save | tee analysis/pg-$page-$dt-ReadGlucoseHistory.markdown
  sudo ./bin/mm-send-comm.py --prefix-path logs/$dt- --serial 584923 --port /dev/ttyUSB0 tweak ReadISIGHistory --page $page --save | tee analysis/pg-$page-$dt-ReadISIGHistory.markdown
fi
