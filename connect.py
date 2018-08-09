from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import string
import time
import os
import datetime
import tkinter

def App(event):
    def worker():
        address = ''.join(random.choices(string.ascii_letters, k=20))
        # options = Options()
        # options.add_argument('--headless')
        current_folder = os.path.dirname(os.path.abspath(__file__))
        driver_path = os.path.join(current_folder, 'chromedriver')
        print("chromedriver-path:" + driver_path)
        driver = webdriver.Chrome(executable_path=driver_path)
        # driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://do-spot.net')

        driver.find_element_by_id("check").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("email").send_keys(address + "@gmail.com")
        driver.find_element_by_id("submit2").click()
        time.sleep(1)
        driver.quit()
        now = datetime.datetime.now()
        os.system("osascript -e 'display notification\"接続に成功しました({})\"'".format(str(now)))
        print("接続に成功しました(" + str(now) + ")")


    interval = 780
    while True:
        worker()
        time.sleep(interval)


root = tkinter.Tk()
root.title("dospot_connect")
root.geometry("300x300+1500+10")
Button = tkinter.Button(text=u'connect', width=50)
Button.bind("<Button-1>",App) 
Button.pack()
root.mainloop()