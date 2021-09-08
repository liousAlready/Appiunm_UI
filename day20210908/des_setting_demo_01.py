# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 8:36 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : des_setting_demo_01.py
# @Software: PyCharm
# @desc : adb连接命令详解,安装apk并打开

from appium import webdriver

des = {
    "automationName": "Appium",  # 默认是配置appium
    "platformName": "Android",  # 平台名称 ios/android/firefox Os
    "platformVersion": "8.1.0",  # 安卓的版本
    "deviceName": "vivo x20",  # 随便填 没关系
    "app": "/Users/lishouwu/Downloads/CalcTest.apk",
    "appPackage": "com.sky.jisuanji",  # 包名
    "appActivity": "com.sky.jisuanji.JisuanjizixieActivity",  # 活动入口
    "udid": "c6c8c4ce",  # adb连接的设备名称
    "noSign": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
