# -*- coding: utf-8 -*-
# @Time : 2021/9/8 9:26
# @Author : Limusen
# @File : demo_04hunhe


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
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

time.sleep(1)
driver.find_element_by_android_uiautomator('text("9")').click()

# driver.find_element_by_android_uiautomator("text('9')").click()  # 注意一下　外面要用单引号，里面要用双引号不然会报错不是一个字符串
time.sleep(1)
driver.find_element_by_android_uiautomator('new UiSelector().textContains("0")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.ibox.calculators:id/digit0")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('resourceId("com.ibox.calculators:id/minus")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("8")').click()
time.sleep(1)
driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.ibox.calculators:id/simplePad").childSelector(className("android.widget.LinearLayout").instance(0))').click()

# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("")').click()

# # 使用 uiautomator2 框架
# d = u2.connect('c6c8c4ce')
# d.app_start(package_name="com.ibox.calculators")
# time.sleep(10)
# d(resourceId='com.ibox.calculators:id/digit0').click()
# d(resourceId="com.ibox.calculators:id/minus").click()
