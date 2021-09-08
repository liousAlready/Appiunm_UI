# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01


import time
from appium import webdriver

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "uni.UNIDD11F28",
    "appActivity": "io.dcloud.PandoraEntry",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)
time.sleep(2)
# 　点击工具箱
# driver.find_element_by_android_uiautomator('text("资讯")').click()
# driver.find_element_by_xpath('//android.widget.Button[@text="5"]').click()
driver.find_element_by_xpath('//android.widget.TextView[@text="资讯"]').click()
time.sleep(2)
# 获取app的混合应用的WebView值
print(driver.contexts)
print(driver.current_context)
