#!/bin/bash
# terser explanation of log
# Useful to tell what clear_buffer has been up to.

grep -n --color  -E "howdy|clear_bu|BAD|CRC|ACK|IGNORE|ReadHistory|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" status-quo.log   

#####
# EOF
