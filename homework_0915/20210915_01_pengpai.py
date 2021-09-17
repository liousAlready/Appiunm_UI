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

# des = {
#     "platformName": "Android",
#     "platformVersion": "9",
#     "deviceName": "mac虚拟机",
#     "appPackage": "com.wondertek.paper",
#     "appActivity": "cn.thepaper.paper.ui.main.MainActivity",
#     "udid": "192.168.56.104:5555",
#     "noReset": "True"
# }

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

# 查看温度
w = driver.find_element(By.XPATH,
                        '//android.widget.TextView[@resource-id="com.wondertek.paper:id/ths_weather_tv"]').text
print(w)

time.sleep(2)
# 查看朋友圈是否能够点击
# enabled = driver.find_element(By.XPATH, '//android.widget.ImageView[@bounds="[940,2628][1052,2730]"]').is_enabled()
# print(enabled)

enabled = driver.find_element(By.XPATH, '//android.widget.TextView[@text="澎友圈"]').is_enabled()
print(enabled)