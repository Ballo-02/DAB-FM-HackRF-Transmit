import sys
import os
import time

def transmit_FM_2(frequency2, sample_rate, mp3_name2):
    """
        transmit_FM_2- Transmits the FM signal twice with the chosen frequency, sample rate and what to play for both broadcasts

        frequency2- What frequency the fm channel should be on
        sample_rate2- The sample whichthe frequency is wanting to be on
        mp3_name2- The mp3 file that is wanting to be played
    """
    # Read in the file
    with open('src/temp/fmtx2_real.py', 'r') as file :
        filedata = file.read()

    new_frequency = (f'= freq = {frequency2}e6')
    filedata = filedata.replace('= freq =', new_frequency)

    # Write the file out again
    with open('src/temp/fmtx2_real.py', 'w') as file:
        file.write(filedata)
    command2 = (f"xterm -e 'sudo mpg123 -r{sample_rate} -m -s ../music/{mp3_name2}.mp3 > pipes/stream2.fifo'")
    #os.system(command2)
    command2 = (f"xterm -hold -e 'sudo /usr/bin/python3 src/temp/fmtx2_real.py'")
    os.system(command2)
if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #Creates the default values
    frequency1 = '93.4'
    frequency2 = '94.4'
    sample_rate = 32000
    mp3_name2 = 'ernie'
    length=len(sys.argv)
    #If channel parameter is passed to the script
    for i in range(length):
        if (sys.argv[i] == '-f'):
            frequency2 = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-i'):
            mp3_name2 = sys.argv[i+1]
    time.sleep(5)
    transmit_FM_2(frequency2, sample_rate, mp3_name2)
