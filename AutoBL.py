import random
import datetime

tem = random.randrange(5,9)
temp = str(36) + '.' + str(tem)

from selenium import webdriver
import pandas as pd
import time

#ここにメールアドレスとパスワードを入力
Login_ID = ''
Login_pass = ''

#ここにwebdriverのパスを指定
browser = webdriver.Chrome(executable_path = 'C:\\Users\\DELL\\Google ドライブ\\プログラミング\\chromedriver.exe')

url_login = "https://docs.google.com/forms/d/e/1FAIpQLSegJ5_ypMJ10ZSQZbLH-Onkv-Ca2u0xLmJ_xNIRyfFCThM3Jw/viewform?usp=pp_url&entry.1061678014=[0]&entry.1274018874="+temp
browser.get(url_login)
time.sleep(3)

element = browser.find_element_by_id('identifierId')
element.clear()
element.send_keys(Login_ID)

browser_from = browser.find_element_by_class_name('VfPpkd-vQzf8d')
time.sleep(3)
browser_from.click()

time.sleep(3)
element = browser.find_element_by_name('password')
element.clear()
element.send_keys(Login_pass)

browser_from = browser.find_element_by_class_name('VfPpkd-vQzf8d')
time.sleep(3)
browser_from.click()


