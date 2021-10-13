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
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

current_path = os.path.dirname(__file__)
jisuanqi_path = os.path.join(current_path, '../apk/jisuanqi.apk')
print(jisuanqi_path)

if driver.is_app_installed(' com.ibox.calculators'):
    driver.remove_app('com.ibox.calculators')
driver.install_app(r"D:\Appiunm_UI\apk\jisuanqi_587.apk")
time.sleep(3)
driver.start_activity('com.ibox.calculators', 'com.ibox.calculators.CalculatorActivity')

time.sleep(3)
driver.find_element(By.XPATH, '//android.widget.Button[@text="7"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@text="+"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@text="9"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@text="="]').click()

driver.background_app(5)

time.sleep(6)
driver.activate_app("com.android.settings")
time.sleep(3)
driver.activate_app("com.ibox.calculators")
time.sleep(3)
driver.close_app()