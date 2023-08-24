# PyWake

A simple Python program that can wake up devices using Wake On Lan.

    usage: PyWake [-h] [-i INTERFACE] [-b] mac_address
    
    A simple Python program that can wake up devices using Wake On Lan.
    
    positional arguments:
      mac_address           MAC address of the device you wish to wake. ':' and
                            '-' supported as separators
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INTERFACE, --interface INTERFACE
      -b, --broadcast       Send packet to broadcast instead
