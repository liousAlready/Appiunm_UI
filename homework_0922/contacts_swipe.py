# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:32
# @Author : Limusen
# @File : contacts_swipe


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

# vivo手机按住联系人会有弹出框
# driver.swipe(start_x=544, start_y=1471, end_x=502, end_y=227, duration=3000)
