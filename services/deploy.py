#!/usr/bin/python

import sys
import os
import pdb

def deploy(SERVICE_NAME):
    if os.path.exists(SERVICE_NAME):
        os.system(f"rm -rf {SERVICE_NAME}")

    if SERVICE_NAME == "routingmanager":
        os.system(f"sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/{SERVICE_NAME}/ .")
        os.system(f"sudo chown -R jhshin:jhshin {SERVICE_NAME}")
    else:
        os.system(f"sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/{SERVICE_NAME}/release/ .")
        os.system(f"mv release/ {SERVICE_NAME}")
        os.system(f"sudo chown -R jhshin:jhshin {SERVICE_NAME}")

        '''
        print(f"sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/{SERVICE_NAME}/release/ .")
        print(f"mv release/ {SERVICE_NAME}")
        print(f"sudo chown -R jhshin:jhshin {SERVICE_NAME}")
        '''

def deploy_all():
    service_list = ["Collision", "Driving", "Intersection", "ObjectDetection", "SteeringWheel", \
                    "TrafficLight", "Transmission", "VehicleAccel", "VehicleLocation", \
                    "VehiclePose", "VehicleSpeed", "Logging",
                    "Audio", "Window_FL", "Window_FR", "Window_RL", "Window_RR"
                    ]

    for svc in service_list:
        print(f"Copy someip_dev/ to current directory ({svc})")
        deploy(svc)


def main():
    items = os.popen("sudo docker exec someip_dev ls /home/jhshin/work/someip_dev/services").read().strip().split("\n")
    for i, item in enumerate(items, 1):
        print(f"[{i}] {item}")

    num = input("choose the number >> ")
    num = int(num)

    SERVICE_NAME = items[num-1]
    print(f"SERVICE_NAME: {SERVICE_NAME}")

    deploy(SERVICE_NAME)

    # deploy time_interval txt
    os.system("python3 ./set_svc_event_interval.py")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'all':
        deploy_all()
    else:
        main()
