#!/bin/bash

/root/someip_app/services/routingmanager/run_routingd.sh &
sleep 5

/root/someip_app/services/Logging/run_server.sh tcp 1 &
sleep 1
