
import os
import sys


if sys.argv[1] == "front":
    os.system("python3 ~/someip_app/libavtp/my_example/frontcam.py | ~/someip_app/libavtp/my_example/ieciidc-talker -i veth0.2 --prio=1 -d 91:ef:00:00:fe:00")

if sys.argv[1] == "rear":
    os.system("python3 ~/someip_app/libavtp/my_example/rearcam.py | ~/someip_app/libavtp/my_example/ieciidc-talker -i veth0.2 --prio=1 -d 91:ef:00:00:fe:01")
