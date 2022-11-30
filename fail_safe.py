import os
import time
import subprocess

#Wait for all HackRF to run
time.sleep(30)
result = os.popen('cat src/values.txt') # Get values
result = result.read()
result = result.split(',') # Create the list to hold the values
result = [y.replace('\n', '') for y in result]
# Assign the variable with the correct values 
mp3_name1 = result[1]
mp3_name2 = result[3]
mp3_name3 = result[5]
mp3_name4 = result[7]
sample_rate1 = result[9]
sample_rate2 = result[11]
bit_rate = result[13]
station_id1 = result[15]
station_id2 = result[17]
label1 = result[19]
label2 = result[21]
channel1 = result[23]
channel2 = result[25]
ensID1 = result[27]
ensID2 = result[29]
ensLabel1 = result[31]
ensLabel2 = result[33]
service1 = result[35]
service2 = result[37]
frequency1 = result[39]
frequency2 = result[41]
default =[]
for i in range(43,50,1):
    default.append(result[i])
def main():
    """
        main- Kills and reboots scripts if any HackRF fails
    """
    #Query the usb message history when all HackRF are running to compare
    result = os.popen ('dmesg | grep 0000000000000000')
    result = result.read()
    result = result.split('\n')
    #Delete unesscary data which is also picked via specifying 0x16
    for i in range(3):
        del result[0]
    total_old = len(result)+3
    time.sleep(1)
    while (True):
        #See if any usb inputs have failed eg message will appear
        compare = os.popen ('dmesg | grep 0000000000000000')
        compare = compare.read()
        compare = compare.split('\n')
        total = len(compare)
        if ((total_old) != total):
            time.sleep(1)
            #Find what has HackRf has failed to kill and reboot the script
            fail = compare[total-2]
            fail = fail[38:]
            fail = fail.replace(' ', '')
            if (default[0] == fail):
                print('fm1')
                #Kill script
                os.system("sudo pkill -f 'fmtx1_real.py'")
                time.sleep(1)
                #Re-run script
                subprocess.Popen(["/usr/bin/python3", "src/transmitfm1.py", "-f", frequency1, "-s", sample_rate1, "-i", mp3_name1],"-p")
            elif (default[1] == fail):
                print('fm2')
                os.system("sudo pkill -f 'fmtx2_real.py'")
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/transmitfm1.py", "-f", frequency1, "-s", sample_rate1, "-i", mp3_name1,"-p"])
                subprocess.Popen(["/usr/bin/python3", "src/transmitfm2.py", "-f", frequency2, "-s", sample_rate1, "-i", mp3_name2],"-p")
            elif (default[2] == fail):
                print('dab1')
                os.system("sudo pkill -f 'odr-dabmod -C src/temp/config_real1.ini'")
                time.sleep(1)
                os.system("sudo pkill -f 'CRC-DabMux -i 0xc000'")
                time.sleep(1)
                os.system("sudo pkill -f 'ffmpeg -stream_loop -1 -re -i music/800.mp3'")
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/convert1.py", "-i", mp3_name3, "-s", sample_rate2, "-b", bit_rate ])
                time.sleep(1)
                subprocess.Popen(['/usr/bin/python3', "src/params1.py", "-b", bit_rate, "-id", station_id1, "-l", label1, "-eid", ensID1, "-el", ensLabel1, "-s2", service1 ])
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/transmit1.py", "-ch", channel1],"-p")
            elif (default[3] == fail):
                print('dab2')
                os.system("sudo pkill -f 'odr-dabmod -C src/temp/config_real2.ini'")
                time.sleep(1)
                os.system("sudo pkill -f 'CRC-DabMux -i 0xc001'")
                time.sleep(1)
                os.system("sudo pkill -f 'ffmpeg -stream_loop -1 -re -i music/1k.mp3'")
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/convert2.py", "-i", mp3_name4, "-s", sample_rate2, "-b", bit_rate ])
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/params2.py", "-b", bit_rate, "-id", station_id2, "-l", label2, "-eid", ensID2, "-el", ensLabel2, "-s", service2])
                time.sleep(1)
                subprocess.Popen(["/usr/bin/python3", "src/transmit2.py", "-ch", channel2],"-p")
            main()
main()