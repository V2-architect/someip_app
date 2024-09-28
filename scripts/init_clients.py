import os
import time

vECUs = [
    "mn.ivi",
    "mn.cluster",
    "mn.adas",
    "mn.telematics"
]


t_s = time.time()

for vECU in vECUs:
    os.system(f"sudo docker exec -itd {vECU} bash -c \"nohup /root/someip_app/scripts/cc.sh\"")
    print(f"[{vECU}] SOME/IP clients init done")

time.sleep(1)

t_e = time.time()
print(f"{format(t_e - t_s, '.3f')}")
