# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 8:36 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : des_setting_demo_01.py
# @Software: PyCharm
# @desc : adb连接命令详解,元素识别

from appium import webdriver

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.ibox.calculators",
    "appActivity": "com.ibox.calculators.CalculatorActivity",
    "udid": "c6c8c4ce",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
# 点击事件
driver.find_element_by_id('com.ibox.calculators:id/digit8').click()
# 输入事件
driver.find_element_by_id('com.ibox.calculators:id/digit8').click()
