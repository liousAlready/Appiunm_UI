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
    "appPackage": "com.android.dialer",
    "appActivity": "com.android.dialer.TwelveKeyDialer",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "chromedriverExecutable": r"D:\apk\chromedriver.exe",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[0,1170][360,1338]"]').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.ImageView[@bounds="[360,1338][720,1506]"]').click()
time.sleep(1)

# 　获取文本信息
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').text
print(value)

# 获取tag_name
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').tag_name
print(value)
# 获取元素标签名
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').get_attribute("bounds")
print(value)
# 获取大小
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').size
print(value)
# 获取元素左上角的坐标　ｘ，ｙ　用字典返回
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').location
print(value)
# 元素大小跟字典坐标都返回
value = driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').rect
print(value)

#　获取元素之后截屏
driver.find_element_by_xpath(
    '//android.widget.TextView[@resource-id="com.android.dialer:id/dialer_no_match_list_name"]').screenshot(
    './test.png')

#　新建联系人然后清空输入框
# driver.find_element_by_xpath('//android.widget.RelativeLayout[@bounds="[0,72][1080,216]"]').click()
# driver.find_element_by_xpath('//android.widget.EditText[@text="姓名"]').send_keys("ui自动化测试")
# time.sleep(1)
# #　清除操作
# driver.find_element_by_xpath('//android.widget.EditText[@bounds="[279,502][942,642]"]').clear()
