from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

#client3_mac = getmacbyip(client3_ip)
#print(f"client3_mac: {client3_mac}")

def process_packet(packet):
    print("hit!")
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SOMEIP):
            print("someip!")
            pdb.set_trace()
            #packet[IP].ttl = 99
            #sendp(packet, iface='telematics-eth0')
            #print("send packet")
            #pdb.set_trace()
            #print(f"Modified Payload sent as: {modified_payload}")

sniff(filter=f"udp and src host 10.0.0.2", iface='telematics-eth0', prn=process_packet)

