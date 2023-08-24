import socket
import re
import argparse
from codecs import decode
import binascii


class MacLength(argparse.Action):
    def __call__(self, parser, namespace, mac_input, option_string=None):
        mac = re.sub(r'\W+', '', mac_input) # Strip non alphanumeric characters
        if len(mac) != 12:
            parser.error(
                "The MAC address entered is not 12 characters long".format(option_string))
            
        setattr(namespace, self.dest, mac_input)

parser = argparse.ArgumentParser(
    prog="PyWake",
    description="Python program to wake a device using Wake On Lan",
)
parser.add_argument (
    "mac_address", help="MAC address of the device you wish to wake. ':' and '-' supported as separators", action=MacLength)
parser.add_argument("-i", "--interface", default="eth0", type=str)
parser.add_argument("-b", "--broadcast", help="Send packet to broadcast instead", action="store_true")
args = parser.parse_args()


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind((args.interface, 0))

mac = re.sub(r'\W+', '', args.mac_address)  # Strip non alphanumeric characters
MAC_to_wake = mac                           # Device to wake  
if args.broadcast:                          # If broadcast is enabled send to the broadcast
    MAC_destination = "ff"*6
else:
    MAC_destination = mac
MAC_source = "00"*6                         # MAC Address Source
Packet_type = "0842"                        # Protocol-Type: WOL
Sync_stream = "ff"*6                        # Sync stream

ethernet = MAC_destination
ethernet += MAC_source
ethernet += Packet_type

wake_on_lan = Sync_stream
wake_on_lan += MAC_to_wake*16

packet = ethernet + wake_on_lan
try:
    s.send(decode(packet, 'hex_codec'))
    print('Sent a package to', args.mac_address)
except binascii.Error:
    print("MAC address is invalid")
