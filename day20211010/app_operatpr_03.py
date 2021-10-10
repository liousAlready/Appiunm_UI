#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 9:41
# @Author  : limusem
# @File    : app_operatpr_02.py
# @Software: PyCharm
# @Description: app相关操作


import time
import os
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "windwos虚拟机",
    "udid": "192.168.67.101:5555",
    "appPackage": "com.ibox.calculators",
    "appActivity": "com.ibox.calculators.CalculatorActivity",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)
time.sleep(3)
driver.close_app()
time.sleep(3)
driver.launch_app() # 重置app 重新打开
