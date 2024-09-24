#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5

/root/someip_app/services/TrafficLight/run_server.sh udp 1 &
sleep 1
/root/someip_app/services/Intersection/run_server.sh udp 1 &
sleep 1
/root/someip_app/services/VehicleLocation/run_server.sh udp 1 &
sleep 1

