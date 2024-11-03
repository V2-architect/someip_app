from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
from common import update_ip_chksum
import random
import pdb

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

while True:
    packets = []
    weight = random.uniform(1, 3)
    packet_count = int(500*weight)
    interval = random.uniform(1, 3) * 0.001
    print(f"packet count: {packet_count}")
    print(f"sending interval: {interval*1000}ms")

    for i in range(packet_count):
        src_ip = random_ip()
        dst_ip = random_ip()

        src_mac = random_mac()
        dst_mac = random_mac()

        #packet = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / ICMP()
        packet = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / Padding(b'\x00' * 22)
        packet[IP].ttl = 6

        packet = update_ip_chksum(packet)

        packets.append(packet)

        if i % 200 == 0:
            print(f"progress: {i}/{packet_count}")

    sendp(packets, iface='veth0.3', inter=interval)
    #delay = random.uniform(1, 2)
    #print(f"sleep {delay}s")
    #time.sleep(delay)

print("end")


