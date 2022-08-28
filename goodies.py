import pyautogui
import time
import webbrowser
import requests
from bs4 import BeautifulSoup
import csv



#---------------------order_ids extractor |  requests
def extract_ids(headers):
    # list of orders where video needs to be uploaded
    url = "https://www.g2g.com/payment/floating?cur=USD"

    # open the url with headers attached
    req = requests.get(url, headers=headers)

    # snag that into soup
    soup = BeautifulSoup(req.text, "lxml")

    # get all orders ids from html
    orders = soup.find_all("td", class_="floating-balance__table-hold-date")[::2]

    # write everything to csv file
    with open('order_ids.csv', "w") as write_file:
        csv_writer = csv.writer(write_file, lineterminator = '\n')

        # write every element, split removes spaces after characters
        for i in orders:
            print(i.text)
            csv_writer.writerow(i.text.split())

# --------------------uploader | pyautogui 

#chrome path
path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
def upload(url):
# 1) open a new chrome window
# 2) opens a tab in the new window
    webbrowser.get(path).open(url)
    time.sleep(2.5)
# 3) make sure the screen is in 100% and night mode on
# 4) click the upload buttons
    # a)
    x, y = pyautogui.locateCenterOnScreen('images/uploadscreenshot.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1.5)
    # b)
    x, y = pyautogui.locateCenterOnScreen('images/uploadplus.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1.5)
    # c) upload image
    pyautogui.write('image.png')
    pyautogui.press('enter')
    time.sleep(4)
    # d) submit button
    x, y = pyautogui.locateCenterOnScreen('images/submit.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(2.5)
    # f) close the tab
    x, y = pyautogui.locateCenterOnScreen('images/close.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1.5)