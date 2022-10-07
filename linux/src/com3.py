import sys
import os

def config():
    command = (f"xterm -hold -e 'sudo ./../ODR-DabMod/odr-dabmod config_file.ini'")
    os.system(command)
if __name__=="__main__":
    channel = '13C'
    length=len(sys.argv)
    for i in range(length):
        if (sys.argv[i] == '-ch'):
            channel = sys.argv[i+1]
    config()

