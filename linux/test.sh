#!/bin/sh
/usr/bin/python3 src/convert1.py -i 800 -s 44100 -b 128 &
/usr/bin/python3 src/params1.py -b 128 -id 1 -l Skyships-12C -eid 0xc000 -el Skyships1 -s 10 &
/usr/bin/python3 src/transmit1.py -ch 12C &
#/usr/bin/python3 src/convert2.py -i 1k -s 44100 -b 128 &
#/usr/bin/python3 src/params2.py -b 128 -id 1 -l Skyships-13C -eid 0xc001 -el Skyships2 -s 11 &
#/usr/bin/python3 src/transmit2.py -ch 13C
