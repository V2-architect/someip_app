from scapy.all import *
from scapy.contrib.automotive.someip import *

import time
from datetime import datetime
import struct
import numpy as np
import pdb
import pickle
import sys

f_pkl = sys.argv[1]

with open(f_pkl, 'rb') as f:
    someip_packet = pickle.load(f)
pdb.set_trace()
