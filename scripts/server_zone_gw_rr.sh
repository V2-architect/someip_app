#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5

/root/someip_app/services/VehicleSpeed/run_server.sh udp 1 &

