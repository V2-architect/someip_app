
from scapy.all import *
from scapy.contrib.automotive.someip import *

import pickle
import json
import pdb

class Replay:
    packet_series_count=50
    accel_interval = 0.02
    speed_interval = 0.02
    collision_interval = 0.02
    driving_interval = 0.01
    location_interval = 0.1
    transmission_interval = 0.02


class SOMEIP_MSG:
    OFFER=1
    SUBSCRIBE=2
    SUBSCRIBE_ACK=3
    STOP_OFFER=4
    STOP_SUBSCRIBE=5

class SOMEIP:
    def __init__(self, dump_path):
        self.dump_path = dump_path
        self.msg_dump_map = {
            SOMEIP_MSG.OFFER: 'someipsd_offer.pkl',
        }
        self.service_info = json.loads(open('../someip_service_spec.json').read())

    def load_someip_packet(self, msg_type):
        dump_filename = self.msg_dump_map[msg_type]
        with open(os.path.join(self.dump_path, dump_filename), 'rb') as f:
            someip_packet = pickle.load(f)
        return someip_packet

    def apply_service_info(self, service, someip_packet):
        pdb.set_trace()
        # someip_packet
        return someip_packet

someip = SOMEIP('/home/jhshin/work/someip_app/scripts/attacker/someip_dumps')

def update_udp_chksum(packet):
    packet[IP].chksum = None
    packet[UDP].chksum = None
    packet = packet.__class__(bytes(packet))
    return packet

def update_tcp_chksum(packet):
    packet[IP].chksum = None
    packet[TCP].chksum = None
    packet = packet.__class__(bytes(packet))
    return packet

def update_ip_chksum(packet):
    packet[IP].chksum = None
    packet = packet.__class__(bytes(packet))
    return packet

def get_someip_service_info():
    return service_info

def get_someip_packet(service, someip_msg):
    global someip
    someip_packet = someip.load_someip_packet(someip_msg)
    someip_packet = someip.apply_service_info(service, someip_packet)
    return someip_packet


