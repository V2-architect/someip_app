#!/bin/bash

HOSTNAME=$(hostname)

# TARGET: routing, service
TARGET=$1

/root/someip_app/scripts/server_${HOSTNAME}.sh ${TARGET}
