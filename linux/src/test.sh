#!/bin/sh

/usr/bin/python3 transmitfm1.py -f 93.4 -s 48000 -i uranium &
/usr/bin/python3 convert1.py -i ernie -s 48000 -b 128 &
/usr/bin/python3 params1.py -b 128 -id 1 -l Skyships -12C &
/usr/bin/python3 transmit1.py -ch 12C 
