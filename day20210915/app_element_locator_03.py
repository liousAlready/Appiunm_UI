# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc : 计算器的操作


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
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
time.sleep(2)
driver.find_element(By.XPATH, '//android.widget.TextView[@text="在设置中搜索"]').click()
time.sleep(1)
driver.press_keycode(29, 64, 59)  # a 打开左边shift键的开关 按住左边shift键 == A
time.sleep(1)
driver.press_keycode(29, 128, 60)  # a 打开右边的shift键开关  按住右边shift键 == A
time.sleep(1)
driver.press_keycode(29, 1048576)  # a 打开大小写开关
time.sleep(1)
driver.press_keycode(29, 1)  # 1 打开shift键
