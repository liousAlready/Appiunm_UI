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
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.find_element_by_id('')