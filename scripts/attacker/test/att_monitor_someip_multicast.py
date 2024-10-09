from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import pdb
import time
from datetime import datetime
import struct

prev = 0
def process_packet(packet):
    global prev

    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SOMEIP):
            if prev == 0:
                prev = datetime.now()
            curr = datetime.now()
            print(curr-prev)
            prev = curr

filter = "udp and src host 10.0.3.2 and src port 31002"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

