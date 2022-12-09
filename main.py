import sys
import subprocess
import os
'''
    Author: Ballo-02
'''
def mp3tofifo_DAB_0(mp3_name, sample_rate, bit_rate, gui):
    """
       mp3tofifo_DAB_0- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    sample_rate_short = str(int(sample_rate)/1000) #Converts the file into KHz output
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen([f"{debug}ffmpeg -stream_loop -1 -re -i music/{mp3_name}.mp3 -ar {sample_rate} -f wav -| sudo ./repos/toolame-02l/toolame -s {sample_rate_short} -D 4 -b {bit_rate} /dev/stdin ./pipes/f0.fifo{debug_end}"],shell=True)
    #Find mp3 file and create wav file to output results to toolame to make it into an mp2 format piped into a fifo file
def params_DAB_0(bit_rate,station_id,label, ensID, ensLabel, service, gui):
    """
       params_DAB_0- Adds paramters to the given stream such as label, station id, proection level etc. This stream has come in from a previous ffmpg/toolame
       command and is outputed on a specifed fifo pipe.

       bit_rate - The bit rate which the frequency is wanted to be transmitted on
       station_id - Gives the station ID that is wanting to be used
       label - Gives the label wanting to be used
       ensID - Ensemble ID
       ensLabel - Ensamble Label
       service - Service ID
    """
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen([f"{debug}sudo ./repos/crc-dabmux/src/CRC-DabMux -i {ensID} -L {ensLabel} -A ./pipes/f0.fifo -b {bit_rate} -i {station_id} -p 3 -S -L {label} -i {service} -C -i1 -O fifo://pipes/s0.fifo{debug_end}"],shell=True)


def transmit_DAB_0(channel, gui):
    """
       transmit_DAB_0- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

       channel - Which channel/ensamble to broadcast on
    """
    #Pipes in the given fifo stream and chooses which ensamble to broadcast on using the configeration file provided. This is then outputted on an 
    #xterm terminal
    # Read in the file
    with open('src/temp/config_real0.ini', 'r') as file :
        filedata = file.read()

    # Replace the target string
    new_channel = (f'channel={channel}')
    filedata = filedata.replace('channel=', new_channel)

    # Write the file out again
    with open('src/temp/config_real0.ini', 'w') as file:
        file.write(filedata)
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen ([f"{debug}sudo ./repos/ODR-DabMod/odr-dabmod -C src/temp/config_real0.ini{debug_end}"],shell=True)

def mp3tofifo_DAB_1(mp3_name, sample_rate, bit_rate, gui):
    """
       mp3tofifo_DAB_1- Gets a mp3 file and converts it with passed parameters to a .wav file that is then piped to an output. The tool called toolame which
       converts the the given stream into an mp2 format again with passed parameters to allow the signal to be transmitted correctly which is finally
       passed to a given fifo pipe name in this case 'first.fifo' to alow the enxt process to take this steam

       mp3_name - The mp3 file that is wanted to be converted
       sample_rate - The sample rate which the frequency is wanting to be transmitted on
       bit_rate - The  bit rate which the frequency is wanted to be transmitted on

    """
    sample_rate_short = str(int(sample_rate)/1000) #Converts the file into KHz output
    #   Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen ([f"{debug}ffmpeg -stream_loop -1 -re -i music/{mp3_name}.mp3 -ar {sample_rate} -f wav -| sudo ./repos/toolame-02l/toolame -s {sample_rate_short} -D 4 -b {bit_rate} /dev/stdin ./pipes/f1.fifo{debug_end}"],shell=True)
def params_DAB_1(bit_rate,station_id,label, ensID, ensLabel, service, gui):
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
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen  ([f"{debug}sudo ./repos/crc-dabmux/src/CRC-DabMux -i {ensID} -L {ensLabel} -A ./pipes/f1.fifo -b {bit_rate} -i {station_id} -p 3 -S -L {label} -i {service} -C -i1 -O fifo://pipes/s1.fifo{debug_end}"],shell=True)
def transmit_DAB_1(channel, gui):
    """
       transmit_DAB_1- Transmits the pipe stream given as well as choosing which broadcast ensample to boradcast on

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
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen ([f"{debug}sudo ./repos/ODR-DabMod/odr-dabmod -C src/temp/config_real1.ini{debug_end}"],shell=True)


