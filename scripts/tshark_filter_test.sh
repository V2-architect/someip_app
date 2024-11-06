#!/bin/bash

PCAP=/home/jhshin/K-city_2CAM_40m_5ms-02--anomaly.pcap

echo "TFTP"
time tshark -r $PCAP -Y "tftp" | awk '{print $1}' | wc -l

echo "DOIP"
time tshark -r $PCAP -Y "doip" | awk '{print $1}' | wc -l

echo "UDS"
time tshark -r $PCAP -Y "uds" | awk '{print $1}' | wc -l

echo "someipsd"
time tshark -r $PCAP -Y "someipsd" | awk '{print $1}' | wc -l

echo "someip and not someipsd"
time tshark -r $PCAP -Y "someip and not someipsd" | awk '{print $1}' | wc -l

echo "UDP"
time tshark -r $PCAP -Y "udp" | awk '{print $1}' | wc -l

echo "TCP"
time tshark -r $PCAP -Y "tcp" | awk '{print $1}' | wc -l

