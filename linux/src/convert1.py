import os
import sys

def mp3tofifo(mp3_name, sample_rate, bit_rate):
    """
       mp3tofifo- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    sample_rate_short = str(int(sample_rate)/1000) #Converts the file into KHz output
    #Creates the stream that converts the mp3 to wav piped into toolame tool to make it into a mp2 stream and output the command to xterm window
    command = (f"xterm -hold -e 'sudo ffmpeg -stream_loop -1 -re -i music/{mp3_name}.mp3 -ar {sample_rate} -f wav - |./repos/toolame-02l/toolame -s {sample_rate_short} -D 4 -b {bit_rate} /dev/stdin ./pipes/f1.fifo'")
    os.system(command)
if __name__=="__main__":
    """
        Take in the paramters and runs mp3tofifo funtion
    """
    #Creates default values
    mp3_name = 'uranium'
    sample_rate = 48000
    bit_rate = 128
    length=len(sys.argv)
    #If parameters are passed to the script this will take them in and change them values
    for i in range(length):
        if (sys.argv[i] == '-i'):
            mp3_name = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
    mp3tofifo(mp3_name, sample_rate, bit_rate)

