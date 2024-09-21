#!/bin/bash

if [ -z "$1" -o -z "$2" ]; then
    echo "./add_route.sh <multicast_ip> <vlan_id>"
    exit -1
fi

MULTICAST_IP=$1
VLAN_ID=$2

route add -n ${MULTICAST_IP} veth0.${VLAN_ID}
