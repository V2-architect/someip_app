#!/bin/bash

/root/someip_app/services/SteeringWheel/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/TrafficLight/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Intersection/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/VehiclePose/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/VehicleAccel/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Driving/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/VehicleSpeed/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Transmission/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
