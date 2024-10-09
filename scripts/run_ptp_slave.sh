#!/bin/bash


VERSION=$1
/root/someip_app/ptp/ptp4l_${VERSION} -s -m -S -i veth0.1 -f /root/someip_app/ptp/configs/automotive-slave.cfg &
