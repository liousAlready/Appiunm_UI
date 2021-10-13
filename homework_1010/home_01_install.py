# -*- coding: utf-8 -*-
# @Time : 2021/10/13 13:21
# @Author : Limusen
# @File : home_01_install

import os
import time
from appium import webdriver
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
    # "appPackage": "com.wondertek.paper",
    # "appActivity": "cn.thepaper.paper.ui.splash.welcome.LaunchActivity",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

# 判断设备中是否存在澎湃新闻
if driver.is_app_installed("com.wondertek.paper"):
    driver.remove_app("com.wondertek.paper")  # 如果存在则删除
current_path = os.path.dirname(__file__)
apk_path = os.path.join(current_path, '../apk/pengpai.apk')
driver.install_app(apk_path)  # 安装澎湃新闻
time.sleep(2)
driver.start_activity("com.wondertek.paper", "cn.thepaper.paper.ui.splash.welcome.LaunchActivity")  # 通过活动打开澎湃新闻
