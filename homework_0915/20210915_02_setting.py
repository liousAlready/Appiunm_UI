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
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# 判断当前是否锁屏
print(driver.is_locked())

# 锁屏3s
driver.lock(3)

# 解锁
driver.unlock()
print(driver.is_locked())

# 打开通知栏
driver.open_notifications()

# 横屏操作
driver.orientation = "LANDSCAPE"  # 设置横屏
time.sleep(3)
# 竖屏操作
driver.orientation = "PORTRAIT"  # 设置竖屏
