#!/usr/bin/env python3

#              _        ____ _____  #
#   __ _ _   _| |_ ___ | __ )_   _| #
#  / _` | | | | __/ _ \|  _ \ | |   #
# | (_| | |_| | || (_) | |_) || |   #
#  \__,_|\__,_|\__\___/|____/ |_|   #

# consts
LOGIN_ID = ""
LOGIN_PW = ""
BODYTEMP_MIN = 36.5
BODYTEMP_MAX = 36.7

import time
import random
import datetime
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def makeTime() -> str:
    return str(datetime.datetime.now().strftime("%Y/%m/%d"))

def makeBodyTemp() -> str:
    return str(int((random.randrange(int(BODYTEMP_MIN*10),int(BODYTEMP_MAX*10)+1,1)+random.randrange(int(BODYTEMP_MIN*10),int(BODYTEMP_MAX*10)+1,1))/2) / 10)

def submitTemp(submittime:str, submittemp:str):
    rawurl = "https://docs.google.com/forms/d/e/1FAIpQLSegJ5_ypMJ10ZSQZbLH-Onkv-Ca2u0xLmJ_xNIRyfFCThM3Jw/viewform?usp=pp_url&entry.1061678014=" + \
        submittime + "&entry.1274018874=" + \
        submittemp
    print(rawurl)

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

    print("done")


if __name__ == "__main__":
    submitTemp(makeTime(), makeBodyTemp())
