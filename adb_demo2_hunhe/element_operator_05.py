# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　操作设备

import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

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
print(driver.network_connection)  # 查看完目前的网络状态
time.sleep(2)
# 打开飞行模式 两种都可以写
# driver.set_network_connection(0)
# driver.set_network_connection(ConnectionType.AIRPLANE_MODE)

print(driver.network_connection)  # 查看网络
driver.save_screenshot('./test1.png')
print(driver.get_device_time())

# 打开数据
