#!/bin/bash

CURR_DATE=`date +%y%m%d-%H%M%S`
STATS_LOGFILE=docker_stats_${CURR_DATE}.log
echo "Start monitoring docker ecus to "${STATS_LOGFILE}
sudo docker stats `sudo docker ps | grep mn | awk '{print $NF}'` | tee $STATS_LOGFILE
