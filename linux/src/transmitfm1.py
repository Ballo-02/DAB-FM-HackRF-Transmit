import sys
import os
import time

def transmit_FM_1(frequency, sample_rate, mp3_name):
    # Read in the file
    with open('fmtx1_real.py', 'r') as file :
        filedata = file.read()
    # Replace the target string
    new_frequency = (f'= freq = {frequency}e6')
    filedata = filedata.replace('= freq =', new_frequency)

    # Write the file out again
    with open('fmtx1_real.py', 'w') as file:
        file.write(filedata)
    command1 = (f"xterm -e 'sudo mpg123 -r{sample_rate} -m -s {mp3_name}.mp3 > stream1.fifo'")
    #os.system(command1)
    command2 = (f"xterm -hold -e 'sudo /usr/bin/python3 fmtx1_real.py'")
    os.system(command2)
if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #Creates the default values
    frequency = '93.4'
    sample_rate = 32000
    mp3_name = 'jungle'
    length=len(sys.argv)
    #If channel parameter is passed to the script
    for i in range(length):
        if (sys.argv[i] == '-f'):
            frequency = sys.argv[i+1]
        elif (sys.argv[i] == 's'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == 'i'):
            mp3_name = sys.argv[i+1]
    transmit_FM_1(frequency, sample_rate, mp3_name)
