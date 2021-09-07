# -*- coding: utf-8 -*-
# @Time : 2021/9/7 14:22
# @Author : Limusen
# @File : demo_02h5


import time
from appium import webdriver

# des = {
#     "platformName": "Android",
#     "platformVersion": "10.0",
#     "deviceName": "小米",
#     "browserName": "chrome",
#     "appPackage": "com.tencent.mtt",
#     "appActivity": ".MainActivity",
#     "udid": "7592904",
#     "noReset": True,
#     "unicodeKeyboard": True,
#     "resetKeyboard": True,
#     "chromedriverExecutable": r"D:\apk\chromedriver.exe"
# }

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "browserName": "Chrome",
    "udid": "c6c8c4ce",
    "noReset": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")
time.sleep(3)
# 语法跟ui自动化一样
driver.find_element_by_xpath("//*[@id='index-kw']").send_keys("newdream")
driver.find_element_by_id('index-bn').click()
