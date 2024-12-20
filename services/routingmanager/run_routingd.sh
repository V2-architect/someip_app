#!/bin/bash -e

# leave as before
#if [ -z "$1" ]; then
#    echo "[Error] input the argument like below"
#    echo "  $ $0 [<delay(second),default(5s)>]
#    echo "  $ $0 5
#    exit -1
#fi

# set curr_path to script_path
CURR_SH_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ${CURR_SH_PATH}

LAUNCH_DELAY=$1
if [ -z "$1" ]; then
    LAUNCH_DELAY=5
fi
echo "LAUNCH_DELAY: "${LAUNCH_DELAY}
sleep ${LAUNCH_DELAY}


# get data from user input
HOSTNAME=$(hostname)
SOMEIP_HOST_IP=`cat host_ip.txt | grep $(hostname) | awk -F: '{print $2}'`

DEV_MODE="n"
if [ "$(echo $(pwd) | grep someip_dev)" != "" ]; then
    DEV_MODE="y"
fi

# get SOME/IP service runtime information from someip_service.prop
SERVICE_NAME=`cat someip_service.prop | grep SERVICE_NAME | awk -F= '{print $2}'`
MULTICAST_IP=`cat someip_service.prop | grep MULTICAST_IP | awk -F= '{print $2}'`

# get env variable at runtime
GIT_PROJECT_ROOT=`./get_git_path.py ${CURR_SH_PATH}`
BOOST_LIBRARY_PATH=${GIT_PROJECT_ROOT}/dependencies/boost_1_64_0/lib
CAPICXX_CORE_PATH=${GIT_PROJECT_ROOT}/dependencies/capicxx-core-runtime_3.2.0/lib
CAPICXX_SOMEIP_PATH=${GIT_PROJECT_ROOT}/dependencies/capicxx-someip-runtime_3.2.0/lib
VSOMEIP_PATH=${GIT_PROJECT_ROOT}/dependencies/vsomeip_3.3.0/lib
APP_LD_LIBRARY_PATH=${BOOST_LIBRARY_PATH}:${CAPICXX_CORE_PATH}:${CAPICXX_SOMEIP_PATH}:${VSOMEIP_PATH}

APP_ROOT=${GIT_PROJECT_ROOT}/services/${SERVICE_NAME}
if [ "${DEV_MODE}" == "y" ]; then
    APP_ROOT=${GIT_PROJECT_ROOT}/services/${SERVICE_NAME}/build
fi

# check prerequisite
./pre_check.py ${APP_LD_LIBRARY_PATH}

CONF_FILE_TEMPLATE=${APP_ROOT}/routingmanagerd.json.in
CONF_FILE=${APP_ROOT}/routingmanagerd-${HOSTNAME}.json
CONF_FILE_TMP=${APP_ROOT}/routingmanagerd-${HOSTNAME}.json.tmp

echo "==========================================="
echo "============= SOME/IP Client =============="
echo "==========================================="

echo "GIT_PROJECT_ROOT  : "${GIT_PROJECT_ROOT}
echo "APP_ROOT          : "${APP_ROOT}
echo "SOMEIP_HOST_IP    : "${SOMEIP_HOST_IP}
echo "MULTICAST_IP      : "${MULTICAST_IP}
echo "LD_LIBRARY_PATH   : "${APP_LD_LIBRARY_PATH}

sed "s/@SOMEIP_HOST_IP@/${SOMEIP_HOST_IP}/g" $CONF_FILE_TEMPLATE > $CONF_FILE
LOGGING_FILEPATH="/root/someip_app/logs/${HOSTNAME}-${SERVICE_NAME}.log"
echo "LOGGING_FILEPATH: "${LOGGING_FILEPATH}
mv ${CONF_FILE} ${CONF_FILE_TMP}
sed "s,@LOGGING_FILEPATH@,${LOGGING_FILEPATH},g" ${CONF_FILE_TMP} > ${CONF_FILE}
rm ${CONF_FILE_TMP}

LD_LIBRARY_PATH=$APP_LD_LIBRARY_PATH \
    VSOMEIP_CONFIGURATION=$CONF_FILE \
    ${APP_ROOT}/routingmanagerd


