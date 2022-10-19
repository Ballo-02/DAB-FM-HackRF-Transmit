import sys
import subprocess
import os
import time

def mp3tofifo_DAB_1(mp3_name, sample_rate, bit_rate):
    """
       mp3tofifo- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    result = (subprocess.Popen('mkfifo ./../pipes/f1.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    #Writes the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh','a')
    bash_script.write(f"""
/usr/bin/python3 src/convert1.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_1(bit_rate, station_id, label):
    """
       config- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    result = (subprocess.Popen('mkfifo ./../pipes/s1.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3  src/params1.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit_DAB_1(channel, dab):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    if (dab == True):
        add='&'
    else:
        add=''
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmit1.py -ch {channel} {add}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()

def mp3tofifo_DAB_2(mp3_name, sample_rate, bit_rate):
    """
       mp3tofifo- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    result = (subprocess.Popen('mkfifo ./../pipes/f2.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    #Writes the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh','a')
    bash_script.write(f"""
/usr/bin/python3 src/convert2.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_2(bit_rate, station_id, label):
    """
       config- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    result = (subprocess.Popen('mkfifo ./../pipes/s2.fifo',shell=True,stdout=subprocess.PIPE)) #create fifo file
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/params2.py -b {bit_rate} -id {station_id} -l {label} &""") #Create python launch sript inside launch shell script passing desired params


def transmit_DAB_2(channel):
    """
       config- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmit2.py -ch {channel}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()




def transmit_FM_1(frequency, sample_rate, mp3_name, dab):
    if (dab == True):
        add='&'
    else:
        add=''
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmitfm1.py -f {frequency} -s {sample_rate} -i {mp3_name} {add}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()


def transmit_FM_2(frequency1, frequency2,sample_rate, mp3_name1, mp3_name2, dab):
    if (dab == True):
        add='&'
    else:
        add=''
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmitfm1.py -f {frequency1} -s {sample_rate} -i {mp3_name1} &""") #Create python launch sript inside launch shell script passing desired params
    bash_script.write(f"""
/usr/bin/python3 src/transmitfm2.py -f {frequency2} -s {sample_rate} -i {mp3_name2} {add}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()


def serial(fm, dab):
    result = os.popen('hackrf_info | grep Serial')
    result = result.read()
    amount=(result.split('Serial number:'))
    amount = [y.replace('\n', '') for y in amount]
    amount = [y.replace(' ', '') for y in amount]
    if (fm == 1):
        fm1 = amount[1]
        print(fm1)
        os.system('sudo cp src/fmtx1_blank.py src/temp/fmtx1_real.py')
        with open('src/temp/fmtx1_real.py', 'r') as file :
            filedata = file.read()
        # Replace the target string
        new_serial = (f'hackrf={fm1}')
        filedata = filedata.replace('hackrf=', new_serial)

        # Write the file out again
        with open('src/temp/fmtx1_real.py', 'w') as file:
            file.write(filedata)
        if (dab >= 1):
            amount = [y.replace('0000000000000000', '') for y in amount]
            dab1 = amount[2]
            print(dab1)
            os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini')
            with open('src/temp/config_real1.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab1}')
            filedata = filedata.replace('device=serial=', new_serial)
            # Write the file out again
            with open('src/temp/config_real1.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab2 = amount[3]
                print(dab2)
                os.system('sudo cp src/config_blank2.ini src/temp/config_real2.ini')
                with open('src/temp/config_real2.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab2}')
                filedata = filedata.replace('device=serial=', new_serial)
                # Write the file out again
                with open('src/temp/config_real2.ini', 'w') as file:
                    file.write(filedata)
    elif (fm ==2):
        fm1 = amount[1]
        fm2 = amount[2]
        print(fm1)
        print(fm2)
        os.system('sudo cp src/fmtx1_blank.py src/temp/fmtx2_real.py')
        os.system('sudo cp src/fmtx1_blank.py src/temp/fmtx1_real.py')
        with open('src/temp/fmtx1_real.py', 'r') as file :
            filedata = file.read()
        # Replace the target string
        new_serial = (f'hackrf={fm1}')
        filedata = filedata.replace('hackrf=', new_serial)
        # Write the file out again
        with open('src/temp/fmtx1_real.py', 'w') as file:
            file.write(filedata)


        with open('src/temp/fmtx2_real.py', 'r') as file :
            filedata = file.read()
        new_serial = (f'hackrf={fm2}')
        filedata = filedata.replace('hackrf=', new_serial)
        # Write the file out again
        with open('src/temp/fmtx2_real.py', 'w') as file:
            file.write(filedata)
        if (dab >= 1):
            amount = [y.replace('0000000000000000', '') for y in amount]
            dab1 = amount[3]
            print(dab1)
            os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini')
            with open('src/temp/config_real1.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab1}')
            filedata = filedata.replace('device=serial=', new_serial)
            # Write the file out again
            with open('src/temp/config_real1.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab2 = amount[4]
                print(dab2)
                os.system('sudo cp config_blank2.ini src/temp/config_real2.ini')
                with open('src/temp/config_real2.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab2}')
                filedata = filedata.replace('device=serial=', new_serial)

                # Write the file out again
                with open('src/temp/config_real2.ini', 'w') as file:
                    file.write(filedata)
    else:
        if (dab >= 1):
            amount = [y.replace('0000000000000000', '') for y in amount]
            dab1 = amount[1]
            print(dab1)
            os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini')
            with open('src/temp/config_real1.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab1}')
            filedata = filedata.replace('device=serial=', new_serial)
            # Write the file out again
            with open('src/temp/config_real1.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab2 = amount[2]
                print(dab2)
                os.system('sudo cp src/config_blank2.ini src/temp/config_real2.ini')
                with open('src/temp/config_real2.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab2}')
                filedata = filedata.replace('device=serial=', new_serial)

                # Write the file out again
                with open('src/temp/config_real2.ini', 'w') as file:
                    file.write(filedata)
            else:
                print('Error- Typed more than 2? (Not Capable yet)')
        else:
            print('Error- Typed more than 2? (Not Capable yet)')


def full_settings():
    new_channel = (f'channel={channel}')
    filedata = filedata.replace('channel=', new_channel)
    result = os.popen('cat values.txt')
    result = result.read()
    result = result.split(',')
    print(result)

def main(fm, dab):
    """
        main- Take in the paramters and displays help script if needed
    """
    #Create the default values
    mp3_name1 = '1k'
    mp3_name2 = '2k'
    mp3_name3 = 'cold'
    mp3_name4 = 'uranium'
    sample_rate = 48000
    bit_rate = 128
    station_id1 = 1
    station_id2 = 1
    channel1 = '12C'
    channel2 = '13C'
    frequency1 = '93.4'
    frequency2 = '94.4'
    label1 = f'Skyships-{channel1}'
    label2 = f'Skyships-{channel2}'
    length= len(sys.argv)

    #If parameters are passed to the script this will take them in and change them values
    for i in range(length):
        if (sys.argv[i] == '-i' or sys.argv[i] == '-i1'):
            mp3_name1 = sys.argv[i+1]
        elif (sys.argv[i] == '-i2'):
            mp3_name2 = sys.argv[i+1]
        elif (sys.argv[i] == '-i3'):
            mp3_name2 = sys.argv[i+1]
        elif (sys.argv[i] == '-i4'):
            mp3_name2 = sys.argv[i+1]
        elif (sys.argv[i] == '-s'):
            sample_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-h'):
            print(help)
        elif (sys.argv[i] == '-id' or sys.argv[i] == '-id1'):
            station_id1 = sys.argv[i+1]
        elif (sys.argv[i] == '-id2'):
            station_id2 = sys.argv[i+1]
        elif (sys.argv[i] == '-l' or sys.argv[i] == '-l1'):
            label1 = sys.argv[i+1]
        elif (sys.argv[i] == '-l2'):
            label2 = sys.argv[i+1]
        elif (sys.argv[i] == '-ch' or sys.argv[i] == '-ch2'):
            channel1 = sys.argv[i+1]
        elif (sys.argv[i] == '-ch2'):
            channel2 = sys.argv[i+1]
        elif (sys.argv[i] == '-f' or sys.argv[i] == '-f1'):
            frequency1 = sys.argv[i+1]
        elif (sys.argv[i] == '-f2'):
            frequency2 = sys.argv[i+1]
        elif (sys.argv[i] == '-v'):
            full_settings()
        else:
            print(help)
    bash_script = open('src/launch.sh','a')
    bash_script.write(f"""#!/bin/sh
""")
    bash_script.close()
    serial(int(fm), int(dab))
    if (fm == '1'):
        print('starting 1 FM radio')
        if (int(dab) > 0):
            transmit_FM_1(frequency1, sample_rate, mp3_name1, True)
        else:
            transmit_FM_1(frequency1, sample_rate, mp3_name1, False)
    elif (fm == '2'):
        if (int(dab) > 0):
            transmit_FM_2(frequency1, frequency2,32000, mp3_name1, mp3_name2, True)
        else:
            transmit_FM_2(frequency1, frequency2,32000, mp3_name1, mp3_name2, False)
        print("starting 2 FM radio's")
    elif (fm == '0'):
        print("'starting 0 FM radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    if (dab == '1'):
        print('starting 1 DAB radio')
        mp3tofifo_DAB_1(mp3_name3, sample_rate, bit_rate)
        params_DAB_1(bit_rate, station_id1, label1)
        transmit_DAB_1(channel1, False)
    elif (dab == '2'):
        mp3tofifo_DAB_1(mp3_name3, sample_rate, bit_rate)
        params_DAB_1(bit_rate, station_id1, label1)
        transmit_DAB_1(channel1, True)
        mp3tofifo_DAB_2(mp3_name4, sample_rate, bit_rate)
        params_DAB_2(bit_rate, station_id2, label2)
        transmit_DAB_2(channel2)
        print("'starting 2 DAB radio's")
    elif  (dab == '0'):
        print("'starting 0 DAB radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    os.system('cat src/launch.sh')
    os.system('sh src/launch.sh') #Launches the final script
    result2 = (subprocess.Popen('rm src/launch.sh',shell=True,stdout=subprocess.PIPE)) #Deletes any outstanding launch files


help = '''
Usage: sudo python3 src/main.py [options]
sudo python3 src/main.py -i1 uranium -i2 jungle -s 48000 -b 128 -ch1 11C -id1 1 -l1 'Ballo-02'

-v                  use the settings in 'values.txt'
-i 1/2/3/4          mp3 name (without .mp3)
-s                  sample rate
-b                  bitrate
-ch 1/2             channel 
-id 1/2             channel id
-l 1/2              label
-h                  help menu
'''
if __name__=="__main__":
#    sys.argv=['-ch','11C']
    length=(len(sys.argv))-1
    if (sys.argv[length] == '-h'):
        print(help)
    else:
        fm = input('How many hackrf for FM transmit- ')
        dab = input('How many hackrf for DAB transmit- ')
        main(fm, dab)
