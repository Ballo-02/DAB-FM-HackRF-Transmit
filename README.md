# DAB-FM-HackRF-Transmit
This project transmits 2 FM signals and 2 DAB signals (clearly) on a chosen frequency/ensemble, station name and any extra details that can be added, using HackRF One devices. It runs on 1 script with 4 HackRF's plugged in at once running on Linux (Ubunutu used). You can choose if you want what you want running e.g doesnt have to be all 4.

### Author Notes
This project was initially supposed to be run on both windows and linux but after spending some time with Syswin and other window compilers it seemed to over complicate things, as a lot of the binaries depended on linux and without great time and effort it did not seem worth it.

## Guidlines
Official guidelines to follow - 'In the UK the use of any radio transmitting device is required to be either licensed or specifically exempted from licensing under the Wireless Telegraphy Act 2006 (WT Act 2006)'

### `---Disclaimer---`
This repository contains scripts that can broadcast radio signals miles away which without a license is illegal in the UK. Therefore these scripts shall be deployed in a controlled environment for testing and results posted as shown.


## Team Members

|   Name              |    Username     |
|---------------------|-----------------|
| Owen Ball           |   Ballo-02      |


## Repos that need to be downlaoded
 - SoapySDR-
https://github.com/pothosware/SoapySDR
 - SoapyHackRF-
https://github.com/pothosware/SoapyHackRF
- toolame (not toolame-dab or twolame)
 Please see 'Install.txt' instructions as high chance of compile errors-
https://sourceforge.net/projects/toolame/
- ODR-DabMod-
https://github.com/Opendigitalradio/ODR-DabMod
- CRC-DabMux
 Please see 'Install.txt' instructions as high chance of compile errors-
https://github.com/coinchon/crc-dabmux

## Hardware Used
- HackRf One x4-
https://greatscottgadgets.com/hackrf/one/ 

- Dab Radio (can be any but this tells you a lot of information and allows you to select specific ensembles etc)-
https://www.digitalradiochoice.com/reviews/pure-elan-one-dab-bluetooth-radio/

## How to use?

Usage: sudo python3 main.py [options]

 - -v                  use the settings in 'values.txt'
 - -i 1/2              mp3 name for FM (without .mp3)
 - -i 3/4              mp3 name for DAB (without .mp3)
 - -s 1/2              sample rate (FM/DAB)
 - -b                  bitrate
 - -ch 1/2             channel 
 - -id 1/2             channel ID
 - -l 1/2              label
 - -eid 1/2            ensemble ID
 - -el 1/2             ensemble Label
 - -sl 1/2             service
 - -h                  help menu
 

## Examples
 - sudo python3 main.py -v
 
 Runs the parameters in 'values.txt'
 
 - sudo python3 main.py -i1 uranium -i3 jungle -s1 48000 -s2 48000 -b 128 -ch1 11C -id1 1 -l1 'Ballo-02'
 
 Broadcasts Uranium Fever on FM and Welcome to the Jungle mp3 on DAB on ensemble 11C with the label 'Ballo-02', station ID as 1 and both FM/DAB using a 48000 sample rate
 
## Installation
Go to the Install.txt, currenlty only working for Linux (no plans for any future OS unless high demand)
 
## Errors (Recommended to read)
 - Too Small, uou have to run the command 'mpg123 -r{samplerate} -m -s {mp3 name} > music/stream{1/2}' as a root user for FM stations as it's a current bug for converting your own mp3 files and so far no work around
 
  - If constant 'Mute' errors occur for DAB this is most likely due to sample rate problems with the file you have given specify with -s1/2
  
  - Thread error, most likely caused with a bottle neck with the USB bus you're using. You cannot use USB bus if you're wanting 2 FM + anything else 
 
  - Compile Errors, look at Installation.txt as that'll most likely help
 ## What's in this repository?

### `main.py`
The main script to deploy 2 DAB and 2 FM signals with the default values

### `src/`
Holds the scripts to deploy the stations depending on what parameters have been given

### `music/`
This is where you put the music files in .mp3 you want to be played

### `src/temp`
Holds the most recentley run configerations scripts with the hard coded HackRf One values in

### `src/launch.sh`
This is created when running and deleted once the main.py script is killed. This bash script launches the xterminals at once with the chosen configeration

### `src/temp/config_file_real1/2.ini`
Contains the configeration for transmitting the DAB station which can be edited manually or with the script (ODR-DabMod)

### `pipes/*.fifo)`
4 fifo pipes to allow real time encoding and transmitting to occur

### `music/uranium.mp3`
A mp3 file containing the song 'Uranium Fever' as a default test sound 

### `gnuradio/fmtx1/2.py`
Python3 script that runs GNURadio libaries to transmit FM 

## Documentation on sites used
- Tool used to convert mp3 files-
https://en.y2mate.is/68/youtube-to-mp3.html 
- Uranium Fever song used for testing-
https://www.youtube.com/watch?v=2ANI6oj8p2M
- Ernie song used for testing-
https://www.youtube.com/watch?v=8e1xvyTdBZI
- Welcome to the jungle song used for testing-
https://www.youtube.com/watch?v=o1tj2zJ2Wvg

- Sign Waves download tool-
https://www.audiocheck.net/audiofrequencysignalgenerator_sinetone.php
- Wav to mp3 tool-
https://online-audio-converter.com/ 

## Solo Commands for both FM and DAB

### DAB (3 seperate terminals)
 - sudo mkfifo pipes/f1.fifo
 - sudo mkfifo pipes/s1.fifo

 - sudo ffmpeg -re -i music/uranium.mp3 -ar 48000 -f wav | sudo ./repos/toolame-02l/toolame -s 48 -D 4 -b 128 /dev/stdin ./pipes/f1.fifo
 - sudo ./repos/crc-dabmux/src/DabMux -A ./pipes/f1.fifo -b 128 -i1 -p 3 -S -L 'Test1' -C -1 -O fifo://pipes/s1.fifo
 - sudo ./repos/ODR-DabMod/odr-dabmod -C src/temp/config_real1.ini
 
### FM (1 terminal)
 - sudo python gnuradio/fmtx1.py
### FM GNU
 - sudo gnuradio-companion
 
