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

while True:
    print("===========")
    print("  StopOffer/StartOffer")
    print("===========")
    print("[0] Exit")
    print("[1] StopOffer (Location)")
    print("[2] StopOffer (TrafficLight)")
    print("[3] StopOffer (Intersection)")
    print("===========")
    print("[4] StartOffer (Location)")
    print("[5] StartOffer (TrafficLight)")
    print("[6] StartOffer (Intersection)")
    print("===========")
    try:
        num = int(input("# select the number >> "))
        base_cmd = "sudo docker exec -itd mn.telematics bash -c"
        if num == 0:
            print("Exit!")
            exit(0)
        if num in [1, 2, 3]:
            #packet = stopoffers[num-1]
            #sendp(packet, iface='veth0.3')
            if num == 1:
                someip_service_cmd = "pkill VehicleLocation"
            elif num == 2:
                someip_service_cmd = "pkill TrafficLight"
            elif num == 3:
                someip_service_cmd = "pkill Intersection"
        elif num in [4, 5, 6]:
            if num == 4:
                someip_service_cmd = "/root/someip_app/services/VehicleLocation/run_server.sh udp 1"
            elif num == 5:
                someip_service_cmd = "/root/someip_app/services/TrafficLight/run_server.sh udp 1"
            elif num == 6:
                someip_service_cmd = "/root/someip_app/services/Intersection/run_server.sh udp 1"

        print(f"{base_cmd} \"nohup {someip_service_cmd}\"")
        os.system(f"{base_cmd} \"nohup {someip_service_cmd}\"")
    except:
        print("Exit!")
        exit(0)


