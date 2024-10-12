
import os
import time
import sys
import pdb
import random
import json

t_s = time.time()

config = json.loads(open("service-vecu.json").read())
for ecu_name in config['ecus']:
    os.system(f"sudo docker exec -itd mn.{ecu_name} bash -c \"nohup /root/someip_app/scripts/s.sh\"")
    print(f"[mn.{ecu_name}] SOME/IP service init done")
    time.sleep(0.5)

time.sleep(1)

t_e = time.time()
print(f"{format(t_e - t_s, '.3f')}")

