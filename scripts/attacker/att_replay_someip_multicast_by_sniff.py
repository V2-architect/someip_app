from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import pdb
import time
import struct

accel_x, accel_y, accel_z = 1.0, 2.0, 3.0
def process_packet(packet):
    global accel_x
    global accel_y
    global accel_z

    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SOMEIP):
            print("someip - vehicle_accel!")
            #packet[SOMEIP].session_id += 1
            for _ in range(3):
                data = struct.pack('>fff', accel_x, accel_y, accel_z)
                packet[SOMEIP].payload = Raw(load=data)
                packet = update_udp_chksum(packet)
                #sendp(packet, iface='veth0.3', loop=1, inter=0.001)
                sendp(packet, iface='veth0.3')
                accel_x += 1
                accel_y += 1
                accel_z += 1


filter = "udp and src host 10.0.3.2 and src port 31002"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

