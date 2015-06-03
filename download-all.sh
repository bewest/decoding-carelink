#!/bin/bash

SERIAL="417540"
PORT="/dev/ttyUSB0"
FOLDER="./data/"

if [ ! -e ${PORT} 2>/dev/null ]; then
    echo "Cannot find USB dongle!"
    exit 1
fi

# Get the number of pages
./bin/mm-send-comm.py --init --serial ${SERIAL} --port ${PORT} --prefix-path ${FOLDER} --prefix ReadCurGlucosePageNumber --save sleep 0 > ${FOLDER}ReadCurGlucosePageNumber.markdown

 
pages=`cat ${FOLDER}ReadCurGlucosePageNumber.markdown | grep -Po "page': \K([0-9]*)" | head -n 1`
glucose=`cat ${FOLDER}ReadCurGlucosePageNumber.markdown | grep -Po "glucose': \K([0-9]*)" | head -n 1`
start=$(expr $pages - $glucose)

for page in `seq ${start} ${pages}`; do
	`./bin/mm-send-comm.py --serial ${SERIAL} --port ${PORT} --prefix-path ${FOLDER} tweak ReadGlucoseHistory --page ${page} --save > ${FOLDER}ReadGlucoseHistory-page-${page}.markdown`
	`./bin/mm-send-comm.py --serial ${SERIAL} --port ${PORT} --prefix-path ${FOLDER} tweak ReadHistoryData --page ${page} --save > ${FOLDER}ReadHistoryData-page-${page}.markdown`

	echo "Decoding page ${page}.." 
	`./list_cgm.py ${FOLDER}ReadGlucoseHistory-page-${page}.data > ${FOLDER}ReadGlucoseHistory-page-${page}.json`

	curl --header "Content-type: application/json" --request POST --data-binary "@data/ReadGlucoseHistory-page-${page}.json" http://localhost:9000/upload

	echo "Decoding page ${page}.." 
	`./list_dates.py ${FOLDER}ReadHistoryData-page-${page}.data > ${FOLDER}ReadHistoryData-page-${page}-dates.json`
	`./list_history.py ${FOLDER}ReadHistoryData-page-${page}.data > ${FOLDER}ReadHistoryData-page-${page}-history.json`
	#curl --header "Content-type: application/json" --request POST --data-binary "@data/ReadHistoryData-page-${page}.json" http://localhost:9000/upload

done

#Page: 58
#./bin/mm-send-comm.py --serial 417540 --port /dev/ttyUSB0 --prefix-path ./ tweak ReadGlucoseHistory --page 58 --save
#python ./list_cgm.py ./ReadGlucoseHistory-page-58.data