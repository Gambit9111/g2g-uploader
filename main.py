import csv
import time
import pyautogui
from goodies import upload, extract_ids

# 1 get the headers
headers =  {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "cookie": ""  ### insert your cookie here
    }


extract_ids(headers)  # 2
print("\n ")
print("----")
print("\n ")
time.sleep(3)

# open csv file with saved ids  # 3
with open('order_ids.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    good = 0
    failed = 0
    failed_urls = []
    for row in csv_reader:
        # make valid link  # 4
        url = f'https://www.g2g.com/order/sellOrder/order?oid={row[0]}'
        print("working on: " + url)

        try:  # 5
            upload(url)   
            good += 1
        except:
            failed += 1
            time.sleep(1)

            failed_urls.append(url)

            # f) close the tab
            x, y = pyautogui.locateCenterOnScreen('images/close.png', confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(1)

            continue

    print("\n ")
    print("----")
    print("\n ")
    print (f"{good} orders were succesful")
    print("\n ")
    print("----")
    print("\n ")
    print (f"{failed} orders failed")
    print("\n ")
    print("----")
    print("\n ")
    for url in failed_urls:
        print(url)