
import os
import pdb

# 현재 스크립트의 파일 경로를 얻음
script_path = os.path.abspath(__file__)

# 디렉토리 경로를 얻음
script_dir = os.path.dirname(script_path)

os.chdir("../services")

service_list = os.popen("ls -d */").read().strip().split("\n")

# at services/
for service in service_list:
    print(f"cp -rf ../scripts/run_*.sh {service}")
    os.system(f"cp -rf ../scripts/run_*.sh {service}")
