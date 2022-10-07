import sys
import subprocess
import os

def mp3tofifo(mp3_name, sample_rate, bit_rate):
    sample_rate_short = sample_rate/1000
    result = (subprocess.Popen('mkfifo ./one.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    bash_script = open('launch.sh','a')
    bash_script.write(f"""#!/bin/sh
/usr/bin/python3 com1.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def config(bit_rate, station_id, label):
    result = (subprocess.Popen('mkfifo ./second.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 com2.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit(channel):
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 com3.py {channel} """) #Create python launch sript inside launch shell script passing desired params
    bash_script.close()
if __name__=="__main__":
    mp3_name = 'uranium'
    sample_rate = 48000
    bit_rate = 128
    length=len(sys.argv)
    label = 'Skyships'
    station_id = 1
    channel = '13C'
    help = '''
Usage: sudo python3 main.py [options] 

-i          mp3 name (without .mp3)
-s          sample rate
-b          bitrate
-h          help menu
'''
    for i in range(length):
        if (sys.argv[i] == '-i'):
            mp3_name = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-h'):
            print(help)
        elif (sys.argv[i] == '-id'):
            station_id = sys.argv[i+1]
        elif (sys.argv[i] == '-l'):
            label = sys.argv[i+1]
    mp3tofifo(mp3_name, sample_rate, bit_rate)
    config(bit_rate, station_id, label)
    transmit(channel)
    os.system('sh launch.sh')
    result2 = (subprocess.Popen('rm launch.sh',shell=True,stdout=subprocess.PIPE)) #delete any outstanding launch files

