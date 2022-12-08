#! /bin/sh

apt-get install python3 hackrf libhackrf-dev make cmake xterm gnuradio gr-osmosdr ffmpeg g++ libpython3-dev python3-numpy swig autoconf fftw3-dev libuhd-dev libfec-dev git libtool -y&&

chmod 777 repos/
cd repos/ &&
git clone https://github.com/pothosware/SoapySDR
git clone https://github.com/pothosware/SoapyHackRF
git clone https://github.com/zeromq/libzmq
git clone https://github.com/Opendigitalradio/ODR-DabMod
git clone https://github.com/coinchon/crc-dabmux


chmod 777 -R repos/*
cd crc-dabmux &&
sed -i '27i #include <sys/resource.h>' repos/crc-dabmux/src/DabMux.cpp

./configure; make; make install

cd libzmq &&
./autogen.sh; ./configure; make; make install

cd ODR-DabMod &&
./bootstrap.sh; ./configure; make; make install

cd SoapySDR &&
mkdir build; cd build; cmake ..; make -j4; sudo make install; sudo ldconfig

sudo add-apt-repository -y ppa:myriadrf/drivers
sudo apt-get update

cd SoapyHackRF &&
mkdir build; cd build; cmake ..; make -j4; sudo make install; sudo ldconfig

cd toolame-02l &&
make clean
make