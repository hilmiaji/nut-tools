import subprocess , os
import time, datetime
from subprocess import Popen, PIPE

print("Initial Setup.....")
time.sleep(1)
nama_UPS = "ups"

def restart_ups():
    try:
        command1 = 'systemctl stop nut-server'.split()
        command2 = 'systemctl stop nut-monitor'.split()
        command3 = 'systemctl start nut-server'.split()
        command4 = 'systemctl start nut-monitor'.split()
        p1 = Popen(['sudo', '-S'] + command1, stdin=PIPE, stderr=PIPE,
            universal_newlines=True)
        sudo_prompt = p1.communicate(sudo_password + '\n')

        p2 = Popen(['sudo', '-S'] + command2, stdin=PIPE, stderr=PIPE,
                universal_newlines=True)
        sudo_prompt = p2.communicate(sudo_password + '\n')
        
        time.sleep(5)
        
        p3 = Popen(['sudo', '-S'] + command3, stdin=PIPE, stderr=PIPE,
                universal_newlines=True)
        sudo_prompt = p2.communicate(sudo_password + '\n')
        
        p4 = Popen(['sudo', '-S'] + command4, stdin=PIPE, stderr=PIPE,
                universal_newlines=True)
        sudo_prompt = p2.communicate(sudo_password + '\n')
        print("sukses")
    except Exception as e:
        raise e

try :
    sudo_password = 'sysop'
    
    command = "upsc " + nama_UPS + " 2>&1 | grep -v '^Init SSL'"
    ups = subprocess.check_output(command, shell=True)
    ups_status = ups.decode('UTF-8')
    if "stale" in ups_status:
        restart_ups()
    if "not connected" in ups_status:
        restart_ups()
    if "Error" in ups_status:
        restart_ups()
    else:
        print("tidak ada error ditemukan")

except Exception as e:
    raise e
