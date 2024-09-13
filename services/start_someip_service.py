
import os
import pdb

def is_provider(app_type):
    return app_type.lower() == "p"

def is_consumer(app_type):
    return app_type.lower() == "c"

def start(app):
    app_name, app_type = app.split('_')

    # change directory
    os.chdir(app_name)

    # run SOME/IP app
    if is_provider(app_type):
        #os.system("bash ./run_server.sh")
        print("bash ./run_server.sh")
    elif is_consumer(app_type):
        #os.system("bash ./run_client.sh")
        print("bash ./run_client.sh")
    else:
        print(f"App_type error: {app_type}")
        exit(-1)

def main(apps):
    for app in apps:
        start(app)

if __name__ == "__main__":
    host_apps_filename = "host_someip_app.txt"
    hostname = os.popen("hostname").read().strip()
    someip_apps = ""
    with open(host_apps_filename) as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            _hostname, someip_apps_str = line.split(':')
            if hostname == _hostname:
                someip_apps = someip_apps_str.split(',')

    if not bool(someip_apps):
        print("[Error] No item matched hostname")
        exit(-1)
    print(f"HOSTNAME:     {hostname}")
    print(f"SOME/IP apps: {someip_apps}")
    main(someip_apps)
