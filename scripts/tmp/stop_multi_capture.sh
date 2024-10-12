#!/bin/bash

CURR_DATE=`date +%y%m%d-%H%M%S`
PCAP_FILE="inbound-${CURR_DATE}.pcap"
echo "CURR_DATE: "${CURR_DATE}

echo "merge all *.pcap files -> merged.pcap - start"
sudo mergecap -w merged.pcap \
    eth1.pcap \
    eth2.pcap \
    eth3.pcap \
    eth4.pcap \
    eth5.pcap \
    eth6.pcap \
    eth7.pcap \
    eth8.pcap
echo "merge all *.pcap files -> merged.pcap - end"

echo "rename merged.pcap to ${PCAP_FILE}"
mv merged.pcap ${PCAP_FILE}

sudo chown -R jhshin:jhshin *.pcap
