# PyChromeCastControl
PyChromeCastControl is a hacking tool used for enumeration and information gathering purposes on ChromeCast devices.

## Features:
With PyChromeCastControl, you can:
* Scan ChromeCast devices on the network
* Enumerate information, such as certificate, gateway information, MAC address, WiFi networks etc.
* Enumerate WiFi networks in range of the ChromeCast device
* Reboot and reset the machine
* Get timezone and locale information
And plenty more!

## Installation (beginner):
    git clone https://github.com/MaliciouZzHD/PyChromeCastControl
    cd PyChromeCastControl
    chmod +x ChromeCastControl
    ./ChromeCastControl
    
## Installation (advanced):
    git clone https://github.com/MaliciouZzHD/PyChromeCastControl
    cd PyChromeCastControl
    chmod +x ChromeCastControl
    sudo ln -s $(pwd)/ChromeCastControl /sbin/pychromecastcontrol
    cd ~
    pychromecastcontrol
