# DAB-FM-HackRF-Transmit
This project transmits 2 FM signals and 2 DAB signals (clearly) on a chosen frequency/ensemble, station name and any extra details that can be added, using HackRf devices. It runs on 1 script with 4 HackRF's plugged in at once running on both Linux (Ubunutu used) and Windows (Windows 11 used).

## Guidlines
Official guidelines to follow - 'In the UK the use of any radio transmitting device is required to be either licensed or specifically exempted from licensing under the Wireless Telegraphy Act 2006 (WT Act 2006)'

### `---Disclaimer---`
This repository contains scripts that can boradcast radio signals miles are away which without a license is illegal. It shall be deployed in a controlled environment for testing and results posted as shown.

## Team Members

|   Name              |    Username     |
|---------------------|-----------------|
| Owen Ball           |   Ballo-02      |

##Documentation on sites used

https://en.y2mate.is/68/youtube-to-mp3.html - Tool used to convert uranium mp3 file
https://www.youtube.com/watch?v=2ANI6oj8p2M - Uranium fever song used for testing


## What's in this repository?

### `src/linux/src/main.py`
The main script to deploy 2 DAB and 2 FM signals with the default values

### `src/linux/src/com1.py`
This is 1/3 scipts to run each command seperately. In this case converting the mp3 to an mp2 stream with added parameters

### `src/linux/src/com2.py`
This is 2/3 scipts to run each command seperately. In this case taking in the audio stream and adding parameters such as label, station id, protection level etc.

### `src/linux/src/com3.py`
This is 3/3 scipts to run each command seperately. In this case transmitting the audio stream nto the HackRF and choosing which ensample to run on

### `src/linux/src/launch.sh`
This is created when running and deleted once the main.py script is killed. This bash script launches the xterminals at once with the chosen configeration

### `src/linux/src/config_file.ini`
Conatians the configeration for transmitting the DAB station which can be edited manually or with the script (ODR-DabMod)

### `src/linux/src/(first.fifo/second.fifo)`
2 fifo pipe files to allow streaming data to be passed to each command

### `src/linux/src/uranium.mp3`
A mp3 file containing the song 'Uranium Fever' as a default test sound 

## How to use?

### `src/linux/main.py` and `src/windows/main.py`
#### `Linux`

Usage: sudo python3 main.py [options]

 - -i          mp3 name (without .mp3)
 - -s          sample rate
 - -b          bitrate
 - -ch         channel (changes the channel permentally until next change)
 - -id         channel id
 - -l          label
 - -h          help menu
 

Example
 - python3 windows/src/main.py
 - python3 linux/src/main.py -ch 12C -b 128 -s 48000 -id 1 -l 'hello world' -i 'uranium'
 
 
