#!/bin/bash
# RetroPi Control Install
CURRENT=`pwd`
PARENT=`dirname $CURRENT`
SCRIPTS='/home/pi/scripts'
#start install
echo "**************************************"
echo "Installing Snes pi nfc"
echo "**************************************"
echo -n "**************************************"
echo -n "demo instalacion snes pi!"
echo "**************************************"
echo -n "Would you like to continue with the installation? (y/n): "
read REPLY
if [ $REPLY = "y" ] || [ $REPLY = "Y" ]
then
    echo "**************************************"
    echo "Installing NFC "
    apt-get install python2.7-dev
    git clone https://github.com/lthiery/SPI-Py.git
    cd SPI-Py
    python setup.py install
    cd ../
    #update startup
    echo "Updating Startup Commands............."
    sed -i '\:emulationstation #auto:d' /opt/retropie/configs/all/autostart.sh
    sed -i '\:emulationstation:d' /opt/retropie/configs/all/autostart.sh
    sed -i '\:python /home/pi/Snespi/romv4.py 2>&1:d' /opt/retropie/configs/all/autostart.sh
    echo 'python /home/pi/Snespi/romv4.py 2>&1' >> /opt/retropie/configs/all/autostart.sh
    echo 'emulationstation' >> /opt/retropie/configs/all/autostart.sh
    rm -R /home/pi/RetroPie/retropiemenu/rom.sh
    echo 'python /home/pi/Snespi/consola.py 2>&1&' > /home/pi/RetroPie/retropiemenu/rom.sh
    chmod -R 7777 /home/pi/RetroPie/retropiemenu/rom.sh
    echo "Installation Complete................."
    echo -n "You must reboot for changes to take effect, reboot now? (y/n): "
    read REPLY
    if [ $REPLY = "y" ] || [ $REPLY = "Y" ]
    then
        sleep 3
    fi
fi

cd /etc/
RC=rc.local

if grep -q "sudo python \/home\/pi\/Snespi\/Reset.py \&" "$RC";
	then
		echo "File /etc/rc.local already configured. Doing nothing."
	else
		sed -i -e "s/^exit 0/sudo python python \/home\/pi\/Snespi\/Reset.py \&\n&/g" "$RC"
		echo "File /etc/rc.local configured."
fi

echo "Will now reboot after 3 seconds."
sleep 3
sudo reboot
#end