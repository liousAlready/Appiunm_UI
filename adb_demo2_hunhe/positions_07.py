# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　滑动操作

import time
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}
# com.android.settings/com.android.settings.Settings
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

