import os

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
    print(f"sudo docker exec -it {vECU} bash -c /root/someip_app/scripts/kill_someip.sh")
    os.system(f"sudo docker exec -it {vECU} bash -c /root/someip_app/scripts/kill_someip.sh")
