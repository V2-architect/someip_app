from scapy.all import *
from scapy.contrib.automotive.someip import *

import pdb

pcaps = rdpcap("../../tmp.pcap")
someip_event = pcaps[0]
while True:
    someip_event[SOMEIP].payload = Raw(load=b'\x01' * 12)
    sendp(someip_event, iface='veth0.3')
    #sendp(someip_event, iface='veth0.3', loop=1, inter=0.01)
    pdb.set_trace()

print("end")


