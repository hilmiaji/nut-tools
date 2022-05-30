import subprocess , os, time, datetime
import csv
from subprocess import Popen, PIPE
import requests

array = []

nama_ups = "ups-psn"

delay=60*5              # Delay 5 menit
close_time=time.time()+delay

subprocess.check_output(f"upscmd -u sysop -p sysop {nama_ups} test.battery.start 5", shell=True)


while close_time > time.time():

    date = datetime.datetime.now().strftime("%H:%M:%S")
    output = subprocess.check_output(f"upsc {nama_ups} 2>&1 battery.voltage | grep -v '^Init SSL'", shell=True)
    output2 = subprocess.check_output(f"upsc {nama_ups} 2>&1 ups.status | grep -v '^Init SSL'", shell=True)
    out = float(output.rstrip())
    out2 = output2.rstrip()
    out2 = out2.decode("utf-8")
    data = ("{},{},{}".format(date,out,out2))

    array.append(data)

    time.sleep(2)

upslokasi = subprocess.check_output("upsc -L", shell=True)
hasil = "\n".join(array)
sentmessage = "{}\n{}".format(upslokasi.decode("utf-8"),hasil)
print(hasil)
requests.get(f"https://api.telegram.org/bot5018630455:AAGtGqco1EKa4gNcyRJ-UKWvOnoGMKgeKHk/sendMessage?chat_id=-769732161&parse_mode=html&text={sentmessage}")
