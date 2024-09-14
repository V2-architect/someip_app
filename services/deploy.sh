#!/bin/bash

if [ -z "$1" ]; then
    echo "$ deploy.sh <SERVICE_NAME>"
    echo "ex) $ deploy.sh VehicleAccel"
    exit -1
fi
SERVICE_NAME=$1

sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/${SERVICE_NAME}/release/ .
mv release/ ${SERVICE_NAME}
sudo chown -R jhshin:jhshin ${SERVICE_NAME}
