#!/bin/bash


VERSION=$1
if [ $VERSION = "3.0" ]; then
/root/someip_app/ptp/ptp4l_${VERSION} -m -S -i veth0.1 -f /root/someip_app/ptp/configs_3.0/automotive-master.cfg &
else
/root/someip_app/ptp/ptp4l_${VERSION} -m -S -i veth0.1 -f /root/someip_app/ptp/configs/automotive-master.cfg &
fi
