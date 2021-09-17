# -*- coding: utf-8 -*-
# @Time : 2021/9/17 14:45
# @Author : Limusen
# @File : demo01

import time
from appium import webdriver
from appium.webdriver.webdriver import By

"""

h5元素识别 
混合框架的切换

"""

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "browserName": "Chrome",
    "udid": "c6c8c4ce",
    "noReset": True,
    # "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.get("https://www.baidu.com")  # 进入了webview视图
driver.implicitly_wait(10)
# # 获取当前所在的位置 混合还是web
# print(driver.context)
# # 获取所有的
# print(driver.contexts)
# 切换到native_app
driver.switch_to.context('NATIVE_APP')

## 虚拟机的操作
# driver.find_element(By.XPATH, '//*[@resource-id="com.android.chrome:id/positive_button"]').click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@text="允许"]').click()
# time.sleep(2)

# 真机操作
time.sleep(5)
driver.find_element(By.XPATH,'//*[@text="允许"]').click()

# 切换到chrome
driver.switch_to.context('CHROMIUM')
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="index-kw"]').send_keys("卧室逆蝶")
driver.find_element(By.XPATH, '//button[@id="index-bn"]').click()
