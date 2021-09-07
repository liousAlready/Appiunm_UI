# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:20
# @Author : Limusen
# @File : demo_03h5

import time
from appium import webdriver

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
driver.get("http://hao.uc.cn/")

driver.find_element_by_xpath('//input[@class="search-input"]').send_keys("newdream")
driver.find_element_by_xpath('//button[@class="search-btn"]').click()