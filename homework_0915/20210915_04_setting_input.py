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
from appium.webdriver.connectiontype import ConnectionType

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.find_element(By.XPATH, '//android.widget.TextView[@text="在设置中搜索"]').click()
time.sleep(1)
# 按住左边shift再按c
driver.press_keycode(31, 64)
# 按住右边shift再按c
driver.press_keycode(31, 128)
#
driver.press_keycode(31,1048576)

driver.press_keycode(31,1)

time.sleep(2)

driver.save_screenshot('c.jpg')