#!/usr/bin/python3

import os
import time
import pandas as pd
import numpy as np
import pdb

pcap = '/home/jhshin/K-city_2CAM_40m_5ms-02--anomaly.pcap'

def init(row_number):
    col_names = ['FrameNumber', 'Protocol', 'FrameType', 'AttackType', 'Periodicity', 'Interval']
    df = pd.DataFrame(0, index=range(row_number), columns=col_names)
    df['FrameNumber'] = range(1, len(df) + 1)
    return df


def add_protocol_info(df):
    proto_nums = get_frame_num_per_protocol()

    for proto, frame_nums in proto_nums.items():
        print(f"add {proto} onto the frame_numbers")
        df.loc[df['FrameNumber'].isin(frame_nums), 'Protocol'] = proto

    print("Adding protocol done!")
    print(df)
    return df


def get_frame_num_per_protocol():
    global pcap
    protocol_filters = [
        ['SOMEIPSD', 'someipsd'],
        ['SOMEIP', 'someip and not someipsd'],
        ['UDS', 'uds'],
        ['DOIP', 'doip and not uds'],
        ['TFTP', 'tftp'],
        ['UDP', 'udp and not doip and not someip and not tftp'],
        ['TCP', 'tcp and not doip and not someip and not tftp'],
        ['IP', '(ip or ipv6) and not udp and not tcp'],
        ['ARP', 'arp'],
        ['ICMP', 'icmp'],
        ['IGMP', 'igmp'],
    ]

    '''
    # debug
    protocol_filters = [
        ['SOMEIPSD', 'someipsd']
    ]
    '''

    proto_frame_no = {}
    for proto, filt in protocol_filters:
        cmd = f"bash get_frame_number_by_filter.sh '{pcap}' '{filt}'"
        print(f"bash get_frame_number_by_filter.sh '{pcap}' '{filt}'")
        frame_nums = [int(n) for n in os.popen(cmd).read().strip().split('\n')]
        proto_frame_no[proto] = frame_nums

    return proto_frame_no



def get_frame_num_per_attack_type():
    global pcap

    attack_filters = [
        [1, 'ip.ttl==4'],
        [2, 'ip.ttl==5'],
        [3, 'ip.ttl==6'],
        [4, 'ip.src!=10.0.3.8 and tcp.dstport==46000 and tcp.flags.syn'],
        [5, 'not someip and not tftp and not doip and udp']
    ]

    attack_id_frame_no = {}
    for attack_id, attack_filt in attack_filters:
        cmd = f"bash get_frame_number_by_filter.sh '{pcap}' '{attack_filt}'"
        print(f"bash get_frame_number_by_filter.sh '{pcap}' '{attack_filt}'")
        frame_nums = [int(n) for n in os.popen(cmd).read().strip().split('\n')]
        attack_id_frame_no[attack_id] = frame_nums

    return attack_id_frame_no


def add_attack_info(df):
    attack_id_nums = get_frame_num_per_attack_type()

    # update AttackType(0: Normal, 1-5: AttackType)
    for attack_id, frame_nums in attack_id_nums.items():
        print(f"add attack_id({attack_id}) onto the frame_numbers")
        df.loc[df['FrameNumber'].isin(frame_nums), 'AttackType'] = attack_id

    # update FrameType(0: Normal, 1: Attack)
    df.loc[df['AttackType'] != 0, 'FrameType'] = 1

    print("Adding attack_type done!")
    print(df)
    return df


def get_frame_num_of_periodic_packet():
    global pcap

    intv_20ms_svc_ids = ["1000", "1001", "1001", "1002", "2000", "2004", "3002", "3003"]
    periodic_20ms_filter = " or ".join([f'someip.serviceid==0x{intv}' for intv in intv_20ms_svc_ids])

    periodic_packet_filters = [
        [10,  'someip.serviceid==0x2001'],
        [20,  periodic_20ms_filter],
        [100, 'someip.serviceid==0x1003'],
        [200, 'someip.serviceid==0x3000 or someip.serviceid==0x3001']
    ]

    interval_frame_no = {}
    for intv, periodic_filter in periodic_packet_filters:
        cmd = f"bash get_frame_number_by_filter.sh '{pcap}' '{periodic_filter}'"
        print(f"bash get_frame_number_by_filter.sh '{pcap}' '{periodic_filter}'")
        frame_nums = [int(n) for n in os.popen(cmd).read().strip().split('\n')]
        interval_frame_no[intv] = frame_nums
    return interval_frame_no


def add_periodic_info(df):
    interval_nums = get_frame_num_of_periodic_packet()

    # update interval(0: Non-periodic, 10,20,100,200: interval of periodic packet)
    for interval, frame_nums in interval_nums.items():
        print(f"add interval({interval}ms) onto the frame_numbers")
        df.loc[df['FrameNumber'].isin(frame_nums), 'Interval'] = interval

    # update Periodicity(0: Non-periodic, 1: Periodic)
    df.loc[df['Interval'] != 0, 'Periodicity'] = 1

    print("Adding periodic information done!")
    print(df)
    return df


def main():
    s_time = time.time()
    df = init(1789711)

    # 1. Column: Protocol
    df = add_protocol_info(df)

    # 2,3. Column: AttackType, FrameType
    df = add_attack_info(df)

    # 4,5. Column: Periodicity, Interval
    df = add_periodic_info(df)

    e_time = time.time()
    print(f"elapsed time: {e_time-s_time}s")
    pdb.set_trace()


if __name__ == "__main__":
    main()
