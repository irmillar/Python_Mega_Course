import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"C:\Windows\WinSxS\amd64_microsoft-windows-w..ucture-other-minwin_31bf3856ad364e35_10.0.17134.1_none_1ac029cdce3c581c"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "gmail.com", "www.gmail.com", "mail.google.com", "www.mail.google.com"]
test_file = r"C:\Users\Ian\Desktop\Python\10-Apps\Website Blocker\test.txt"

while True:
    if 8 < dt.now().hour < 17:
        print("Working Hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    continue
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)
