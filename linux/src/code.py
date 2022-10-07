import sys
import subprocess
import os

def mp3tofifo(mp3_name, sample_rate, bit_rate):
    """
       mp3tofifo- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    result = (subprocess.Popen('mkfifo ./first.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    #Writes the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('launch.sh','a')
    bash_script.write(f"""#!/bin/sh
/usr/bin/python3 com1.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def config(bit_rate, station_id, label):
    """
       config- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    result = (subprocess.Popen('mkfifo ./second.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 com2.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 com3.py {channel} """) #Create python launch sript inside launch shell script passing desired params
    bash_script.close()
def main():
    """
        main- Take in the paramters and displays help script if needed
    """
    #Create the default values
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
    #If parameters are passed to the script this will take them in and change them values
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
        else:
            print(help)
    mp3tofifo(mp3_name, sample_rate, bit_rate)
    config(bit_rate, station_id, label)
    transmit(channel)
    os.system('sh launch.sh') #Launches the final script
    result2 = (subprocess.Popen('rm launch.sh',shell=True,stdout=subprocess.PIPE)) #Deletes any outstanding launch files
if __name__=="__main__":
    main()
