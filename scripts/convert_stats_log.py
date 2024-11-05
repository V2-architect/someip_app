
import time
import sys
import copy
import os
import json
import pdb
import re
import pickle
import numpy as np
import argparse
from datetime import datetime
from datetime import timedelta

def check_input_files(docker_stats_log_txt, stats_timeinfo):
    if not os.path.exists(docker_stats_log_txt):
        print(f"[Error] {docker_stats_log_txt} NOT found!")
        exit(-1)

    if not os.path.exists(stats_timeinfo):
        print(f"[Error] {stats_timeinfo} NOT found!")
        exit(-1)


def get_log_contents(docker_stats_log_txt):
    return open(docker_stats_log_txt).read().strip().replace('\x1b[2J\x1b[H', '').split('\n')


def get_timestamp_info(stats_timeinfo, chunk):
    timeinfo = open(stats_timeinfo).read().strip().split('\n')
    timestamp_s, timestamp_e = timeinfo
    timestamp_s = datetime.strptime(timestamp_s, "%y%m%d-%H%M%S")
    timestamp_e = datetime.strptime(timestamp_e, "%y%m%d-%H%M%S")

    # actual logging is started after 2.5s
    timestamp_s = timestamp_s + timedelta(seconds=2.5)
    time_interval = (timestamp_e - timestamp_s) / chunk

    return timestamp_s, time_interval


class Timestamp(json.JSONEncoder):

    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __add__(self, ts):
        return Timestamp(self.timestamp + ts)

    def __sub__(self, ts):
        return Timestamp(self.timestamp - ts)

    def __str__(self):
        return self.timestamp.isoformat()

    def __repr__(self):
        return self.timestamp.isoformat()

    def default(self, obj):
        return self.__str__()


def dump(stat_dataset, filename):
    for stat in stat_dataset:
        stat['timestamp'] = str(stat['timestamp'])

    with open(filename, "w") as f:
        f.write(json.dumps(stat_dataset, indent=4))


def get_digit(target_string):
    return re.findall(r"[\d.]+", target_string)[0]

def make_json(ecu_group, timestamp):
    ecu_group_stat = {}

    for ecu in ecu_group:
        stat = json.loads(ecu)
        vECU_name = stat['Name']
        stat['MemUsageTotal'] = stat['MemUsage'].split(' / ')[1]
        stat['MemUsage'] = get_digit(stat['MemUsage'].split(' / ')[0])
        stat['NetIOTotal'] = stat['NetIO'].split(' / ')[1]
        stat['NetIO'] = get_digit(stat['NetIO'].split(' / ')[0])
        stat['BlockIOTotal'] = stat['BlockIO'].split(' / ')[1]
        stat['BlockIO'] = get_digit(stat['BlockIO'].split(' / ')[0])
        stat['CPUPerc'] = get_digit(stat['CPUPerc'])
        stat['MemPerc'] = get_digit(stat['MemPerc'])
        ecu_group_stat[vECU_name] = stat

    ecu_group_stat['timestamp'] = copy.copy(timestamp)

    return ecu_group_stat


def main(docker_stats_log_txt, stats_timeinfo, out_json, out_bin, vecu_num):
    # chunk: the # of vECUs
    CHUNK = vecu_num

    check_input_files(docker_stats_log_txt, stats_timeinfo)

    lines = get_log_contents(docker_stats_log_txt)

    # need to parse "%y%m%d-%H%M%S"
    ts, ts_interval = get_timestamp_info(stats_timeinfo, int(len(lines)/CHUNK))
    timestamp = Timestamp(ts)

    ecu_groups = [lines[i:i+CHUNK] for i in range(0, len(lines), CHUNK)]
    stat_dataset = []
    for ecu_group in ecu_groups:
        #ecu_group_stat = {json.loads(ecu)['Name']:json.loads(ecu) for ecu in ecu_group}
        ecu_group_stat = make_json(ecu_group, timestamp)
        timestamp += ts_interval
        stat_dataset.append(ecu_group_stat)

    with open(out_bin, 'wb') as f:
        pickle.dump(stat_dataset, f)

    # dump to json file
    dump(stat_dataset, out_json)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some input files and parameters about docker_stats')
    
    # params info
    parser.add_argument('-l', '--docker_stat_logfile', type=str, required=True, help='Docker stat log file name')
    parser.add_argument('-t', '--docker_stat_timeinfo', type=str, required=True, help='Docker stat time info file name')
    parser.add_argument('-j', '--out_json', type=str, required=True, help='Output JSON file name')
    parser.add_argument('-b', '--out_bin', type=str, required=True, help='Output binary file name')
    parser.add_argument('-n', '--number_of_vecu', type=int, required=True, help='Number of VECU')

    # parse params
    args = parser.parse_args()

    # print args for debug
    print(f'Docker Stat Logfile: {args.docker_stat_logfile}')
    print(f'Docker Stat Timeinfo: {args.docker_stat_timeinfo}')
    print(f'Output JSON: {args.out_json}')
    print(f'Output Binary: {args.out_bin}')
    print(f'Number of VECU: {args.number_of_vecu}')

    main(
        args.docker_stat_logfile,
        args.docker_stat_timeinfo,
        args.out_json,
        args.out_bin,
        args.number_of_vecu
    )
