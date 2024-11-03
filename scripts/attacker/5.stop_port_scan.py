from scapy.all import *
import random
import pickle
import pdb
import os
from common import update_tcp_chksum


cmd = "ps -ef| grep nmap | grep -v grep | awk '{print $2}'"
os.system(cmd)

cmd = "kill -9 $(ps -ef| grep nmap | grep -v grep | awk '{print $2}' | head -1)"
print(cmd)
os.system(cmd)

