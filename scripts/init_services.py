
import os
import time
import sys
import pdb

target = ""
if len(sys.argv) > 1:
    target = sys.argv[1]

if bool(target) and target not in ["routing", "service"]:
    print("target should be routing, service")
    exit(-1)

t_s = time.time()

vECUs = [
    "mn.zone_gw_fl",
    "mn.zone_gw_fr",
    "mn.zone_gw_rl",
    "mn.zone_gw_rr",
    "mn.ivi",
    "mn.cluster",
    "mn.adas",
    "mn.telematics"
]

for vECU in vECUs:
    os.system(f"sudo docker exec -itd {vECU} bash -c \"nohup /root/someip_app/scripts/ss.sh {target}\"")
    print(f"[{vECU}] SOME/IP {target} init done")

if target == "routing":
    time.sleep(5)
if target == "service":
    time.sleep(1)

t_e = time.time()
print(f"{format(t_e - t_s, '.3f')}")
