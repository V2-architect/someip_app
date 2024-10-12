#!/bin/bash

python3 ./run_ecu_r.py
sleep 1
python3 ./run_ecu_s.py
sleep 1
python3 ./run_ecu_c.py
sleep 1
