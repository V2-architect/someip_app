import os

svc_event_interval = open("svc_event_interval.txt").read().strip().split("\n")

for info in svc_event_interval:
    svc, event, interval = info.split(":")

    # create file(event_interval.txt) under service
    interval_us = int(interval) * 1000
    print(f"echo {interval_us} > {svc}/{event}_interval.txt")
    os.system(f"echo {interval_us} > {svc}/{event}_interval.txt")
