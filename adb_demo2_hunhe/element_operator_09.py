# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　app操作详解

import time
import os
from appium import webdriver
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    # "appPackage": "com.android.settings",
    # "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": True,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

"""
判断app是否安装
1.没有安装则安装app
2.存在的话卸载之后在安装
3.启动
4.进行加法运算
5.关闭
6.卸载app

com.sky.jisuanji/com.sky.jisuanji.JisuanjizixieActivity

# # 　命令启动指定app
# driver.start_activity("com.android.settings", "com.android.settings.Settings")
# # 上滑操作 scroll  从一个元素移到另一个元素
# web_element_e1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="游戏模式"]')
# web_element_e2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="飞行模式"]')
# driver.scroll(web_element_e1, web_element_e2, 2000)
# driver.find_element(By.XPATH, '//android.widget.TextView[@text="指纹、面部与密码"]').click()
# time.sleep(1)
"""
current = os.path.dirname(__file__)
apk = current + '/jisuanqi_587.apk'
os_apk = os.getcwd() + '\jisuanqi_587.apk'

if driver.is_app_installed("com.ibox.calculators"):
    driver.remove_app("com.ibox.calculators")
driver.install_app(apk)
# 启动app
driver.start_activity("com.ibox.calculators", ".CalculatorActivity")
time.sleep(1)

driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.ibox.calculators:id/digit9"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.ibox.calculators:id/plus"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.ibox.calculators:id/digit7"]').click()
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.ibox.calculators:id/equal"]').click()

# 关闭当前app
driver.close_app()
time.sleep(1)
# 卸载
driver.remove_app("com.ibox.calculators")
