# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
#　操作设备

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

#　判断屏幕是否锁屏,锁屏返回false
print(driver.is_locked())
driver.lock(3)
print(driver.is_locked())
time.sleep(2)
driver.unlock()

#　打开通知栏
driver.open_notifications()
time.sleep(3)
# # 切换横屏
# driver.orientation = 'LANDSCAPE'
# time.sleep(3)
# # 切换竖屏
# driver.orientation = 'PORTRAIT'
# time.sleep(3)

size = driver.get_window_size()
# 获取手机屏幕分辨率
print(size)
#  获取当前横竖屏状态
print(driver.orientation)

driver.get_window_size(windowHandle='current')