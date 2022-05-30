import subprocess , os, time, datetime
import csv
from subprocess import Popen, PIPE
import requests


delay=60*5    ###for 15 minutes delay
close_time=time.time()+delay
tes = subprocess.check_output("upscmd -u sysop -p sysop ups-psn test.battery.start 5", shell=True)
#print("Send command to UPS : ",tes)

header = ['time','battery_volt']
array = []
array_time = []
while close_time > time.time():

    date = datetime.datetime.now().strftime("%H:%M:%S")
    output = subprocess.check_output("upsc ups-psn 2>&1 battery.voltage | grep -v '^Init SSL'", shell=True)
    out = float(output.rstrip())
    data = ("{},{}".format(date,out))

    array.append(data)
    array_time.append(date)

    #requests.get(f"https://api.telegram.org/bot5018630455:AAGtGqco1EKa4gNcyRJ-UKWvOnoGMKgeKHk/sendMessage?chat_id=-723095568&parse_mode=html&text={}")
    time.sleep(2)
#print(array)
#print(array_time)
upslokasi = subprocess.check_output("upsc -L", shell=True)
hasil = "\n".join(array)

sentmessage = "{}\n\n{}".format(upslokasi,hasil)
print(hasil)
requests.get(f"https://api.telegram.org/bot5018630455:AAGtGqco1EKa4gNcyRJ-UKWvOnoGMKgeKHk/sendMessage?chat_id=-769732161&parse_mode=html&text={sentmessage}")