# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　操作设备

import time
from appium import webdriver

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.dialer",
    "appActivity": "com.android.dialer.TwelveKeyDialer",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)



driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[0,1170][360,1338]"]').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[360,1338][720,1506]"]').click()
time.sleep(1)

# 　新建联系人然后清空输入框
driver.find_element_by_xpath('//android.widget.RelativeLayout[@bounds="[0,72][1080,216]"]').click()
driver.find_element_by_xpath('//android.widget.EditText[@text="姓名"]')

# # 调整音量
# driver.long_press_keycode(24)