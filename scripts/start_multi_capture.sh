#!/bin/bash

CURR_DATE=`date +%y%m%d-%H%M%S`
PCAP_FILE="inbound-${CURR_DATE}.pcap"
echo "CURR_DATE: "${CURR_DATE}

sudo tcpdump -i s1-eth1 ether src 00:00:00:00:00:01 -w eth1.pcap &
sudo tcpdump -i s1-eth2 ether src 00:00:00:00:00:02 -w eth2.pcap &
sudo tcpdump -i s1-eth3 ether src 00:00:00:00:00:03 -w eth3.pcap &
sudo tcpdump -i s1-eth4 ether src 00:00:00:00:00:04 -w eth4.pcap &
sudo tcpdump -i s1-eth5 ether src 00:00:00:00:00:05 -w eth5.pcap &
sudo tcpdump -i s1-eth6 ether src 00:00:00:00:00:06 -w eth6.pcap &
sudo tcpdump -i s1-eth7 ether src 00:00:00:00:00:07 -w eth7.pcap &
sudo tcpdump -i s1-eth8 ether src 00:00:00:00:00:08 -w eth8.pcap &

