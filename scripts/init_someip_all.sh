#!/bin/bash

python3 ./init_services.py routing
sleep 1
python3 ./init_services.py service
sleep 1
python3 ./init_clients.py
sleep 1
