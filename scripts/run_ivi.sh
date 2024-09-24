#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5
/root/someip_app/services/SteeringWheel/run_client.sh udp 2 &