def transmit_FM_0(frequency, sample_rate, mp3_name, gui):
    """
        transmit_FM_0- Transmits the FM signal with the chosen frequency, sample rate and what to play

        frequency- What frequency the fm channel should be on
        sample_rate- The sample whichthe frequency is wanting to be on
        mp3_name- The mp3 file that is wanting to be played
    """
    # Read in the file
    with open('src/temp/fmtx0_real.py', 'r') as file :
        filedata = file.read()
    # Replace the target string
    new_frequency = (f'= freq = {frequency}e6')
    filedata = filedata.replace('= freq =', new_frequency)

    # Write the file out again
    with open('src/temp/fmtx0_real.py', 'w') as file:
        file.write(filedata)
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    os.system(f"sudo mpg123 -r{sample_rate} -m -s music/{mp3_name}.mp3 > pipes/stream0.fifo") # Create the stream to play and give permissions to allow reading from
    os.popen(f'sudo chmod u+=rwx pipes/*')
    subprocess.Popen  ([f"{debug}sudo /usr/bin/python3 src/temp/fmtx0_real.py{debug_end}"],shell=True)


def transmit_FM_1(frequency0, frequency1,sample_rate, mp3_name0, mp3_name1, gui):
    """
        transmit_FM_1- Transmits the FM signal twice with the chosen frequency, sample rate and what to play for both broadcasts

        frequency0/1- What frequency the fm channel should be on
        sample_rate0/1- The sample whichthe frequency is wanting to be on
        mp3_name0/1- The mp3 file that is wanting to be played
    """
     # Read in the file
    with open('src/temp/fmtx0_real.py', 'r') as file :
        filedata = file.read()
    # Replace the target string
    new_frequency = (f'= freq = {frequency0}e6')
    filedata = filedata.replace('= freq =', new_frequency)

    # Write the file out again
    with open('src/temp/fmtx0_real.py', 'w') as file:
        file.write(filedata)
    os.system(f"sudo mpg123 -r{sample_rate} -m -s music/{mp3_name0}.mp3 > pipes/stream0.fifo") # Create the stream to play and give permissions to allow reading from
    os.system(f"sudo mpg123 -r{sample_rate} -m -s music/{mp3_name1}.mp3 > pipes/stream1.fifo")
    os.popen(f'sudo chmod u+=rwx pipes/*')
    # Adds xterm command to beinning
    if (gui == 'True'):
        debug = "sudo xterm -hold -e '"
        debug_end = "'"
    else:
        debug = ""
        debug_end = ""
    subprocess.Popen ([f"{debug}sudo /usr/bin/python3 src/temp/fmtx0_real.py{debug_end}"],shell=True)
    # Read in the file
    with open('src/temp/fmtx1_real.py', 'r') as file :
        filedata = file.read()

    new_frequency = (f'= freq = {frequency1}e6')
    filedata = filedata.replace('= freq =', new_frequency)

    # Write the file out again
    with open('src/temp/fmtx1_real.py', 'w') as file:
        file.write(filedata)

    subprocess.Popen ([f"{debug}sudo /usr/bin/python3 src/temp/fmtx1_real.py{debug_end}"],shell=True)


