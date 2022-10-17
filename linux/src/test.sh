/usr/bin/python3 transmitfm2.py -f1 93.4 -f2 94.4 -s 32000 -i1 uranium -i2 jungle 
/usr/bin/python3 convert1.py -i ernie -s 48000 -b 128 &
/usr/bin/python3 params1.py -b 128 -id 1 -l skyships1 &
/usr/bin/python3 transmit1.py -ch 12C
