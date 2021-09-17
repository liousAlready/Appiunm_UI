# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　操作设备
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webdriver import By

des = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "mac虚拟机",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.56.104:5555",
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

# 显示等待
e = WebDriverWait(driver, 10).until(
    lambda x: x.find_element(By.XPATH, '//android.widget.TextView[@text="在设置中搜索"]'))
e.click()
