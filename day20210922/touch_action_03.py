# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc : 滑动app页面


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
    "udid": "192.168.228.102:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

time.sleep(2)

e = driver.find_element(By.XPATH, '//android.widget.TextView[@text="显示"]')

# TouchAction(driver).press(e).release().perform()  # 链条指令  点击操作

# long_press BUG：当你把元素作为参数，会把元素的bounds属性， 相加/2 会得出x，y坐标，但是x，y坐标可能出现有小数的情况
# 因为坐标只能是整数，所以会导致报错

# 长按元素
# TouchAction(driver).long_press(el=e, duration=3000).perform()
# [54,1230][162,1338]   54+162/2= 108   1230+1338/2  = 1284
TouchAction(driver).long_press(x=108, y=1284, duration=3000).perform()
