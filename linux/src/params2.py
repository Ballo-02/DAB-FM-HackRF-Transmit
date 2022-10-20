import os
import sys

def params(bit_rate,station_id,label, ensID, ensLabel, service):
    """
       params- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.
       
       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
       ensID - Ensemble ID
       ensLabel - Ensamble Label
       service - Service ID
    """
    #Adds onto the piped stream parameters allowing the station to be correctly broadcast amd finally outputting the stream to different pipe. Runs this in 
    #xterm to open another window
    command=(f"sudo xterm -hold -e 'sudo ./repos/crc-dabmux/src/CRC-DabMux -i {ensID} -L {ensLabel} -A ./pipes/f2.fifo -b {bit_rate} -i {station_id} -p 3 -S -L {label} -i {service} -C -i1 -O fifo://pipes/s2.fifo'")
    os.system(command)

if __name__=="__main__":
    """
        Take in the paramters and runs config funtion
    """
    #sys.argv=['-b','128','-id','1','-l','skyships']
    #Creates default values
    bit_rate = '128'
    station_id = '1'
    label = 'Skyships2'
    ensID = '0xc001'
    ensLabel = 'Skyships2'
    service = '11'
    length=len(sys.argv)
    #If parameters are passed to the script
    for i in range(length):
        if (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-id'):
            station_id = sys.argv[i+1]
        elif (sys.argv[i] == '-l'):
            label = sys.argv[i+1]
        elif (sys.argv[i] == '-eid'):
            ensID = sys.argv[i+1]
        elif (sys.argv[i] == '-el'):
            ensLabel = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            service = sys.argv[i+1]
    params(bit_rate, station_id, label, ensID, ensLabel, service)
