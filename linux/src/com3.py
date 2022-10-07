import sys
import os

def config(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Pipes in the given fifo stream and chooses which ensamble to broadcast on using the configeration file provided. This is then outputted on an 
    #xterm terminal
    command = (f"xterm -hold -e 'sudo ./../ODR-DabMod/odr-dabmod config_file.ini'")
    os.system(command)
if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #Creates the default values
    channel = '13C'
    length=len(sys.argv)
    #If channel parameter is passed to the script
    for i in range(length):
        if (sys.argv[i] == '-ch'):
            channel = sys.argv[i+1]
    config(channel)

