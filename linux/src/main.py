import sys
import subprocess
import os
import time

def mp3tofifo_DAB_1(mp3_name, sample_rate, bit_rate):
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
    bash_script.write(f"""
/usr/bin/python3 convert1.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_1(bit_rate, station_id, label):
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
/usr/bin/python3 params1.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit_DAB_1(channel, dab):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    if (dab == True):
        add='&'
    else:
        add=''
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 transmit1.py -ch {channel} {add}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()

def mp3tofifo_DAB_2(mp3_name, sample_rate, bit_rate):
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
/usr/bin/python3 convert2.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_2(bit_rate, station_id, label):
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
/usr/bin/python3 params2.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit_DAB_2(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 transmit2.py -ch {channel}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()




def transmit_FM_1(frequency, sample_rate, mp3_name):
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 transmitfm1.py -f {frequency} -s {sample_rate} -i {mp3_name} &""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()


def transmit_FM_2(frequency1, frequency2,sample_rate, mp3_name1, mp3_name2):
    bash_script = open('launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 transmitfm2.py -f1 {frequency1} -f2 {frequency2} -s {sample_rate} -i1 {mp3_name1} -i2 {mp3_name2} """) #Create python launch sript inside launch shell script passing desired params
    bash_script.close()



def main(fm, dab):
    """
        main- Take in the paramters and displays help script if needed
    """
    #Create the default values
    mp3_name1 = 'uranium'
    mp3_name2 = 'jungle'
    mp3_name3 = 'ernie'
    mp3_name4 = 'jungle'
    sample_rate = 48000
    bit_rate = 128
    station_id1 = 1
    station_id2 = 2
    channel1 = '12C'
    channel2 = '13C'
    frequency1 = '93.4'
    frequency2 = '94.4'
    label1 = f'Skyships -{channel1}'
    label2 = f'Skyships -{channel2}'
    length= len(sys.argv)

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
        elif (sys.argv[i] == '-ch'):
            channel = sys.argv[i+1]
        elif (sys.argv[i] == '-f'):
            frequency = sys.argv[i+1]
        else:
            print(help)
    bash_script = open('launch.sh','a')
    bash_script.write(f"""#!/bin/sh
""")
    bash_script.close()
    if (fm == '1'):
        print('starting 1 FM radio')
        transmit_FM_1(frequency1, sample_rate, mp3_name1)
    elif (fm == '2'):
        print("starting 2 FM radio's")
        transmit_FM_2(frequency1, frequency2,sample_rate, mp3_name1, mp3_name2)
    elif (fm == '0'):
        print("'starting 0 FM radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    if (dab == '1'):
        print('starting 1 DAB radio')
        mp3tofifo_DAB_1(mp3_name3, sample_rate, bit_rate)
        params_DAB_1(bit_rate, station_id1, label1)
        transmit_DAB_1(channel1, False)
    elif (dab == '2'):
        mp3tofifo_DAB_1(mp3_name3, sample_rate, bit_rate)
        params_DAB_1(bit_rate, station_id1, label1)
        transmit_DAB_1(channel1, True)
        mp3tofifo_DAB_2(mp3_name4, sample_rate, bit_rate)
        params_DAB_2(bit_rate, station_id2, label2)
        transmit_DAB_2(channel2)
        print("'starting 2 DAB radio's")
    elif  (dab == '0'):
        print("'starting 0 DAB radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    os.system('cat launch.sh')
    os.system('sh launch.sh') #Launches the final script
    result2 = (subprocess.Popen('rm launch.sh',shell=True,stdout=subprocess.PIPE)) #Deletes any outstanding launch files


help = '''
Usage: sudo python3 main.py [options]

-i          mp3 name (without .mp3)
-s          sample rate
-b          bitrate
-ch         channel (changes the channel permentally until next change)
-id         channel id
-l          label
-h          help menu
'''
if __name__=="__main__":
    length=(len(sys.argv))-1
    if (sys.argv[length] == '-h'):
        print(help)
    else:
        fm = input('How many hackrf for FM transmit- ')
        dab = input('How many hackrf for DAB transmit- ')
        main(fm, dab)

