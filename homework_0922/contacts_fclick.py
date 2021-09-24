# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:26
# @Author : Limusen
# @File : contacts_fclick


import time
from appium import webdriver
from appium.webdriver.webdriver import By
import pytest
import random

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.contacts",
    "appActivity": "com.android.contacts.DialtactsContactsEntryActivity",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)
driver.flick(start_x=449, start_y=1755, end_x=649, end_y=135)
