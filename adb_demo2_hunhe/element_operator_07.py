# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　点击&滑动操作

import time
from appium import webdriver
from appium.webdriver.webdriver import By

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
}

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# 模拟手指点击  tap([(坐标值,坐标值)])
# 根据坐标点击
# driver.tap([(289, 779)],1000)
# 　点击多组坐标
# driver.tap([(375, 777), (232, 929)], 1000)

# # 上滑操作 scroll  从一个元素移到另一个元素
# web_element_e1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="游戏模式"]')
#
# web_element_e2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="蓝牙"]')
# driver.scroll(web_element_e1, web_element_e2, 3000)

# 滑动操作
# driver.flick(289, 779, 100, 100)

# # 获取屏幕的分辨率
# size = driver.get_window_size()
# print(size)
# # # 从a点滑动至b点
# # driver.swipe(1080/2, 2034/2, 1080/2,2034/4,3000)
#
# driver.swipe(size['width'] / 2, size['height'] / 2, size['width'] / 2, size['height'] / 4, 3000)


# # 　函数 已知屏幕分辨率 x y 447 1426 == ？
# #   447/x*100 1426/y*100
# def calc(x, y):
#     return (x / 1440.0, y / 2960.0)
#
#
# print(calc(447, 1426))  # 元素坐标
