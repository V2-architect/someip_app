#!/bin/bash

CURR_DATE=`date +%y%m%d-%H%M%S`
STATS_FILE="docker_stats-${CURR_DATE}.txt"
echo "CURR_DATE: "${CURR_DATE}

sudo docker stats $(sudo docker ps --all | grep mn. | awk '{print $NF}') | tee ${STATS_FILE}
