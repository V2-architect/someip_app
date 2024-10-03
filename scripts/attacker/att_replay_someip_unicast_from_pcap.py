from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import struct
import pdb
import time

pcaps = rdpcap("../../someip_unicast.pcap")
packet_vlan = pcaps[0]

while True:
    accel_x, accel_y, accel_z = 10.0, 20.0, 30.0
    data = struct.pack('>fff', accel_x, accel_y, accel_z)
    packet_vlan[SOMEIP].payload = Raw(load=data)

    #pkt = Ether(src=packet[Ether].src, dst=packet[Ether].dst) / packet[IP] / packet[IP].payload
    packet = Ether(src=packet_vlan[Ether].src, dst=packet_vlan[Ether].dst) / packet_vlan[IP]

    packet = update_udp_chksum(packet)
    sendp(packet, iface='veth0.3')
    print("send!")
    time.sleep(1)

print("end")


