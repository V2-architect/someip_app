#!/bin/bash


/root/someip_app/services/ObjectDetection/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/VehicleLocation/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/VehicleSpeed/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Transmission/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Collision/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Audio/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Window_FL/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Window_FR/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Window_RL/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))
/root/someip_app/services/Window_RR/run_client.sh udp 1 &
sleep $((RANDOM % 5 + 1))


##/root/someip_app/services/Hvac/run_client.sh udp 1 &
##sleep 1
