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

# 查看当前的网络
print(driver.network_connection)
# 设置网络
# 设置飞行模式
# driver.set_network_connection(1)
time.sleep(3)
print(driver.network_connection)
# 设置飞行模式
driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
print(driver.network_connection)
