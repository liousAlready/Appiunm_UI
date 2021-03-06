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
    "appPackage": "com.ibox.calculators",
    "appActivity": "com.ibox.calculators.CalculatorActivity",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# 　点击工具箱
driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.ibox.calculators:id/toolbox_btn_layout")'
).click()
# 获取app的混合应用的WebView值
print(driver.context)
print(driver.contexts)
time.sleep(2)
# driver.switch_to.context('WEBVIEW_chrome')
# time.sleep(1)
# driver.find_element_by_xpath('//p[text()="中华万年历"]').click()
