#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5

/root/someip_app/services/Collision/run_server.sh udp 1 &
sleep 1
