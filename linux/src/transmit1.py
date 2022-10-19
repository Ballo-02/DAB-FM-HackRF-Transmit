import sys
import os
import time

def transmit_DAB_1(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on
       channel - Which channel/ensamble to broadcast on
    """
    #Pipes in the given fifo stream and chooses which ensamble to broadcast on using the configeration file provided. This is then outputted on an 
    #xterm terminal
    # Read in the file
    with open('src/temp/config_real1.ini', 'r') as file :
        filedata = file.read()

    # Replace the target string
    new_channel = (f'channel={channel}')
    filedata = filedata.replace('channel=', new_channel)

    # Write the file out again
    with open('src/temp/config_real1.ini', 'w') as file:
        file.write(filedata)
    command = (f"xterm -hold -e 'sudo ./repos/ODR-DabMod/odr-dabmod src/temp/config_real1.ini'")
    os.system(command)
if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #Creates the default values
    channel = '12C'
    length=len(sys.argv)
    #If channel parameter is passed to the script
    for i in range(length):
        if (sys.argv[i] == '-ch'):
            channel = sys.argv[i+1]
    time.sleep(10)
    transmit_DAB_1(channel)
