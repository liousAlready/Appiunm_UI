#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 10:35
# @Author  : limusem
# @File    : wait_operatpr_04.py
# @Software: PyCharm
# @Description: 控制打开使劲按


import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "windwos虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.67.101:5555",
    "noReset": "True",
    "newCommandTimeout": 30
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# time.sleep(3)  # 固定等待3秒

# 全局设置，只要设置好了 只要包含 find_element 方法都会产生等待效果
# 等待机制：每隔500ms在页面上检查是否出现该元素，如何在指定的时间内都没找到，则报错
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//android.widget.TextView[@text="屏幕锁定"]')


# # 找不到就会报错
# driver.find_element(By.XPATH, '//android.widget.TextView[@text="屏幕锁定ss"]')


# 创建一个显示等待对象    until() 直到我的内容查找到   until() 需要一个method作为实参
# 工作机制：默认每隔500ms检查页面是否出现该元素，默认值可以通过参数定制
def add(x, y):
    return x + y


add1 = lambda x, y: x + y

WebDriverWait(driver, 30, 0.8).until(lambda x: x.find_element(By.XPATH, '//android.widget.TextView[@text="屏幕锁定"]'))
