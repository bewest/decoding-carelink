
sudo ./bin/mm-send-comm.py  --init --port /dev/ttyUSB0  --serial 584923  --prefix  ReadCurPageNumber --prefix ReadCurGlucosePageNumber  sleep 0 | tee current-cgm-page.markdown


