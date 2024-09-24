#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5

/root/someip_app/services/VehicleAccel/run_server.sh udp 1 &
/root/someip_app/services/Driving/run_server.sh udp 1 &

