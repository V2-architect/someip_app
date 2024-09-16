from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

#client3_mac = getmacbyip(client3_ip)
#print(f"client3_mac: {client3_mac}")

def process_packet(packet):
    if packet.haslayer(IP):
        if packet.haslayer(UDP):
            print("ptp!")
            sendp(packet, iface='telematics-eth0', loop=1, inter=0.01)
            # modify Offer to StopOffer by setting ttl to zero

filter = "udp and (src port 319 and dst port 319)"
#filter = "dst host 224.0.1.129"
sniff(filter=filter, iface='telematics-eth0', prn=process_packet)

