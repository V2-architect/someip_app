#!/bin/bash

CURR_DATE=`date +%y%m%d-%H%M%S`
PCAP_FILE="inbound-${CURR_DATE}.pcap"
echo "CURR_DATE: "${CURR_DATE}

echo 'check sudo permission to run this script'
sudo echo ' '

sudo tcpdump -i s1-eth1 ether src 00:00:00:00:00:01 -w eth1.pcap &
sudo tcpdump -i s1-eth2 ether src 00:00:00:00:00:02 -w eth2.pcap &
sudo tcpdump -i s1-eth3 ether src 00:00:00:00:00:03 -w eth3.pcap &
sudo tcpdump -i s1-eth4 ether src 00:00:00:00:00:04 -w eth4.pcap &
sudo tcpdump -i s1-eth5 ether src 00:00:00:00:00:05 -w eth5.pcap &
sudo tcpdump -i s1-eth6 ether src 00:00:00:00:00:06 -w eth6.pcap &
sudo tcpdump -i s1-eth7 ether src 00:00:00:00:00:07 -w eth7.pcap &
sudo tcpdump -i s1-eth8 ether src 00:00:00:00:00:08 -w eth8.pcap &
sudo tcpdump -i s1-eth8 'ip[8] == 6'                -w eth8_mac_flooding.pcap &

#sudo tshark -i s1-eth1 -t ad -f "inbound" -w /tmp/eth1.pcap &
#sudo tshark -i s1-eth2 -t ad -f "inbound" -w /tmp/eth2.pcap &
#sudo tshark -i s1-eth3 -t ad -f "inbound" -w /tmp/eth3.pcap &
#sudo tshark -i s1-eth4 -t ad -f "inbound" -w /tmp/eth4.pcap &
#sudo tshark -i s1-eth5 -t ad -f "inbound" -w /tmp/eth5.pcap &
#sudo tshark -i s1-eth6 -t ad -f "inbound" -w /tmp/eth6.pcap &
#sudo tshark -i s1-eth7 -t ad -f "inbound" -w /tmp/eth7.pcap &
#sudo tshark -i s1-eth8 -t ad -f "inbound" -w /tmp/eth8.pcap &

