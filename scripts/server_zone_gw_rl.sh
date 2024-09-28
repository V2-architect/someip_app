#!/bin/bash

TARGET=$1

if [ -z "${TARGET}" -o "${TARGET}" = "routing" ];
then
    /root/someip_app/services/routingmanager/run_routingd.sh &
    sleep 5
fi

if [ -z "${TARGET}" -o "${TARGET}" = "service" ];
then
    /root/someip_app/services/VehiclePose/run_server.sh udp 1 &
fi

