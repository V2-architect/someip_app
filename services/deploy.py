#!/usr/bin/python

import sys
import os

def main():
    items = os.popen("sudo docker exec someip_dev ls /home/jhshin/work/someip_dev/services").read().strip().split("\n")
    for i, item in enumerate(items, 1):
        print(f"[{i}] {item}")

    num = input("choose the number >> ")
    num = int(num)

    SERVICE_NAME = items[num-1]
    print(f"SERVICE_NAME: {SERVICE_NAME}")

    os.system(f"sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/{SERVICE_NAME}/release/ .")
    os.system(f"mv release/ {SERVICE_NAME}")
    os.system(f"sudo chown -R jhshin:jhshin {SERVICE_NAME}")

    '''
    print(f"sudo docker cp someip_dev:/home/jhshin/work/someip_dev/services/{SERVICE_NAME}/release/ .")
    print(f"mv release/ {SERVICE_NAME}")
    print(f"sudo chown -R jhshin:jhshin {SERVICE_NAME}")
    '''

if __name__ == "__main__":
    main()
