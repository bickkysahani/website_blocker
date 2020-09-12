# C:\Windows\System32\drivers\etc
import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
with open('porn.txt') as f:
    website_list = f.read().splitlines()

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23):
        print("working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")


    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()  # here content is now a list
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours")
    time.sleep(5)
