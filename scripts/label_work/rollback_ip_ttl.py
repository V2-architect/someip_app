from scapy.all import PcapNgReader
from scapy.all import IP
from scapy.all import rdpcap
from scapy.all import wrpcap
import pdb
import os
import time

in_file_path = 'K-city_2CAM_40m_5ms-02--anomaly.pcap'
out_file_path = 'K-city_2CAM_40m_5ms-02--anomaly--orig.pcap'

def read_generator():
    with PcapNgReader(in_file_path) as pcapng_reader:
        for packet in pcapng_reader:
            try:
                if packet.haslayer(IP):
                    if packet[IP].ttl in [4, 5]:
                        packet[IP].ttl = 1
                    elif packet[IP].ttl == 6:
                        packet[IP].ttl = 64
                yield packet
            except:
                continue

#def save_packet(pkt):
#    wrpcap(out_file_path, [pkt])  # PCAP 파일로 저장

packets = []
for i, pkt in enumerate(read_generator()):
    packets.append(pkt)
    if i%10000 == 0:
        print(f"counter: {i}")
        wrpcap(out_file_path, packets, append=True)  # PCAP 파일로 저장
        packets = []

print("save final packets...")
wrpcap(out_file_path, packets, append=True)  # PCAP 파일로 저장


'''

pcaps = rdpcap(file_path)
pdb.set_trace()

packets = []
for i, packet in enumerate(pcaps):
    if packet[IP].ttl in [4, 5]:
        packet[IP].ttl = 1
    elif packet[IP].ttl == 6:
        packet[IP].ttl = 64
    packets.append(packet)

    if i%1000 == 0:
        print(f"counter: {i}")

wrpcap(out_file_path, packets) 

'''


