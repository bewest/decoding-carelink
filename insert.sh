#!/bin/bash
#Bus 002 Device 011: ID 0a21:8001 Medtronic Physio Control Corp. 
sudo modprobe --first-time usbserial vendor=0x0a21 product=0x8001
#####
# EOF
