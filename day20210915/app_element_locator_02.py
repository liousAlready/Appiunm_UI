# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:01 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : 20210912_01_setting.py
# @Software: PyCharm
# @desc : 复选框、查看元素、按键操作、截图、网络配置、菜单栏


import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.connectiontype import ConnectionType

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.wondertek.paper",
    "appActivity": "cn.thepaper.paper.ui.main.MainActivity",
    "udid": "192.168.56.104:5555",
    "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

time.sleep(2)


# # 截图
# driver.save_screenshot('pengpai.png')

# # 网络配置
# print(driver.network_connection) # 查看当前网络状态
# driver.set_network_connection(1)  # 飞行模式  0 1 2 4 6
# time.sleep(5)
# driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)  # 全开

# # 获取屏幕分辨率
# print(driver.get_window_size())

# # 打开通知栏
# driver.open_notifications()
#
# print(driver.orientation)
# # 横竖屏设置
# driver.orientation = "LANDSCAPE" # 设置横屏
# time.sleep(3)
# driver.orientation = "PORTRAIT" # 设置竖屏

# # 锁屏3s  ==》 交叉事件
# driver.lock(3)
# print(driver.is_locked()) # 判断是否锁屏，是啧返回false
# # 解锁
# driver.unlock()
# time.sleep(3)
# print(driver.is_locked())
