#!/bin/bash

sudo ovs-ofctl -O Openflow13 del-flows s1 'ip,in_port="s1-eth1",nw_dst=239.10.0.1'
sudo ovs-ofctl -O Openflow13 del-flows s1 'ip,in_port="s1-eth2",nw_dst=239.10.0.1'
