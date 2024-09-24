#!/bin/bash

/root/someip_app/services/Collision/run_client.sh udp 1 &
sleep 1
/root/someip_app/services/Transmission/run_client.sh udp 1 &
sleep 1
/root/someip_app/services/VehicleSpeed/run_client.sh udp 1 &
sleep 1
/root/someip_app/services/VehicleLocation/run_client.sh udp 1 &
sleep 1