def serial(fm, dab, channel0, channel1, frequency0, frequency1 , default):
    """
        serial- finds the hackrf's serial number and assigns them to either FM or DAB as well as hardcoding these values into the scripts

        fm- The amount of FM stations wanting to be run
        dab - The amount of DAB stations wanting to be run
    """
    if (fm == 1):
        fm0 = default[1] #Assigns the serial number to the variable
        print(f'fm0- {fm0} -on frequency {frequency0}')
        os.system('sudo cp src/fmtx_blank.py src/temp/fmtx0_real.py') #creates a new script with the serial hard coded
        os.popen(f'sudo chmod u+=rwx src/temp/fmtx0_real.py')
        with open('src/temp/fmtx0_real.py', 'r') as file :
            filedata = file.read()
        # Replace the target string
        new_serial = (f'hackrf={fm0}')
        filedata = filedata.replace('hackrf=', new_serial)
        filedata = filedata.replace('pipes', 'pipes/stream0.fifo')

        # Write the file out again
        with open('src/temp/fmtx0_real.py', 'w') as file:
            file.write(filedata)
        if (dab >= 1):
            default = [y.replace('0000000000000000', '') for y in default] #changes the serial sytax as ODR-DabMux can't use 0's
            dab0 = default[2]
            print(f'dab0-{dab0}-on ensamble {channel0}')
            os.system('sudo cp src/config_blank.ini src/temp/config_real0.ini') #creates a new script with the serial hard coded
            os.popen(f'sudo chmod u+=rwx src/temp/config_real0.ini')
            with open('src/temp/config_real0.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab0}')
            filedata = filedata.replace('device=serial=', new_serial)
            filedata = filedata.replace('pipes', './pipes/s0.fifo')
            # Write the file out again
            with open('src/temp/config_real0.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab1 = default[3]
                print(f'dab1- {dab1}-on ensamble {channel1}')
                os.system('sudo cp src/config_blank.ini src/temp/config_real1.ini')
                os.popen(f'sudo chmod u+=rwx src/temp/config_real1.ini')
                with open('src/temp/config_real1.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab1}')
                filedata = filedata.replace('device=serial=', new_serial)
                filedata = filedata.replace('pipes', './pipes/s1.fifo')
                # Write the file out again
                with open('src/temp/config_real1.ini', 'w') as file:
                    file.write(filedata)
    elif (fm ==2):
        fm0 = default[1]
        fm1 = default[2]
        print(f'fm0- {fm0} -on frequency {frequency0}')
        print(f'fm1- {fm1} -on frequency {frequency1}')
        os.system('sudo cp src/fmtx_blank.py src/temp/fmtx0_real.py') #creates a new script with the serial hard coded
        os.system('sudo cp src/fmtx_blank.py src/temp/fmtx1_real.py')
        os.popen(f'sudo chmod u+=rwx src/temp/fmtx0_real.py')
        os.popen(f'sudo chmod u+=rwx src/temp/fmtx1_real.py')
        with open('src/temp/fmtx0_real.py', 'r') as file :
            filedata = file.read()
        # Replace the target string
        new_serial = (f'hackrf={fm0}')
        filedata = filedata.replace('hackrf=', new_serial)
        filedata = filedata.replace('pipes', 'pipes/stream0.fifo')
        # Write the file out again
        with open('src/temp/fmtx0_real.py', 'w') as file:
            file.write(filedata)


        with open('src/temp/fmtx1_real.py', 'r') as file :
            filedata = file.read()
        new_serial = (f'hackrf={fm1}')
        filedata = filedata.replace('hackrf=', new_serial)
        filedata = filedata.replace('pipes', 'pipes/stream1.fifo')
        # Write the file out again
        with open('src/temp/fmtx1_real.py', 'w') as file:
            file.write(filedata)
        if (dab >= 1):
            default = [y.replace('0000000000000000', '') for y in default]  #changes the serial sytax as ODR-DabMux can't use 0's
            dab0 = default[3]
            print(f'dab0- {dab0}-on ensamble {channel0}')
            os.system('sudo cp src/config_blank.ini src/temp/config_real0.ini')
            os.popen(f'sudo chmod u+=rwx src/temp/config_real0.ini')
            with open('src/temp/config_real0.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab0}')
            filedata = filedata.replace('device=serial=', new_serial)
            filedata = filedata.replace('pipes', './pipes/s0.fifo')
            # Write the file out again
            with open('src/temp/config_real0.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab1 = default[4]
                print(f'dab1- {dab1}-on ensamble {channel1}')
                os.system('sudo cp src/config_blank1.ini src/temp/config_real1.ini')
                os.popen(f'sudo chmod u+=rwx src/temp/config_real1.ini')
                with open('src/temp/config_real1.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab1}')
                filedata = filedata.replace('device=serial=', new_serial)
                filedata = filedata.replace('pipes', './pipes/s1.fifo')

                # Write the file out again
                with open('src/temp/config_real1.ini', 'w') as file:
                    file.write(filedata)
    else:
        if (dab >= 1):
            default = [y.replace('0000000000000000', '') for y in default] #changes the serial sytax as ODR-DabMux can't use 0's
            dab0 = default[1]
            print(f'dab0-{dab0}-on ensamble {channel0}')
            os.system('sudo cp src/config_blank.ini src/temp/config_real0.ini') #creates a new script with the serial hard coded
            os.popen(f'sudo chmod u+=rwx src/temp/config_real0.ini')
            with open('src/temp/config_real0.ini', 'r') as file :
                filedata = file.read()
            # Replace the target string
            new_serial = (f'device=serial={dab0}')
            filedata = filedata.replace('device=serial=', new_serial)
            filedata = filedata.replace('pipes', './pipes/s0.fifo')
            # Write the file out again
            with open('src/temp/config_real0.ini', 'w') as file:
                file.write(filedata)
            if (dab == 2):
                dab1 = default[2]
                print(f'dab1-{dab1}-on ensamble {channel1}')
                os.system('sudo cp src/config_blank.ini src/temp/config_real1.ini')
                os.popen(f'sudo chmod u+=rwx src/temp/config_real1.ini')
                with open('src/temp/config_real1.ini', 'r') as file :
                    filedata = file.read()
                # Replace the target string
                new_serial = (f'device=serial={dab1}')
                filedata = filedata.replace('device=serial=', new_serial)
                filedata = filedata.replace('pipes', './pipes/s1.fifo')

                # Write the file out again
                with open('src/temp/config_real1.ini', 'w') as file:
                    file.write(filedata)
        else:
            print('Error- Typed more than 2? (Not Capable yet)')


def execute(mp3_name0, mp3_name1, mp3_name2, mp3_name3, 
sample_rate0, sample_rate1, 
bit_rate, 
station_id0, 
station_id1, 
label0, label1, 
channel0, channel1, 
frequency0, frequency1, 
ensID0, ensID1, 
ensLabel0, ensLabel1, 
service0, service1,
gui):
    """
        execute- Executes the specified function for FM and DAB

        mp3_name0 = MP3 file name of FM 1 station
        mp3_name1 = MP3 file name of FM 2 station
        mp3_name2 = MP3 file name of DAB 1 station
        mp3_name3 = MP3 file name of DAB 2 station
        sample_rate0 = Sample rate of FM audio stream 
        sample_rate1 = Sample rate of DAB audio stream
        bit_rate = Bit rate of audio stream
        station_id0 = Station ID of DAB station 1
        station_id1 = Station ID of DAB station 2
        label0 = Label of DAB station 1
        label1 = Label of DAB station 2
        channel0 = Channel ensamble used for DAB station 1
        channel1 = Channel ensamble used for DAB station 2
        frequency0 = Frequency of FM station 1 
        frequency1 = Frequency of FM station 1
        gui = Adds an xterm scree for each station for debug
    """
    if (fm == '1'):
        print('starting 1 FM radio')
        transmit_FM_0(frequency0, sample_rate0, mp3_name0, gui)
    elif (fm == '2'):
        transmit_FM_1(frequency0, frequency1,sample_rate0, mp3_name0, mp3_name1, gui)
        print("starting 2 FM radio's")
    elif (fm == '0'):
        print("starting 0 FM radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')
    if (dab == '1'):
        print('starting 1 DAB radio')
        mp3tofifo_DAB_0(mp3_name2, sample_rate1, bit_rate, gui)
        params_DAB_0(bit_rate,station_id0,label0, ensID0, ensLabel0, service0, gui)
        transmit_DAB_0(channel0, gui)
    elif (dab == '2'):
        mp3tofifo_DAB_0(mp3_name2, sample_rate1, bit_rate, gui)
        params_DAB_0(bit_rate,station_id0,label0, ensID0, ensLabel0, service0, gui)
        transmit_DAB_0(channel0, gui)
        mp3tofifo_DAB_1(mp3_name3, sample_rate1, bit_rate, gui)
        params_DAB_1(bit_rate, station_id1,label1, ensID1, ensLabel1, service1, gui)
        transmit_DAB_1(channel1, gui)
        print("starting 2 DAB radio's")
    elif  (dab == '0'):
        print("starting 0 DAB radio's")
    else:
        print('Error- Typed more than 2? (Not Capable yet)')

def main(fm, dab):
    """
        main- Take in the paramters and displays help script if needed
    """
    #Create the default values
    result = os.popen('cat src/values.txt') # Get values
    result = result.read()
    result = result.split(',') # Create the list to hold the values
    result = [y.replace('\n', '') for y in result]
    # Assign the variable with the correct values 
    gui = result[1]
    mp3_name0 = result[3]
    mp3_name1 = result[5]
    mp3_name2 = result[7]
    mp3_name3 = result[9]
    sample_rate0 = result[11]
    sample_rate1 = result[13]
    bit_rate = result[15]
    station_id0 = result[17]
    station_id1 = result[19]
    label0 = result[21]
    label1 = result[23]
    channel0 = result[25]
    channel1 = result[27]
    ensID0 = result[29]
    ensID1 = result[31]
    ensLabel0 = result[33]
    ensLabel1 = result[35]
    service0 = result[37]
    service1 = result[39]
    frequency0 = result[41]
    frequency1 = result[43]
    default =[]
    length= len(sys.argv)


    #If parameters are passed to the script this will take them in and change them values
    for i in range(length):
        if (sys.argv[i] == '-i' or sys.argv[i] == '-i1'):
            mp3_name0 = sys.argv[i+1]
        elif (sys.argv[i] == '-i2'):
            mp3_name1 = sys.argv[i+1]
        elif (sys.argv[i] == '-i3'):
            mp3_name2 = sys.argv[i+1]
        elif (sys.argv[i] == '-i4'):
            mp3_name3 = sys.argv[i+1]
        elif (sys.argv[i] == '-s' or sys.argv[i] == '-s1'):
            sample_rate0 = sys.argv[i+1]
        elif (sys.argv[i] == '-s2' ):
            sample_rate1 = sys.argv[i+1]
        elif (sys.argv[i] == '-b'):
            bit_rate = sys.argv[i+1]
        elif (sys.argv[i] == '-h'):
            print(help)
        elif (sys.argv[i] == '-id' or sys.argv[i] == '-id1'):
            station_id0 = sys.argv[i+1]
        elif (sys.argv[i] == '-id2'):
            station_id1 = sys.argv[i+1]
        elif (sys.argv[i] == '-l' or sys.argv[i] == '-l1'):
            label0 = sys.argv[i+1]
        elif (sys.argv[i] == '-l2'):
            label1 = sys.argv[i+1]
        elif (sys.argv[i] == '-ch' or sys.argv[i] == '-ch2'):
            channel0 = sys.argv[i+1]
        elif (sys.argv[i] == '-ch2'):
            channel1 = sys.argv[i+1]
        elif (sys.argv[i] == '-f' or sys.argv[i] == '-f1'):
            frequency0 = sys.argv[i+1]
        elif (sys.argv[i] == '-f2'):
            frequency1 = sys.argv[i+1]
        elif (sys.argv[i] == '-eid' or sys.argv[i] == '-eid1'):
            ensID0 = sys.argv[i+1]
        elif (sys.argv[i] == '-eid2'):
            ensID1 = sys.argv[i+1]
        elif (sys.argv[i] == '-el' or sys.argv[i] == '-el1'):
            ensLabel0 = sys.argv[i+1]
        elif (sys.argv[i] == '-el2'):
            ensLabel1 = sys.argv[i+1]
        elif (sys.argv[i] == '-sl' or sys.argv[i] == '-sl1'):
            service0 = sys.argv[i+1]
        elif (sys.argv[i] == '-sl2'):
            service1 = sys.argv[i+1]
        elif (sys.argv[i] == '-gui'):
            gui = sys.argv[i+1]
    if (sys.argv[i] == '-v'):
        # Added dedicated serial values
        default.append(result[45])
        default.append(result[47])
        default.append(result[49])
        default.append(result[51])
    else:
        # Search for HackRF serial numebrs anad assign them to stations
        result = os.popen ('hackrf_info | grep Serial') # Get the serial numbers of te HAckRf plugged in
        result = result.read()
        default=(result.split('Serial number:'))
        default = [y.replace('\n', '') for y in default] # Remove unwated infomation
        default = [y.replace(' ', '') for y in default]
    # Create pipes and give them read/write/execute permissions 
    os.popen(f'sudo chmod u+=rwx pipes')
    for i in range(2):
        subprocess.run( ["sudo", "mkfifo", f"./pipes/f{i}.fifo"], capture_output=True )
        subprocess.run( ["sudo", "mkfifo", f"./pipes/s{i}.fifo"], capture_output=True )
    os.popen(f'sudo chmod u+=rwx pipes/*')
    serial(int(fm), int(dab), channel0, channel1, frequency0, frequency1, default )
    execute(mp3_name0, mp3_name1, mp3_name2, mp3_name3, sample_rate0, sample_rate1, bit_rate, station_id0, station_id1, label0, label1, channel0, channel1, frequency0, frequency1, ensID0, ensID1, ensLabel0, ensLabel1, service0, service1, gui)



help = '''
Usage: sudo python3 src/main.py [options]
sudo python3 main.py -i1 uranium -i3 jungle -s 48000 -b 128 -ch1 11C -id1 1 -l1 'Ballo-02'

-v                  use HackRF serial values
-gui False          adds a debug/xterm screens (default true) 
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

