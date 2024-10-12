
import argparse
import json
import sys
import os
import random
import time


def main():
    hostname = os.environ.get("HOSTNAME")
    f_path = "/root/someip_app/scripts/service-vecu.json"
    config = json.loads(open(f_path).read())
    common_cfg = config["common"]

    # run routingmanager processes
    app_name = "routingmanager"
    random_interval = random.uniform(common_cfg["run_r_interval_min"], common_cfg["run_r_interval_max"])
    cmd = f"/root/someip_app/services/{app_name}/run_routingd.sh {random_interval} &"
    print(f"Random Interval: {random_interval}")
    print(f"Run cmd: {cmd}")
    os.system(cmd)


if __name__ == "__main__":
    main()

