#!/bin/bash

sudo ovs-ofctl -O Openflow13 add-flow s1 'ip,in_port=1,nw_dst=239.10.0.1,actions=output:2'
sudo ovs-ofctl -O Openflow13 add-flow s1 'ip,in_port=2,nw_dst=239.10.0.1,actions=output:1'
