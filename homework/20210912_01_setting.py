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

# 打开声音
driver.find_element(By.XPATH,
                    '//android.widget.LinearLayout[@bounds="[252,1679][1440,1821]"]').click()
time.sleep(1)
# 点击来电时响铃并振动
driver.find_element(By.XPATH, '//android.widget.RelativeLayout[@bounds="[252,1368][1162,1556]"]').click()
# 点击返回按钮
driver.find_element_by_accessibility_id("向上导航").click()