import subprocess , os
import time, datetime
from subprocess import Popen, PIPE

print("Initial Setup.....")
time.sleep(1)

try :
    sudo_password = 'sysop'
    theUPS = "ups-bpbd-teluk-wondama"
    command = "upsc " + theUPS + " 2>&1 | grep -v '^Init SSL'"
    ups = subprocess.check_output(command, shell=True)
    staleups = ups.decode('UTF-8')
    if "stale" in staleups:
        try:
            command1 = 'systemctl stop nut-server'.split()
            command2 = 'systemctl start nut-server'.split()
            p1 = Popen(['sudo', '-S'] + command1, stdin=PIPE, stderr=PIPE,
                universal_newlines=True)
            sudo_prompt = p1.communicate(sudo_password + '\n')

            time.sleep(5)

            p2 = Popen(['sudo', '-S'] + command2, stdin=PIPE, stderr=PIPE,
                    universal_newlines=True)
            sudo_prompt = p2.communicate(sudo_password + '\n')
            print("sukses")
        except Exception as e:
            raise e

except Exception as e:
    raise e
