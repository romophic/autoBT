#!/usr/bin/env python3
#              _        ____ _____  #
#   __ _ _   _| |_ ___ | __ )_   _| #
#  / _` | | | | __/ _ \|  _ \ | |   #
# | (_| | |_| | || (_) | |_) || |   #
#  \__,_|\__,_|\__\___/|____/ |_|   #

# consts
LOGIN_ID = ""
LOGIN_PW = ""
BODYTEMP_LOW = 36.5
BODYTEMP_MAX = 36.7

import random
import time
from selenium import webdriver

def makeBodyTemp() -> str:
  return str(int((random.randrange(int(BODYTEMP_LOW*10),int(BODYTEMP_MAX*10)+1,1)+random.randrange(int(BODYTEMP_LOW*10),int(BODYTEMP_MAX*10)+1,1))/2) / 10)

rawurl = "https://docs.google.com/forms/d/e/1FAIpQLSegJ5_ypMJ10ZSQZbLH-Onkv-Ca2u0xLmJ_xNIRyfFCThM3Jw/viewform?usp=pp_url&entry.1061678014=2021/07/17&entry.1274018874="+makeBodyTemp()


if __name__ == "__main__":
  driver = webdriver.Chrome()
  driver.get(rawurl)

  time.sleep(2)

  driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(LOGIN_ID)
  driver.find_element_by_xpath("//*[@id='identifierNext']").click()

  time.sleep(2)

  driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(LOGIN_PW)
  driver.find_element_by_xpath("//*[@id='passwordNext']").click()

  time.sleep(2)

  driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()

  time.sleep(2)

  driver.close()