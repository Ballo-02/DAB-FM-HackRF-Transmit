import sys
import os

def transmit_FM_1(frequency1,frequency2, sample_rate, mp3_name1, mp3name2):
#    if (frequency1 != '63.4'):
        # Read in the file
#        with open('fmtx2.py', 'r') as file :
#            filedata = file.read()

        # Replace the target string
#        new_frequency = (f'freq_1 = {frequency1}e6')
#        filedata = filedata.replace('freq_1 = ', new_frequency)

        # Write the file out again
#        with open('fmtx2.py', 'w') as file:
#            file.write(filedata)
#    if (frequency2 != '64.4'):
        # Read in the file
#        with open('fmtx2.py', 'r') as file :
#            filedata = file.read() 

        # Replace the target string
#        new_frequency = (f'freq_2 = {frequency2}e6')
#        filedata = filedata.replace('freq_2 = ', new_frequency)

        # Write the file out again
#        with open('fmtx2.py', 'w') as file:
#            file.write(filedata)
    command1 = (f"xterm -e 'sudo mpg123 -r{sample_rate} -m -s {mp3_name1}.mp3 > stream1.fifo'")
    os.system(command1)
    command2 = (f"xterm -e 'sudo mpg123 -r{sample_rate} -m -s {mp3_name2}.mp3 > stream2.fifo'")
    os.system(command2)
    command2 = (f"xterm -hold -e 'sudo /usr/bin/python3 fmtx2.py'")
    os.system(command2)
if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #Creates the default values
    frequency1 = '93.4'
    frequency2 = '94.4'
    sample_rate = 32000
    mp3_name1 = 'jungle'
    mp3_name2 = 'ernie'
    length=len(sys.argv)
    #If channel parameter is passed to the script
    for i in range(length):
        if (sys.argv[i] == '-f1'):
            frequency1 = sys.argv[i+1]
        elif (sys.argv[i] == '-f2'):
            frequency2 = sys.argv[i+1]
        elif (sys.argv[i] == 's'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == 'i1'):
            mp3_name1 = sys.argv[i+1]
        elif (sys.argv[i] == 'i2'):
            mp3_name2 = sys.argv[i+1]
    transmit_FM_1(frequency1, frequency2, sample_rate, mp3_name1, mp3_name2)
