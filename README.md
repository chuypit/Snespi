# snespi
mi servi pi

## Diagrama
gpio raspberry
pn532 spi 
 ```bash
SCLK = 4  
MISO = 17 
MOSI = 27 
CS   = 22 
button = 18
```

## Install

 ```bash
sudo apt-get update
sudo apt-get install python2.7-dev
cd ~
git clone https://github.com/lthiery/SPI-Py.git
cd ~/SPI-Py
sudo python setup.py install
cd ~
git clone https://github.com/chuypit/Snespi.git
cd Nespirc532
sudo sh ./setup.sh
 ``` 
