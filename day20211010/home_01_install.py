# -*- coding: utf-8 -*-
# @Time : 2021/10/13 13:21
# @Author : Limusen
# @File : home_01_install


import time
from appium import webdriver
from appium.webdriver.webdriver import By


des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    # "appPackage": "com.wondertek.paper",
    # "appActivity": "cn.thepaper.paper.ui.main.MainActivity",
    "appPackage": "com.wondertek.paper",
    "appActivity": "cn.thepaper.paper.ui.splash.welcome.LaunchActivity",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
    # 　 "com.wondertek.paper/cn.thepaper.paper.ui.splash.welcome.LaunchActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)
time.sleep(2)