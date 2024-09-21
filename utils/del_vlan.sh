#!/bin/bash

if [ -z "$1" ]; then
    echo "./del_vlan.sh <interface>"
    exit -1
fi

ip link delete $1
