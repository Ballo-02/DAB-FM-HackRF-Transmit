import sys
import subprocess
import os
'''
    Author: Ballo-02
'''
def mp3tofifo_DAB_1(mp3_name, sample_rate, bit_rate):
    """
       mp3tofifo_DAB_1- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    #Writes the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh','a')
    bash_script.write(f"""
/usr/bin/python3 src/convert1.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_1(bit_rate,station_id,label, ensID, ensLabel, service):
    """
       params_DAB_1- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
       ensID - Ensemble ID
       ensLabel - Ensamble Label
       service - Service ID
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/params1.py -b {bit_rate} -id {station_id} -l {label} -eid {ensID} -el {ensLabel} -s {service} &""") #Create python launch sript inside launch shell script passing desired params


def transmit_DAB_1(channel, dab):
    """
       transmit_DAB_1- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
       dab - Allows the script to know if more commands are needed
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
       mp3tofifo_DAB_2- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    #Writes the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh','a')
    bash_script.write(f"""
/usr/bin/python3 src/convert2.py -i {mp3_name} -s {sample_rate} -b {bit_rate} &""")
    bash_script.close()
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_2(bit_rate,station_id,label, ensID, ensLabel, service):
    """
       params_DAB_2- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
       ensID - Ensemble ID
       ensLabel - Ensamble Label
       service - Service ID
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/params2.py -b {bit_rate} -id {station_id} -l {label} -eid {ensID} -el {ensLabel} -s {service} &""")#Create python launch sript inside launch shell script passing desired params


def transmit_DAB_2(channel):
    """
       transmit_DAB_2- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Write the command into a launch.sh script so multiple xterms can be run at once
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmit2.py -ch {channel}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()




def transmit_FM_1(frequency, sample_rate, mp3_name, dab):
    """
        transmit_FM_1- Transmits the FM signal with the chosen frequency, sample rate and what to play

        frequency- What frequency the fm channel should be on
        sample_rate- The sample whichthe frequency is wanting to be on
        mp3_name- The mp3 file that is wanting to be played
        dab - Allows the script to know if more commands are needed
    """
    #Adds & if dab command is also needing to be run
    if (dab == True):
        add='&'
    else:
        add=''
    bash_script = open('src/launch.sh', 'a')
    bash_script.write(f"""
/usr/bin/python3 src/transmitfm1.py -f {frequency} -s {sample_rate} -i {mp3_name} {add}""") #Create python launch sript inside launch shell script passing desired params
    bash_script.close()


def transmit_FM_2(frequency1, frequency2,sample_rate, mp3_name1, mp3_name2, dab):
    """
        transmit_FM_2- Transmits the FM signal twice with the chosen frequency, sample rate and what to play for both broadcasts

        frequency1/2- What frequency the fm channel should be on
        sample_rate1/2- The sample whichthe frequency is wanting to be on
        mp3_name1/2- The mp3 file that is wanting to be played
        dab - Allows the script to know if more commands are needed
    """
    #Adds & if dab command is also needing to be run
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


