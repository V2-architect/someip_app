#!/bin/bash

HOSTNAME=$(hostname)


if [ "${HOSTNAME}" = "telematics" ]; then
    echo "Don't need to run. because it runs by containernet"
    /root/someip_app/ptp/ptp4l -S -i veth0.1 -f /root/someip_app/ptp/configs/automotive-master.cfg &
else
    echo "[${HOSTNAME}] Run PTP Slave"
    /root/someip_app/ptp/ptp4l -S -i veth0.1 -f /root/someip_app/ptp/configs/automotive-slave.cfg &
fi
