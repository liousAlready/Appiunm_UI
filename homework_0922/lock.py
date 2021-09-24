# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:47
# @Author : Limusen
# @File : Equal_proportion_conversion

import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction
import pytest

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": True,
    "newCommandTimeout": 30  # 30s没对手机发送新命令，就断开连接
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
driver.implicitly_wait(10)

size = driver.get_window_size()

x = size['width']
y = size['height']

x1 = int(x / 2)
y_start = int(y * 4 / 5)
y_end = int(y * 1 / 5)

# # 等比例移动
# TouchAction(driver).long_press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

driver.swipe(start_x=x1, start_y=y_start, end_x=x1, end_y=y_end)

time.sleep(1)

driver.find_element(By.XPATH, '//android.widget.TextView[@text="指纹、面部与密码"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="开启锁屏密码"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="密码选项"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.TextView[@text="图案密码"]').click()
time.sleep(1)

# 267 930
# 517 1200
# 260 1477
# 808 1200

TouchAction(driver).long_press(x=267, y=930).wait(200).move_to(x=517, y=1200).wait(200).move_to(x=260, y=1477).wait(
    200).move_to(x=808, y=1200).release().perform()

time.sleep(1)

TouchAction(driver).long_press(x=267, y=930).wait(200).move_to(x=517, y=1200).wait(200).move_to(x=260, y=1477).wait(
    200).move_to(x=808, y=1200).release().perform()
