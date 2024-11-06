#!/bin/bash

PCAP=/home/jhshin/K-city_2CAM_40m_5ms-02--anomaly.pcap

if [ "" = "x" ]; then
#### Application layer
# someipsd
tshark -r $PCAP -Y "someipsd" | awk '{print $1}' > Protocol_someipsd.txt

# someip and not someipsd
tshark -r $PCAP -Y "someip and not someipsd" | awk '{print $1}' > Protocol_someip.txt

# uds
tshark -r $PCAP -Y "uds" | awk '{print $1}' > Protocol_uds.txt

# doip and not uds
tshark -r $PCAP -Y "doip and not uds" | awk '{print $1}' > Protocol_doip.txt

# tftp
tshark -r $PCAP -Y "tftp" | awk '{print $1}' > Protocol_tftp.txt


#### Transport layer
# udp and not someip and not doip
tshark -r $PCAP -Y "udp and not someip and not doip and not tftp" | awk '{print $1}' > Protocol_udp.txt

# tcp and not someip and not doip
tshark -r $PCAP -Y "tcp and not someip and not doip and not tftp" | awk '{print $1}' > Protocol_tcp.txt
fi


#### Network layer
# ip and not udp and not tcp
tshark -r $PCAP -Y "(ip or ipv6) and not tcp and not udp" | awk '{print $1}' > Protocol_ip.txt

# arp
tshark -r $PCAP -Y "arp" | awk '{print $1}' > Protocol_arp.txt

