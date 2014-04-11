#!/bin/bash

set -x

# This is for educational/demonstration purposes only.

PRESSKEY=./bin/mm-press-key.py
TEMPBASAL=./bin/mm-temp-basals.py
STATUS=./bin/mm-set-suspend.py
INIT="$STATUS --init query"

# SERIAL controls which pump to talk to.
# Please, be responsible and careful.
SERIAL=208850
# PORT is the device file to use.  My udev rules create a nice
# persistent device.  You can try something like this:
# PORT=$(python decocare/scan.py)
PORT=/dev/ttyUSB.Carelink0

# just send power, and query basic status
# will report suspend/resume state as well as whether or not the pump
# is currently bolusing.
$INIT
sleep 2
# set temp basal rate to 0 for 90 minutes.
# --rate can be a float, like 2.0 or 0.025
# --duration must be a multiple of 30 minutes
# this sets a 0 rate for 90 minutes.
$TEMPBASAL --rate 0 --duration 90
sleep 2
# press the esc key, so we can see the results on the pump
$PRESSKEY esc