def serial(fm, dab, channel1, channel2, frequency1, frequency2 , default = []):
    """
        serial- finds the hackrf's serial number and assigns them to either FM or DAB as well as hardcoding these values into the scripts

        fm- The amount of FM stations wanting to be run
        dab - The amount of DAB stations wanting to be run
    """
    if (len(default) == 0):
        result = os.popen ('hackrf_info | grep Serial') # Get the serial numbers of te HAckRf plugged in
        result = result.read()
        amount=(result.split('Serial number:'))
        amount = [y.replace('\n', '') for y in amount] # Remove unwated infomation
        amount = [y.replace(' ', '') for y in amount]
    else:
        amount=['']
        for i in range (len(default)):
            amount.append(default[i])
    if (fm == 1):
        fm1 = amount[1] #Assigns the serial number to the variable
        print(f'fm1- {fm1} -on frequency {frequency1}')
        os.system('sudo cp src/fmtx1_blank.py src/temp/fmtx1_real.py') #creates a new script with the serial hard coded
        with open('src/temp/fmtx1_real.py', 'r') as file :
            filedata = file.read()
        # Replace the target string
        new_serial = (f'hackrf={fm1}')
        filedata = filedata.replace('hackrf=', new_serial)

        # Write the file out again
        with open('src/temp/fmtx1_real.py', 'w') as file:
            file.write(filedata)
        if (dab >= 1):
            amount = [y.replace('0000000000000000', '') for y in amount] #changes the serial sytax as ODR-DabMux can't use 0's
            dab1 = amount[2]
            print(f'dab1-{dab1}-on ensamble {channel1}')
            os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini') #creates a new script with the serial hard coded
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
                print(f'dab2- {dab2}-on ensamble {channel2}')
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
        print(f'fm1- {fm1} -on frequency {frequency1}')
        print(f'fm2- {fm2} -on frequency {frequency2}')
        os.system('sudo cp src/fmtx1_blank.py src/temp/fmtx1_real.py') #creates a new script with the serial hard coded
        os.system('sudo cp src/fmtx2_blank.py src/temp/fmtx2_real.py')
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
            amount = [y.replace('0000000000000000', '') for y in amount]  #changes the serial sytax as ODR-DabMux can't use 0's
            dab1 = amount[3]
            print(f'dab1- {dab1}-on ensamble {channel1}')
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
                print(f'dab2- {dab2}-on ensamble {channel2}')
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
        if (dab >= 1):
            amount = [y.replace('0000000000000000', '') for y in amount] #changes the serial sytax as ODR-DabMux can't use 0's
            dab1 = amount[1]
            print(f'dab1-{dab1}-on ensamble {channel1}')
            os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini') #creates a new script with the serial hard coded
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
                print(f'dab2-{dab2}-on ensamble {channel2}')
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

