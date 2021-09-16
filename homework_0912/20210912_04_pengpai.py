# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc :


import time
from appium import webdriver
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "browserName": "Chrome",
    "udid": "192.168.56.104:5555",
    "noReset": True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.get('http://m.news.cn/')

# 获取当前所在的位置 混合还是web
print(driver.context)
# 获取所有的
print(driver.contexts)

driver.find_element(By.XPATH, '//div[@class="top-nav-pro-cont"]//a[text()="富媒体"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//ul[@class="tabNav"]//li[text()="5G+AI"]').click()
