'''To run it from terminal open terminal as administrator and change the host path
To run it as a background process change the extension to .pyw
To run it automatically, open Task Scheduler and create a new task'''

import time
from datetime import datetime as dt

hosts_temp=r"D:\Python project\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","facebook.com"]

while True:
    if 8<=dt.now().hour<=16:
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websites:
                if website not in content:
                    file.write(redirect+" "+website+"\n")
    else:
         with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)