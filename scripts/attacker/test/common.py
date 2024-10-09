
from scapy.all import *

def update_udp_chksum(packet):
    packet[IP].chksum = None
    packet[UDP].chksum = None
    packet = packet.__class__(bytes(packet))
    return packet

def update_ip_chksum(packet):
    packet[IP].chksum = None
    packet = packet.__class__(bytes(packet))
    return packet

