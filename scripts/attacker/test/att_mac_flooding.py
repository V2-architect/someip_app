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
    src_ip = random_ip()
    dst_ip = random_ip()

    src_mac = random_mac()
    dst_mac = random_mac()

    #packet = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / ICMP()
    packet = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / Padding(b'\x00' * 22)

    packet = update_ip_chksum(packet)
    sendp(packet, iface='veth0.3')

    time.sleep(1)

print("end")


