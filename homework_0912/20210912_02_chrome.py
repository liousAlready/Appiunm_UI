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

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "browserName": "Chrome",
    "udid": "192.168.56.104:5555",
    "noReset": True,
    # "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

# 获取当前所在的位置 混合还是web
print(driver.context)
# 获取所有的
print(driver.contexts)

driver.switch_to.context('NATIVE_APP')
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="允许"]').click()

driver.switch_to.context('CHROMIUM')
time.sleep(1)
driver.find_element(By.XPATH, '//input[@id="index-kw"]').send_keys("李守武")
driver.find_element(By.XPATH, '//button[@id="index-bn"]').click()
