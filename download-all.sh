#!/bin/bash

SERIAL="417540"
PORT="/dev/ttyUSB0"
FOLDER="./data/"

if [ ! -e ${PORT} 2>/dev/null ]; then
    echo "Cannot find USB dongle!"
    exit 1
fi

./bin/mm-glucose.py --init --serial 417540 --port /dev/ttyUSB0
curl --header "Content-type: application/json" --request POST --data-binary "@glucose.json" http://localhost:9000/upload/sensor

./bin/mm-history.py --init --serial 417540 --port /dev/ttyUSB0
curl --header "Content-type: application/json" --request POST --data-binary "@history.json" http://localhost:9000/upload/pump
