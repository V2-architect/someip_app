#!/bin/bash

HOSTNAME=$(hostname)
python3 /root/someip_app/scripts/client.py ${HOSTNAME}
