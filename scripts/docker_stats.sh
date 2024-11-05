#!/bin/bash


# set sh path & chdir to docker_stats
CURR_SH_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${CURR_SH_PATH}
DOCKER_STATS_LOG_PATH=${CURR_SH_PATH}/docker_stats
mkdir -p ${DOCKER_STATS_LOG_PATH}
cd ${DOCKER_STATS_LOG_PATH}

# set env variables
START_TIMESTAMP=`date +%y%m%d-%H%M%S`
PREFIX="docker_stats-${START_TIMESTAMP}"
STATS_TXT_FILE="${PREFIX}.txt"
STATS_JSON_FILE="${PREFIX}.json"
STATS_BIN_FILE="${PREFIX}.bin"
vECU_NUMBER=8

# set trap function (Ctrl+C)
function handle_sigint {
    END_TIMESTAMP=`date +%y%m%d-%H%M%S`

    STATS_TIME_INFO="docker_stats_time-${START_TIMESTAMP}.txt"
    echo ${START_TIMESTAMP} >> ${STATS_TIME_INFO}
    echo ${END_TIMESTAMP} >> ${STATS_TIME_INFO}

    # in:${STATS_TXT_FILE}, out: ${STATS_JSON_FILE}, ${STATS_BIN_FILE}
    echo "Parse Docker Stat Log & gen output(*.json, *.bin)"
    echo " * json: "${STATS_JSON_FILE}
    echo " * bin:  "${STATS_BIN_FILE}
    echo " * # of vECU numbers: "${vECU_NUMBER}

    cd ${CURR_SH_PATH}
    python3 convert_stats_log.py \
        -l ${DOCKER_STATS_LOG_PATH}/${STATS_TXT_FILE} \
        -t ${DOCKER_STATS_LOG_PATH}/${STATS_TIME_INFO} \
        -j ${DOCKER_STATS_LOG_PATH}/${STATS_JSON_FILE} \
        -b ${DOCKER_STATS_LOG_PATH}/${STATS_BIN_FILE} \
        -n ${vECU_NUMBER}
    #python3 convert_stats_log.py /home/jhshin/logs_20s_001.txt timeinfo.txt ${STATS_JSON_FILE} ${STATS_BIN_FILE}
}
trap 'handle_sigint' SIGINT

# start logging of docker_stats
echo "START_TIMESTAMP: "${START_TIMESTAMP}
sudo docker stats --format json $(sudo docker ps --all | grep mn. | awk '{print $NF}') 2>&1 | tee ${STATS_TXT_FILE}

