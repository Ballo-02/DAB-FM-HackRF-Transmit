import os
import sys

def mp3tofifo(mp3_name, sample_rate, bit_rate):
    sample_rate_short = str(int(sample_rate)/1000)
    command = (f"xterm -hold -e 'ffmpeg -re -i {mp3_name}.mp3 -ar {sample_rate} -f wav - |./../toolame-02l/toolame -s {sample_rate_short} -D 4 -b {bit_rate} /dev/stdin ./one.fifo'")
    os.system(command)
if __name__=="__main__":
    mp3_name = 'uranium'
    sample_rate = 48000
    bit_rate = 128
    length=len(sys.argv)
    for i in range(length):
        if (sys.argv[i] == '-i'):
            mp3_name = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
    mp3tofifo(mp3_name, sample_rate, bit_rate)

