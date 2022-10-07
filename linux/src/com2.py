import os
import sys

def config(bit_rate,id,label):
    command=(f"sudo xterm -hold -e './../crc-dabmux/src/CRC-DabMux -A ./first.fifo -b {bit_rate} -i {station_id} -p 3 -S -L {label} -C -i1 -O fifo://second.fifo'")
    os.system(command)

if __name__=="__main__":
    bit_rate = 128
    station_id = 1
    label = 'Skyships'
    length=len(sys.argv)
    for i in range(length):
        if (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-id'):
            station_id = sys.argv[i+1]
        elif (sys.argv[i] == '-l'):
            label = sys.argv[i+1]
    config(bit_rate,station_id,label)

