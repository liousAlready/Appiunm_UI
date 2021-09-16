# -*- coding: utf-8 -*-
# @Time : 2021/9/7 17:44
# @Author : Limusen
# @File : hybrid_locator_01
# 　点击&滑动操作

import time
from appium import webdriver
from appium.webdriver.webdriver import By
from appium.webdriver.common.touch_action import TouchAction

des = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "vivo x20",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "c6c8c4ce",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# 上滑操作 scroll  从一个元素移到另一个元素
web_element_e1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="游戏模式"]')

web_element_e2 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="飞行模式"]')
driver.scroll(web_element_e1, web_element_e2, 2000)

# driver.find_element(By.XPATH, '//android.widget.TextView[@text="指纹、面部与密码"]').click()
# time.sleep(1)
#
# driver.find_element(By.XPATH, '//android.widget.Button[@text="开启锁屏密码"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//android.widget.Button[@text="密码选项"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//android.widget.TextView[@text="图案密码"]').click()
# time.sleep(1)

e1 = driver.find_element(By.XPATH, '//android.widget.TextView[@text="指纹、面部与密码"]')
touch_action = TouchAction(driver)
# 按住e1,
touch_action.press(e1).release().perform()
time.sleep(1)
e2 = driver.find_element(By.XPATH, '//android.widget.Button[@text="开启锁屏密码"]')
touch_action.long_press(e2, duration=3000).release().perform()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@text="密码选项"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//android.widget.TextView[@text="图案密码"]').click()

# 设置屏幕滑动密码
time.sleep(1)
# 1: 258  929
# 2: 545 929
# 3: 545 1208
# 4: 817 939
touch_action.press(x=258, y=929).wait(1000) \
    .move_to(x=545, y=929).wait(1000) \
    .move_to(x=545, y=1208).wait(1000) \
    .move_to(x=817, y=939).wait(1000) \
    .release().perform()
time.sleep(1)
# long_press 也可以
touch_action.long_press(x=258, y=929).wait(1000) \
    .move_to(x=545, y=929).wait(1000) \
    .move_to(x=545, y=1208).wait(1000) \
    .move_to(x=817, y=939).wait(1000) \
    .release().perform()