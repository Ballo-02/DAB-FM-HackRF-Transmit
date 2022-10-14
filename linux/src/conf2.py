import sys
import os

def config(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Pipes in the given fifo stream and chooses which ensamble to broadcast on using the configeration file provided. This is then outputted on an 
    #xterm terminal
    if (channel != '13C'):
        print('test')
        # Read in the file
        with open('config_file.ini', 'r') as file :
            filedata = file.read()

        # Replace the target string
        new_channel = (f'channel={channel}')
        filedata = filedata.replace('channel=13C', new_channel)

        # Write the file out again
        with open('config_file.ini', 'w') as file:
            file.write(filedata)
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

