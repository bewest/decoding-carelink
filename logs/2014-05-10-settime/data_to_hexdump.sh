#!/bin/bash

for f in *.data; do
	hexdump -C $f > $f.hex
done
