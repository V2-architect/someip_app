#!/bin/bash

if [ -z "$1" ]; then
    echo "./add_vlan.sh <vlan_id>"
    exit -1
fi

HOSTNAME=$(hostname)
if [ ${HOSTNAME} == "zone_gw_fl" ]; then
    ECU_ID=1
fi
if [ ${HOSTNAME} == "zone_gw_fr" ]; then
    ECU_ID=2
fi
if [ ${HOSTNAME} == "zone_gw_rl" ]; then
    ECU_ID=3
fi
if [ ${HOSTNAME} == "zone_gw_rr" ]; then
    ECU_ID=4
fi
if [ ${HOSTNAME} == "ivi" ]; then
    ECU_ID=5
fi
if [ ${HOSTNAME} == "cluster" ]; then
    ECU_ID=6
fi
if [ ${HOSTNAME} == "adas" ]; then
    ECU_ID=7
fi
if [ ${HOSTNAME} == "telematics" ]; then
    ECU_ID=8
fi

VLAN_ID=$1

ip link add link $(hostname)-eth0 name veth0.${VLAN_ID} type vlan id ${VLAN_ID}
#ip link set dev veth0.${VLAN_ID} address 00:00:00:00:0${VLAN_ID}:0${ECU_ID}
ip addr add 10.0.${VLAN_ID}.${ECU_ID}/24 dev veth0.${VLAN_ID}
ip link set up veth0.${VLAN_ID}

#ip neigh add 192.168.10.2 lladdr 00:11:22:33:44:55 dev eth0.10 nud permanent
#arp -s 192.168.10.2 00:11:22:33:44:55 -i eth0.10
#arp -s 10.0.${VLAN_ID}.${ECU_ID} 00:00:00:00:00:0${ECU_ID} -i veth0.${VLAN_ID}
