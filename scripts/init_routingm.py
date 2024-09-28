
import os
import time

t_s = time.time()
os.system("sudo docker exec -itd mn.zone_gw_fl bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.zone_gw_fl] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.zone_gw_fr bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.zone_gw_fr] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.zone_gw_rl bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.zone_gw_rl] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.zone_gw_rr bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.zone_gw_rr] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.ivi        bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.ivi] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.cluster    bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.cluster] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.adas       bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.adas] SOME/IP routingm, service init done")

os.system("sudo docker exec -itd mn.telematics bash -c \"nohup /root/someip_app/scripts/ss.sh\"")
print("[mn.telematics] SOME/IP routingm, service init done")

time.sleep(5)

t_e = time.time()
print(f"{format(t_e - t_s, '.3f')}")
