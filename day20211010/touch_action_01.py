#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 8:58
# @Author  : limusem
# @Site    : 
# @File    : touch_action_01.py
# @Software: PyCharm


import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "windwos虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.0.101:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

element_01 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="屏幕锁定"]')

TouchAction(driver).press(element_01).release().perform()
time.sleep(2)
element_02 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="屏幕锁定"]')
TouchAction(driver).press(element_02).release().perform()

time.sleep(2)
element_03 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="图案"]')
TouchAction(driver).press(element_03).release().perform()

"""
339 1287
721 1287
721 1662
721 2043
339 1665
1101 1667
"""
touch_action = TouchAction(driver)
touch_action.press(x=339, y=1297).wait(1000).move_to(x=721, y=1287).wait(1000).move_to(x=721, y=1662).wait(
    1000).move_to(x=721, y=2043).wait(1000).move_to(x=339, y=1665).wait(1000).move_to(x=1101, y=1667).wait(
    1000).release().perform()
