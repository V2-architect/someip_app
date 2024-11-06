#!/bin/bash

PCAP="$1"
FILTER="$2"

tshark -r "$PCAP" -Y "$FILTER" | awk '{print $1}'
