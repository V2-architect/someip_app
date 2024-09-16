
import os
import argparse

def do_port_scanning(ip, sport, dport):
    cmd = f"nmap -p {sport}-{dport} {ip}"
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--ip', '-i', type=str, required=True, help='target ip addr')
    parser.add_argument('--sport', '-s', type=int, required=True, help='scanning target sport')
    parser.add_argument('--dport', '-d', type=int, required=True, help='scanning target dport')

    args = parser.parse_args()

    do_port_scanning(args.ip, args.sport, args.dport)