def execute(mp3_name1, mp3_name2, mp3_name3, mp3_name4, sample_rate1, sample_rate2, bit_rate, station_id1, station_id2, label1, label2, channel1, channel2, frequency1, frequency2, ensID1, ensID2, ensLabel1, ensLabel2, service1, service2):
    """
        execute- Executes the specified function for FM and DAB

        mp3_name1 = MP3 file name of FM 1 station
        mp3_name2 = MP3 file name of FM 2 station
        mp3_name3 = MP3 file name of DAB 1 station
        mp3_name4 = MP3 file name of DAB 2 station
        sample_rate1 = Sample rate of FM audio stream 
        sample_rate2 = Sample rate of DAB audio stream
        bit_rate = Bit rate of audio stream
        station_id1 = Station ID of DAB station 1
        station_id2 = Station ID of DAB station 2
        label1 = Label of DAB station 1
        label2 = Label of DAB station 2
        channel1 = Channel ensamble used for DAB station 1
        channel2 = Channel ensamble used for DAB station 2
        frequency1 = Frequency of FM station 1 
        frequency2 = Frequency of FM station 1
    """
    if (fm == '1'):
        print('starting 1 FM radio')
        if (int(dab) > 0):
            transmit_FM_1(frequency1, sample_rate1, mp3_name1, True)
        else:
            transmit_FM_1(frequency1, sample_rate1, mp3_name1, False)
    elif (fm == '2'):
        if (int(dab) > 0):
            transmit_FM_2(frequency1, frequency2,sample_rate1, mp3_name1, mp3_name2, True)
        else:
            transmit_FM_2(frequency1, frequency2,sample_rate1, mp3_name1, mp3_name2, False)
        print("starting 2 FM radio's")
    elif (fm == '0'):
        print("starting 0 FM radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    if (dab == '1'):
        print('starting 1 DAB radio')
        mp3tofifo_DAB_1(mp3_name3, sample_rate2, bit_rate)
        params_DAB_1(bit_rate,station_id1,label1, ensID1, ensLabel1, service1)
        transmit_DAB_1(channel1, False)
    elif (dab == '2'):
        mp3tofifo_DAB_1(mp3_name3, sample_rate2, bit_rate)
        params_DAB_1(bit_rate,station_id1,label1, ensID1, ensLabel1, service1)
        transmit_DAB_1(channel1, True)
        mp3tofifo_DAB_2(mp3_name4, sample_rate2, bit_rate)
        params_DAB_2(bit_rate, station_id2,label2, ensID2, ensLabel2, service2)
        transmit_DAB_2(channel2)
        print("starting 2 DAB radio's")
    elif  (dab == '0'):
        print("starting 0 DAB radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    #os.system('cat src/launch.sh')
    os.system('sh src/launch.sh') #Launches the final script
    subprocess.Popen('sudo rm src/launch.sh',shell=True,stdout=subprocess.PIPE) #Deletes any outstanding launch files


def full_settings():
    """
        full_settings- Takes in the values from 'values.txt'for effiency when -v is passed

    """
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
    default.append(result[43])
    default.append(result[45])
    default.append(result[47])
    default.append(result[49])
    serial(int(fm), int(dab), channel1, channel2, frequency1, frequency2, default )
    execute(mp3_name1, mp3_name2, mp3_name3, mp3_name4, sample_rate1, sample_rate2, bit_rate, station_id1, station_id2, label1, label2, channel1, channel2, frequency1, frequency2, ensID1, ensID2, ensLabel1, ensLabel2, service1, service2,)


def main(fm, dab):
    """
        main- Take in the paramters and displays help script if needed
    """
    #Create the default values
    mp3_name1 = '400'
    mp3_name2 = '600'
    mp3_name3 = '800'
    mp3_name4 = '1k'
    sample_rate1 = 32000
    sample_rate2 = 48000
    bit_rate = 128
    station_id1 = 1
    station_id2 = 1
    channel1 = '12C'
    channel2 = '13C'
    frequency1 = '93.4'
    frequency2 = '94.4'
    label1 = f'Skyships-{channel1}'
    label2 = f'Skyships-{channel2}'
    ensID1 = '0xc000'
    ensLabel1 = 'Skyships1'
    service1 = '10'
    ensID2 = '0xc001'
    ensLabel2 = 'Skyships2'
    service2 = '11'
    length= len(sys.argv)

    bash_script = open('src/launch.sh','a') #makes it into a bash script
    bash_script.write(f"""#!/bin/sh""")
    bash_script.close()



    #If parameters are passed to the script this will take them in and change them values
    for i in range(length):
        if (sys.argv[i] == '-i' or sys.argv[i] == '-i1'):
            mp3_name1 = sys.argv[i+1]
        elif (sys.argv[i] == '-i2'):
            mp3_name2 = sys.argv[i+1]
        elif (sys.argv[i] == '-i3'):
            mp3_name3 = sys.argv[i+1]
        elif (sys.argv[i] == '-i4'):
            mp3_name4 = sys.argv[i+1]
        elif (sys.argv[i] == '-s' or sys.argv[i] == '-s1'):
            sample_rate1 = sys.argv[i+1]
        elif (sys.argv[i] == '-s2' ):
            sample_rate2 = sys.argv[i+1]
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
        elif (sys.argv[i] == '-eid' or sys.argv[i] == '-eid1'):
            ensID1 = sys.argv[i+1]
        elif (sys.argv[i] == '-eid2'):
            ensID2 = sys.argv[i+1]
        elif (sys.argv[i] == '-el' or sys.argv[i] == '-el1'):
            ensLabel1 = sys.argv[i+1]
        elif (sys.argv[i] == '-el2'):
            ensLabel2 = sys.argv[i+1]
        elif (sys.argv[i] == '-sl' or sys.argv[i] == '-sl1'):
            service1 = sys.argv[i+1]
        elif (sys.argv[i] == '-sl2'):
            service2 = sys.argv[i+1]
    if (sys.argv[i] == '-v'): #use values.txt
        full_settings()
    else:
        serial(int(fm), int(dab), channel1, channel2, frequency1, frequency2 )
        execute(mp3_name1, mp3_name2, mp3_name3, mp3_name4, sample_rate1, sample_rate2, bit_rate, station_id1, station_id2, label1, label2, channel1, channel2, frequency1, frequency2, ensID1, ensID2, ensLabel1, ensLabel2, service1, service2)



help = '''
Usage: sudo python3 src/main.py [options]
sudo python3 main.py -i1 uranium -i3 jungle -s 48000 -b 128 -ch1 11C -id1 1 -l1 'Ballo-02'

-v                  use the settings in 'values.txt'
-i 1/2              mp3 name for FM (without .mp3)
-i 3/4              mp3 name for DAB (without .mp3)
-s 1/2              sample rate (FM/DAB)
-b                  bitrate
-ch 1/2             channel 
-id 1/2             channel ID
-l 1/2              label
-eid 1/2            ensemble ID
-el 1/2             ensemble Label
-sl 1/2             service
-h                  help menu
'''
if __name__=="__main__":
    length=(len(sys.argv))-1
    if (sys.argv[length] == '-h'):
        print(help)
    else:
        fm = input('How many hackrf for FM transmit- ')
        dab = input('How many hackrf for DAB transmit- ')
        main(fm, dab)

